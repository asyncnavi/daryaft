"""Run known-bad controls against isolated copies of the foundation."""

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / 'scripts/check_foundation.py'


class FoundationControls(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ('README.md', 'AGENTS.md', 'CLAUDE.md'):
            shutil.copy(ROOT / name, self.root / name)
        shutil.copytree(ROOT / 'docs', self.root / 'docs')
        shutil.copytree(ROOT / '.github', self.root / '.github')
        self.backlog = self.root / 'docs/planning/BACKLOG.md'

    def run_check(self, expected=None):
        result = subprocess.run([sys.executable, str(CHECKER), '--root', str(self.root)],
                                capture_output=True, text=True)
        if expected is None:
            self.assertEqual(result.returncode, 0, result.stderr)
        else:
            self.assertEqual(result.returncode, 1, result.stderr)
            self.assertIn(expected, result.stderr)

    def test_valid_baseline(self):
        self.run_check()

    def test_missing_required_input(self):
        self.backlog.unlink()
        self.run_check('missing required file: docs/planning/BACKLOG.md')

    def test_broken_link(self):
        with (self.root / 'README.md').open('a') as stream:
            stream.write('\n[Missing](missing.md)\n')
        self.run_check('broken local link: README.md -> missing.md')

    def test_unknown_dependency(self):
        self.backlog.write_text(self.backlog.read_text().replace('Dependencies: none.', 'Dependencies: D99.', 1))
        self.run_check('unknown dependency: D01 -> D99')

    def test_cycle(self):
        self.backlog.write_text(self.backlog.read_text().replace('Dependencies: none.', 'Dependencies: D02.', 1))
        self.run_check('dependency cycle:')

    def test_duplicate_id(self):
        self.backlog.write_text(self.backlog.read_text().replace('## D02 ', '## D01 ', 1))
        self.run_check('duplicate draft ID: D01')

    def test_missing_field(self):
        self.backlog.write_text(self.backlog.read_text().replace('Acceptance criteria:', 'Removed field:', 1))
        self.run_check('missing field: D01 Acceptance criteria')

    def test_wrong_count(self):
        self.backlog.write_text(self.backlog.read_text().replace('These 26 draft IDs', 'These 25 draft IDs', 1))
        self.run_check('backlog declared count does not match entries')

    def test_empty_backlog(self):
        self.backlog.write_text('# Backlog\n')
        self.run_check('backlog has no draft entries')


if __name__ == '__main__':
    unittest.main()
