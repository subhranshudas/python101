# Modern Python Setup

This guide outlines a modern Python development setup using pyenv and Poetry.

## Prerequisites

- macOS (Homebrew is used for installation)
- Terminal access

## Installation

### 1. Install Homebrew (if not already installed)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2. Install pyenv

```bash
brew install pyenv
```

Add the following to your shell configuration (~/.zshrc or ~/.bash_profile):

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```

### 3. Install Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Verify the installation:

```bash
poetry --version
```

## Setting Up a New Project

1. Create a new project directory:

```bash
mkdir python101
cd python101
```

2. Set the Python version using pyenv:

```bash
pyenv install 3.12.0  # or your desired version
pyenv local 3.12.0
```

3. Initialize a new Poetry project:

```bash
poetry init
```

4. Add project dependencies:

```bash
poetry add requests  # example: adding the requests library
```

5. Create your main Python file (e.g., `main.py`)

6. Run your project:

```bash
poetry run python main.py
```

## Understanding pyenv and Poetry

- **pyenv**: Manages Python versions at the system/user level
- **Poetry**: Manages project dependencies and virtual environments

## Project Structure

A typical project structure might look like this:

```
python101/
├── .python-version
├── pyproject.toml
├── poetry.lock
├── main.py
└── .gitignore
```

## Best Practices

- Use `.gitignore` to exclude unnecessary files (e.g., `__pycache__/`, `*.pyc`, `.venv/`)
- Keep your Python versions up to date with pyenv
- Regularly update your project dependencies with Poetry

Happy coding!
