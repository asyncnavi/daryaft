"""Check local inline-link paths and the unpublished backlog dependency graph."""

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

REQUIRED = ('README.md', 'AGENTS.md', 'CLAUDE.md', 'docs/README.md',
            'docs/engineering/PROJECT_STATUS.md', 'docs/planning/BACKLOG.md')
FIELDS = ('Problem statement', 'Why it matters', 'Scope', 'Out of scope',
          'Acceptance criteria', 'Test requirements', 'Dependencies',
          'Priority', 'Labels', 'Documentation requirements', 'Security considerations')


def check(root):
    errors = []
    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append(f'missing required file: {name}')
    files = [root / name for name in REQUIRED[:3]]
    for folder in ('docs', '.github'):
        files.extend(sorted((root / folder).rglob('*.md')))
    for path in files:
        if not path.is_file():
            continue
        content = re.sub(r'^```.*?^```[^\n]*', '', path.read_text(), flags=re.M | re.S)
        for target in re.findall(r'\]\(([^\s)]+)\)', content):
            url = urlsplit(target.strip('<>'))
            if url.scheme or url.netloc or not url.path:
                continue
            if not (path.parent / unquote(url.path)).is_file():
                errors.append(f'broken local link: {path.relative_to(root)} -> {target}')
    backlog = root / 'docs/planning/BACKLOG.md'
    if not backlog.is_file():
        return errors
    text = backlog.read_text()
    sections = re.findall(r'^## (D\d{2}) ([^\n]+)\n(.*?)(?=^## |\Z)', text, re.M | re.S)
    if not sections:
        errors.append('backlog has no draft entries')
    graph = {}
    for key, title, body in sections:
        if key in graph:
            errors.append(f'duplicate draft ID: {key}')
        for field in FIELDS:
            if not re.search(rf'^{re.escape(field)}: \S', body, re.M):
                errors.append(f'missing field: {key} {field}')
        dependency = re.search(r'^Dependencies: (.+)$', body, re.M)
        graph[key] = re.findall(r'\bD\d{2}\b', dependency.group(1)) if dependency else []
    declared = re.search(r'These (\d+) draft IDs', text)
    if not declared or int(declared.group(1)) != len(sections):
        errors.append('backlog declared count does not match entries')
    for key, dependencies in graph.items():
        for dep in dependencies:
            if dep not in graph:
                errors.append(f'unknown dependency: {key} -> {dep}')
    remaining = dict(graph)
    while remaining:
        ready = {key for key, deps in remaining.items() if not set(deps) & remaining.keys()}
        if not ready:
            errors.append('dependency cycle: ' + ', '.join(sorted(remaining)))
            break
        remaining = {key: deps for key, deps in remaining.items() if key not in ready}
    return errors


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    failures = check(args.root.resolve())
    for failure in failures:
        print(f'FAIL: {failure}', file=sys.stderr)
    if not failures:
        print('PASS: required inputs, local inline-link paths, backlog fields, counts and dependencies')
    sys.exit(bool(failures))
