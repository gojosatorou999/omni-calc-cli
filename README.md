# OmniCalc CLI 🧮

An advanced, feature-rich Command Line Interface (CLI) calculator written in Python. OmniCalc supports complex mathematical expressions, scientific functions, and maintains a session history.

## Features

- **Basic Arithmetic**: Addition, subtraction, multiplication, division, exponentiation, and modulo.
- **Scientific Functions**: `sin`, `cos`, `tan`, `sqrt`, `log`, `log10`, `exp`, `abs`, and `round`.
- **Constants**: Built-in support for `pi` and `e`.
- **Interactive Mode**: A clean REPL (Read-Eval-Print Loop) environment for quick calculations.
- **Single Expression Mode**: Pass expressions directly via command line arguments.
- **History**: Track your calculations during the session.

# Installation

Ensure you have Python 3.x installed.

```bash
# Clone the repository
git clone https://github.com/gojosatorou999/omni-calc-cli.git

# Navigate to the directory
cd omni-calc-cli
```

## Usage

### Interactive Mode
Simply run the script without any arguments:
```bash
python calculator.py
```

Inside the interactive mode:
- Type your expression (e.g., `(pi * 5**2) / 2`) and press Enter.
- Type `history` to see previous calculations.
- Type `help` for a list of supported operations.
- Type `quit` or `exit` to leave.

### Direct Expression Mode
Evaluate a single expression from your terminal:
```bash
python calculator.py "sqrt(144) * sin(pi/2)"
```

## Supported Operations

| Type | Examples |
| :--- | :--- |
| **Operators** | `+`, `-`, `*`, `/`, `**` (power), `%` (modulo) |
| **Functions** | `sqrt(x)`, `sin(x)`, `cos(x)`, `tan(x)`, `log(x)`, `exp(x)`, `abs(x)` |
| **Constants** | `pi`, `e` |

## License
MIT
