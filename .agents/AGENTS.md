# Agent Rules — cursosFC_UNAM

## Git & Version Control
- **Never run `git push`**. The user pushes manually.
- `git add` and `git commit` are fine after verifying changes work.
- Write clear, concise commit messages in English.

## Development Workflow (TDD-lite)
1. **Verify first** — before editing, run the relevant build/test to confirm the current state.
2. **Make the smallest change** that fixes or adds the intended behavior.
3. **Test after** — run `make site-build`, `make site-dev`, or the relevant script to confirm the fix works.
4. **Only then commit** — stage and commit locally with a descriptive message.
5. If multiple issues exist, fix them one at a time (one commit per fix).

## Code Style
- Keep Markdown notes Obsidian-compatible (YAML frontmatter, wikilinks).
- Preserve existing comments and docstrings unless explicitly told to remove them.
- When editing config files (YAML, JSON, Makefile), keep formatting consistent with the rest of the file.

## Documentation
- Update `README.md` when changing user-facing setup steps, dependencies, or workflows.
- Do not rewrite large sections unnecessarily — make targeted edits.

## Communication
- Be concise. Summarize what changed and why.
- If something is ambiguous, ask before acting.
- Present a plan before making architectural or multi-file changes.
