# Agent workflow

## Shared context and pstack

Read `AGENTS.md`, current status, and relevant requirements before editing. Both agents use the same repository instructions. `CLAUDE.md` imports them rather than maintaining a second policy.

At inspection, Codex pstack 0.9.120 and Claude pstack 0.9.117 were enabled. Preserve each runtime's model sheet. The current upstream installation instructions are at <https://github.com/michael-denyer/pstack-claude#install>. Recheck those instructions before any install or upgrade. Do not reinstall an enabled plugin blindly.

Align plugin versions deliberately and verify routing in fresh sessions. Codex hook trust must be checked in the application. A model sheet with routing enabled is not proof that a hook executed. No global plugin settings were changed during foundation setup.

## Task loop

1. Select one Ready GitHub issue and read its dependencies. Until remote setup, select an unpublished draft and say so.
2. Read relevant product, architecture, and security requirements.
3. Write a short plan with data shape, scope, acceptance checks, and expected blockers.
4. Implement the smallest complete change.
5. Add meaningful behavior tests and run relevant checks.
6. Review security implications and update documentation.
7. Obtain independent review. An unavailable reviewer blocks acceptance, not unrelated work.
8. Prepare the PR locally. Push only after explicit approval.
9. Update the issue with evidence. Done requires independently verified acceptance criteria.
10. Record results and the next action in the dated journal.

For long work, maintain a local checklist and append-only decision trail in `.audit/`. Break work into units that end with an observed check. Do not start multiple feature implementations at once.

## Handoff

Record the branch, selected issue or draft, changed files, commands and outcomes, open review findings, external blockers, and next action in the journal or status document. Keep secrets and unrelated session transcripts out of handoffs.
