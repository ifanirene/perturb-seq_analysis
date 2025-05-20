# Guidelines for Codex Agents

This repository contains bioinformatic analyses implemented in Python. When making changes, follow these general conventions:

- Use **Python 3.9** or newer.
- Keep code compliant with [PEP8](https://www.python.org/dev/peps/pep-0008/) and format with `black`.
- Lint new or modified Python files with `flake8` before committing.
- Document functions and modules using NumPy-style docstrings.
- Place analysis scripts in logically named directories; prefer `.py` modules over Jupyter notebooks when possible.
- If you add external dependencies, list them in `requirements.txt`.

## Programmatic checks

Run the following commands from the repository root when applicable:

```bash
flake8
pytest
```

`pytest` can be skipped if no tests are present, but `flake8` should always pass.
