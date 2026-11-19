# Tools

- `rubric.py`: the single source for the rubric and test cases. Its
  `render_evals_md()` produces `skill/pencil/references/evals.md`.
- `rubric_v0.2.py`: the rubric as used in CS-002.

Both files contain absolute paths from the workspace they were written in.
Import them for `render_evals_md()` and the `CASES`, `CRITICAL` and
`FORMAT` data; do not run them as scripts without changing the paths.
