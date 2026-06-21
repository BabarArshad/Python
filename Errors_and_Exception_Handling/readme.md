# **Python Errors & Exception Handling**

## **1. Types of Errors in Python**

Python errors occur when something goes wrong during program execution.  
They fall into two main categories: **Syntax Errors** and **Exceptions**.

---

### **1.1 Syntax Errors (code is written incorrectly)**

These errors occur **before** the program runs.  
Python cannot execute the code at all.

#### ❌ Example: Missing colon → `SyntaxError`

```python
# Missing colon -> SyntaxError
if True
    print("Hello")
```

**Output:**

```
SyntaxError: invalid syntax
```

✔ Python stops immediately because the code structure is invalid.

---

### **1.2 Exceptions (runtime errors)**

These errors occur **while the program is running**.  
The syntax is correct, but something unexpected happens.

#### ❌ Example: Division by zero

```python
print(10 / 0)
```

**Output:**

```
ZeroDivisionError: division by zero
```

✔ Code is valid, but execution fails.

---

## **2. Exception Handling in Python**

To prevent programs from crashing, Python provides **try/except blocks**.

### **Basic Structure**

```python
try:
    # risky code
except:
    # what to do if it fails
else:
    # runs if no error happens
finally:
    # always runs
```

- **try** — code that might cause an error  
- **except** — handles the error  
- **else** — runs only if no error occurs  
- **finally** — always runs (cleanup, closing files, etc.)

