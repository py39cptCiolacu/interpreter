---

## 🧠 Expression Interpreter (Educational)

This project also includes a simple **expression interpreter** implemented in Python with a strong educational focus.

Its goal is to help understand the fundamentals of parsing and evaluating arithmetic expressions from scratch — without relying on Python’s `eval()` function.

### 🧪 What It Does

- ✅ Evaluates arithmetic expressions like:
1 + 2*8 - 3 + 5 
- ✅ Alocation of values to variables like:
x = 2
y2 = 21
- ✅ Handles operator precedence correctly (`*` before `+`)
- ✅ Easily extensible to add new operators

### 🔧 How It Works

The interpreter uses the **Pratt Parsing** technique — a top-down operator precedence parsing method.

Key components:
- **Lexer**: Converts input string into tokens
- **Parser**: Builds an abstract syntax tree (AST)
- **Evaluator**: Recursively computes the result

### 🧑‍🏫 Why Pratt Parsing?

Pratt parsing is:
- Easy to implement and reason about
- Powerful enough to handle real-world arithmetic expressions
- A great introduction to writing interpreters and compilers

### 🧩 Usage Example

```python
python interpreter/main.py
```

Then you can just write your expression inside the shell.
