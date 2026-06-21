# Python Functions 

A structured reference covering Python functions from the ground up, with networking-focused examples throughout.

---

## Table of Contents

1. [Introduction to Functions](#1-introduction-to-functions)
2. [Return Statement](#2-return-statement)
3. [Positional and Keyword Arguments](#3-positional-and-keyword-arguments)
4. [Default Arguments](#4-default-arguments)
5. [Variable-Length Arguments — `*args` and `**kwargs`](#5-variable-length-arguments----args-and-kwargs)
6. [Lambda Expressions](#6-lambda-expressions)
7. [Namespaces and Scopes](#7-namespaces-and-scopes)

---

## 1. Introduction to Functions

Functions let you group code into reusable blocks, making programs easier to read and maintain.

```python
def my_function():
    print("Hello from Babar!")
    x = 10
    print(x ** x)

my_function()  # Can be called as many times as needed
my_function()
my_function()
```

```
Hello from Babar!
10000000000
Hello from Babar!
10000000000
Hello from Babar!
10000000000
```

> **Note:** Defining a function does not run it. You must *call* it to execute the code inside.

---

## 2. Return Statement

A `return` statement sends a value back to the caller. This is different from simply printing a value.

Think of it like a server responding to a client request — the server processes the input and sends back a result.

### 2.1 Basic Return

```python
def add(a, b):
    result = a + b
    return result

result = add(10, 5)
print(result)  # Output: 15
```

### 2.2 Print vs. Return

```python
def add_print(a, b):
    print(f"Sum: {a + b}")   # Prints but returns nothing

def add_return(a, b):
    return a + b              # Returns the value for reuse

add_print(10, 20)             # Output: Sum: 30
my_sum = add_return(5, 2)
print(my_sum)                 # Output: 7

print(add_print(1, 2))        # Output: Sum: 3  \n  None
```

> A function without a `return` statement implicitly returns `None`.

### 2.3 The `pass` Statement

Use `pass` as a placeholder when a function hasn't been implemented yet.

```python
def func():
    pass

x = func()
print(x)  # Output: None
```

### 2.4 Returning Multiple Values

A function can return more than one value — Python packs them into a tuple automatically.

```python
def my_func(x):
    return x, x**2, x**3, x**4

print(my_func(3))  # Output: (3, 9, 27, 81)
```

**Tuple unpacking:**

```python
a, b, c, d = my_func(10)
print(a, b, c, d)  # Output: 10 100 1000 10000
```

**Extended unpacking:**

```python
x, *y = my_func(4)
print(x, y)  # Output: 4  [16, 64, 256]
```

---

## 3. Positional and Keyword Arguments

There are four types of function arguments in Python:

| Type | Description |
|------|-------------|
| Positional | Passed in order; position matters |
| Keyword | Passed by name; order doesn't matter |
| Default | Have a fallback value if not provided |
| Variable-length | Accept any number of arguments (`*args`, `**kwargs`) |

### 3.1 Positional Arguments

Arguments are matched to parameters by position. The count must match exactly.

```python
def difference(a, b):
    result = a - b
    print(result)

difference(10, 5)  # Output: 5
```

> **Parameters vs. Arguments:** Parameters are the placeholders in the function definition (`a`, `b`). Arguments are the actual values passed when calling the function (`10`, `5`).

### 3.2 Keyword Arguments

You can pass arguments by name, which makes the order irrelevant.

```python
def func(x, y, z):
    print(f"x = {x}")
    print(f"y = {y}")
    print(f"z = {z}")

func(z=30, x=10, y=20)
```

```
x = 10
y = 20
z = 30
```

### 3.3 Mixing Positional and Keyword Arguments

```python
func(6, z=1, y=9)
```

```
x = 6
y = 9
z = 1
```

> **Rule:** Positional arguments must always come *before* keyword arguments. `func(x=6, 1, z=9)` will raise a `SyntaxError`.

---

## 4. Default Arguments

A default argument provides a fallback value when no argument is supplied by the caller.

### 4.1 Networking Example

```python
def connect_to_server(host, port=80):
    print(f"Connecting to {host} on port {port}...")

connect_to_server("example.com")        # Output: Connecting to example.com on port 80...
connect_to_server("example.com", 443)   # Output: Connecting to example.com on port 443...
```

> **Rule:** Default arguments must always be placed *after* non-default arguments. The following raises a `SyntaxError`:
>
> ```python
> def connect_to_server(port=80, host):  # ❌ Invalid
>     ...
> ```

---

## 5. Variable-Length Arguments — `*args` and `**kwargs`

### 5.1 The Problem They Solve

Standard positional, keyword, and default arguments all have a fixed parameter count. What if you don't know how many values you'll receive?

```python
def ping_devices(ip1, ip2):  # Only works for exactly 2 devices
    print(f"Pinging {ip1}...")
    print(f"Pinging {ip2}...")
```

If a customer has 20 switches, you'd have to rewrite the function. `*args` solves this.

### 5.2 `*args` — Variable Positional Arguments

`*args` collects any number of positional arguments into a **tuple**.

```python
def ping_devices(*devices):
    for device in devices:
        print(f"Pinging {device}...")

# Works for any number of devices — today:
ping_devices("192.168.1.1", "192.168.1.2")

# Next week — no changes needed:
ping_devices(
    "192.168.1.1",
    "192.168.1.2",
    "192.168.1.3",
    "192.168.1.4",
    "192.168.1.5"
)
```

```
Pinging 192.168.1.1...
Pinging 192.168.1.2...
Pinging 192.168.1.3...
Pinging 192.168.1.4...
Pinging 192.168.1.5...
```

> `args` is a **tuple** — you can iterate over it but not modify it.

### 5.3 `**kwargs` — Variable Keyword Arguments

`**kwargs` collects any number of keyword arguments into a **dictionary**.

**The problem without `**kwargs`:**

Imagine a device configuration script that sometimes needs hostname + IP, sometimes needs hostname + IP + DNS + NTP + SNMP. You'd end up defining dozens of optional parameters:

```python
def configure_device(
    hostname=None,
    ip=None,
    gateway=None,
    dns=None,
    ntp=None,
    snmp=None,
    contact=None,
    location=None,
    ...
):
```

**The solution with `**kwargs`:**

```python
def configure_device(**kwargs):
    print(kwargs)

configure_device(
    hostname="SW1",
    ip="192.168.1.10",
    dns="8.8.8.8",
    location="Datacenter"
)
```

```
{'hostname': 'SW1', 'ip': '192.168.1.10', 'dns': '8.8.8.8', 'location': 'Datacenter'}
```

> `kwargs` is a **dictionary** — each keyword argument becomes a `key: value` pair.

### 5.4 Why Not Use `*args` for Everything?

Without keyword names, it's impossible to tell which value is which:

```python
configure_device("SW1", "192.168.1.10", "255.255.255.0", "8.8.8.8")
# Which one is DNS? Which is the subnet mask?
```

With `**kwargs`, the intent is always clear.

### 5.5 Real-World Example — Switch Configuration

```python
def create_switch(**kwargs):
    for command, value in kwargs.items():
        print(f"{command} {value}")

create_switch(
    hostname="CORE1",
    domain="company.local",
    ntp="192.168.100.5",
    snmp="public",
    vlan=100
)
```

```
hostname CORE1
domain company.local
ntp 192.168.100.5
snmp public
vlan 100
```

No need to pre-define `hostname`, `domain`, `ntp`, `snmp`, or `vlan` inside the function — it accepts whatever you pass.

---

## 6. Lambda Expressions

A lambda is a small, anonymous (unnamed) single-expression function. Use it when you need a quick function without formally defining one.

### 6.1 Normal Function vs. Lambda

```python
# Normal function
def square(x):
    return x * x

print(square(5))  # Output: 25
```

```python
# Equivalent lambda
square = lambda x: x * x

print(square(5))  # Output: 25
```

> **When to use lambdas:** Simple, short-lived logic only. If your function needs multiple lines or conditionals, use a normal `def` instead.

---

## 7. Namespaces and Scopes

### 7.1 What Is a Namespace?

A namespace is where Python stores variable names and what they refer to. Think of it like VLANs in a network:

```
Head Office
│
├── VLAN 10 → Printer, Laptop, Server
├── VLAN 20 → Printer, Laptop
└── VLAN 30 → Printer
```

Every VLAN can have a device called `Printer` without conflict — each VLAN is its own namespace.

```python
hostname = "CORE1"        # Global namespace

def configure():
    hostname = "ACCESS1"  # Local namespace
    print(hostname)

configure()       # Output: ACCESS1
print(hostname)   # Output: CORE1
```

### 7.2 What Is Scope?

Scope is where Python is *allowed* to look for a variable. Python follows the **LEGB** rule:

| Level | Name | Description |
|-------|------|-------------|
| L | **Local** | Inside the current function |
| E | **Enclosing** | In any outer (enclosing) function |
| G | **Global** | At the top level of the module |
| B | **Built-in** | Python's built-in names (`print`, `len`, `max`, etc.) |

### 7.3 Local Scope

```python
def configure():
    hostname = "SW1"  # Only exists inside this function
    print(hostname)

configure()  # Output: SW1
```

### 7.4 Enclosing Scope

```python
def outer():
    hostname = "CORE1"

    def inner():
        print(hostname)  # Found in enclosing scope

    inner()

outer()  # Output: CORE1
```

### 7.5 Global Scope

```python
hostname = "CORE1"  # Global

def configure():
    print(hostname)  # Not found locally → looks globally

configure()  # Output: CORE1
```

### 7.6 Built-in Scope

Python's built-in functions (`print`, `len`, `max`, `min`, etc.) live in the built-in namespace. When Python can't find a variable in local, enclosing, or global scope, it looks here last.

---

*End of guide.*
