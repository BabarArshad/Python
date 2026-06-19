# **Python Sets**

## **1. Introduction**
A **set** in Python is a *mutable* collection that stores **unique**, **unordered** elements.  
Because sets have no defined order, there is no concept of a “first” or “second” element — items are simply stored without duplicates.

### **Real‑world examples**
Sets naturally represent collections where duplicates are not allowed:

- email addresses  
- IP and MAC addresses  
- website domains  
- social security numbers  
- any identifier that must be unique  

### **Immutability rule**
A set is mutable, but **its elements must be immutable**.

**Valid set elements:**  
- integers  
- floats  
- strings  
- tuples  
- frozensets  

**Invalid (mutable) elements:**  
- lists  
- dictionaries  
- other sets  

### **Common use case**
Sets are often used to **remove duplicates** from lists or other data structures.

---

## **2. Code Examples (intro_to_sets.py)**

```python
# Creating a set
s1 = {1, 2, 3, 'a', 'b', 4, 5, 6}
print(s1)  # sets are unordered

# print(s1[0])  # ERROR: sets do not support indexing

# Sets are mutable
s1.add((1, 2, 3))  # adding a tuple (immutable)
print(s1)

s1.remove('a')  # removing an element
print(s1)

# Trying to add a list (mutable) will cause an error
l1 = [1, 2]
# s1.add(l1)  # TypeError: unhashable type: 'list'

# Creating empty sets
s2 = set()
s3 = {}  # this is NOT a set, it's a dictionary
print(type(s2))
print(type(s3))

# Converting other types to sets
s4 = set('helooooooo')  # duplicate letters removed
print(s4)

s5 = set((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(s5)

s6 = set([1, 2, 3, 4, 'abr'])
print(s6)

# Removing duplicate MAC addresses
macs = [
    '00:0a:95:9d:68:16',
    '00:0a:95:9d:68:16',
    '00:0a:95:9d:68:16',
    '00:0a:95:9d:68:30'
]

macs_addresses = set(macs)
print(macs_addresses)
print(len(macs_addresses))  # sets work with len()

# Converting back to a list
macs_addresses = list(set(macs))
print(macs_addresses)

# Looping through a set
for item in s4:
    print(item)

# Membership test
print('x' in s4)  # False
```

---

## **3. Program Output**

```
{1, 2, 3, 'b', 4, 5, 6, 'a'}
{1, 2, 3, 'b', 4, 5, 6, (1, 2, 3), 'a'}
{1, 2, 3, 'b', 4, 5, 6, (1, 2, 3)}
<class 'set'>
<class 'dict'>
{'o', 'h', 'l', 'e'}
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
{1, 2, 3, 4, 'abr'}
{'00:0a:95:9d:68:16', '00:0a:95:9d:68:30'}
2
['00:0a:95:9d:68:16', '00:0a:95:9d:68:30']
o
h
l
e
False
```

babar, **now I fully get what you want** — a clean, structured, GitHub‑ready Markdown section for:

**Set Methods — Part 1: add, remove, discard, pop, clear, copy**

Here is the **perfectly formatted `.md` block**, following the same style as your previous Sets document:

- Proper `#`, `##`, `###` hierarchy  
- Clean spacing  
- Code blocks  
- Output section  
- RAG‑friendly structure for your future agent  

Just copy‑paste this into your `.md` file.

---

# **Set Methods — Part 1**

## **1. Equality vs Identity**
Sets compare **values**, not order.

```python
set1 = {1, 2, 3}
set2 = {3, 2, 1}

print(set1 == set2)  # True (same elements)
print(set1 is set2)  # False (different objects)
```

Lists, strings, and tuples **do not** behave this way:

```python
print([1, 2, 3] == [3, 2, 1])  # False (order matters)
```

---

## **2. set.add(item)**
Adds a single element to the set.  
If the element already exists, nothing happens.

```python
s1 = {1, 2, 3}
s1.add('a')
s1.add(4.5)
print(s1)

s1.add(1)  # does nothing (1 already exists)
print(s1)
```

---

## **3. set.remove(item)**
Removes an element.  
If the element does **not** exist → **raises an error**.

```python
s1.remove(3)
print(s1)

# s1.remove(3)  # ERROR: 3 is not in the set
```

---

## **4. set.discard(item)**
Removes an element **if it exists**.  
If it does **not** exist → **no error**.

```python
s1.discard('a')
print(s1)

s1.discard('X')  # does nothing
print(s1)
```

---

## **5. set.pop()**
Removes and returns **a random element** (because sets are unordered).

```python
x = s1.pop()
print(x, s1)
```

### **Important:**  
`pop()` does **not** remove the “first” element — sets have no order.

---

## **6. Mutability and Shared References**
If two variables reference the same set, modifying one affects the other.

```python
s2 = set('abc')
s3 = s2  # both point to the same set
s3.add('x')

print(s2)  # s2 also changes
```

---

## **7. set.clear()**
Removes **all elements** from the set.

```python
s3.clear()
print(f's2: {s2}, s3: {s3}')
```

---

## **8. set.copy()**
Creates a **shallow copy** of the set.

```python
s4 = s1.copy()
print(f's1: {s1}, s4: {s4}')
```

---

# **Program Output**

```
True
False
False
{1, 2, 3, 'a', 4.5}
{1, 2, 3, 'a', 4.5}
{1, 2, 'a', 4.5}
{1, 2, 4.5}
{1, 2, 4.5}
c {'a', 1, 2, 4.5}
{'c', 'b', 'a', 'x'}
s2: set(), s3: set()
s1: {1, 2, 4.5}, s4: {1, 2, 4.5}
```



# **Set Methods — Part 2**

## **1. Intersection**
The **intersection** of two sets returns the elements that exist in *both* sets.

### **Method:** `set.intersection(other_set)`  
### **Operator:** `&`

```python
set1 = {1, 3, 5}
set2 = {5, 7, 9}

set3 = set1.intersection(set2)
print(f'set3: {set3}')  # {5}

set3 = set1 & set2
print(f'set3: {set3}')  # {5}
```

---

## **2. Difference**
The **difference** returns elements that exist in the first set but *not* in the second.

### **Method:** `set.difference(other_set)`  
### **Operator:** `-`

```python
set4 = set1.difference(set2)
print(f'set4: {set4}')  # {1, 3}

set4 = set1 - set2
print(f'set4: {set4}')  # {1, 3}
```

### **Important:**  
You can pass a list to `difference()`, but **not** to the `-` operator.

```python
# set1.difference([1, 2, 3])  # valid
# set1 - [1, 2, 3]            # ERROR
```

---

## **3. Symmetric Difference**
The **symmetric difference** returns all elements that are in either set,  
**except** the ones that appear in *both*.

### **Method:** `set.symmetric_difference(other_set)`  
### **Operator:** `^`

```python
set5 = set1.symmetric_difference(set2)
print(f'set5: {set5}')  # {1, 3, 7, 9}

set5 = set1 ^ set2
print(f'set5: {set5}')  # {1, 3, 7, 9}
```

---

## **4. Union**
The **union** returns all elements from both sets, with duplicates removed.

### **Method:** `set.union(other_set)`  
### **Operator:** `|`

```python
set6 = set1.union(set2)
print(f'set6: {set6}')  # {1, 3, 5, 7, 9}

set6 = set1 | set2
print(f'set6: {set6}')  # {1, 3, 5, 7, 9}
```

---

## **5. isdisjoint()**
Checks whether two sets have **no elements in common**.

```python
s1 = {1, 3, 5}
s2 = {5, 6, 7}

print(s1.isdisjoint(s2))  # False (5 is common)

s3 = {8, 9}
print(s1.isdisjoint(s3))  # True (no overlap)
```

---

## **6. Comparison Operators**
Sets support comparison operators to check subset/superset relationships.

```python
print({1, 3} < {1, 3, 5})  # True (subset)
```

### **Common operators:**
- `<`  → proper subset  
- `<=` → subset  
- `>`  → proper superset  
- `>=` → superset  
- `==` → equal sets  
- `!=` → not equal  

---

# **Program Output**

```
set3: {5}
set3: {5}
set4: {1, 3}
set4: {1, 3}
set5: {1, 3, 7, 9}
set5: {1, 3, 7, 9}
set6: {1, 3, 5, 7, 9}
set6: {1, 3, 5, 7, 9}
False
True
True
```

---


# **Frozensets**

## **1. Introduction**
A **frozenset** is an **immutable** version of a regular Python set.  
Once created, a frozenset **cannot be modified** — you cannot add, remove, or change elements.

This immutability makes frozensets useful in situations where regular sets **cannot** be used, such as:

- keys in dictionaries  
- elements inside other sets  

Regular sets are mutable and therefore **unhashable**, but frozensets are hashable.

---

## **2. Creating Frozensets**

### **From a list**
```python
fs1 = frozenset([1, 2, 3, 'a', 'b'])
print(fs1, type(fs1))
```

### **From a string**
Each character becomes an element in the frozenset.

```python
s1 = 'BABAR is an amazing person'
fs2 = frozenset(s1)
print(fs2)
```

### **Empty frozenset**
```python
fs3 = frozenset()
```

---

## **3. Frozenset Operations**
Frozensets support most **set operations**, but since they are immutable, they do **not** support:

- `.add()`  
- `.remove()`  
- `.discard()`  
- `.clear()`  

They **do** support:

- intersection  
- difference  
- union  
- symmetric difference  
- subset/superset comparisons  

### **Intersection**
```python
fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([3, 4, 5, 6])

fs3 = fs1.intersection(fs2)
print(fs3)  # frozenset({3, 4})
```

---

## **4. Mixing Sets and Frozensets**
When performing operations between a **set** and a **frozenset**, the result type depends on the operation:

```python
s1 = {4, 10, 20}

result1 = s1.intersection(fs1)  # set ∩ frozenset → set
result2 = fs1 - s1              # frozenset - set → frozenset

print(f'result1 type: {type(result1)}')
print(f'result2 type: {type(result2)}')
```

---

# **Program Output**

```
frozenset({1, 2, 3, 'a', 'b'}) <class 'frozenset'>
frozenset({' ', 'i', 'g', 'r', 'm', 's', 'n', 'B', 'p', 'o', 'z', 'a', 'A', 'b', 'e'})
frozenset({3, 4})
result1 type: <class 'set'>
result2 type: <class 'frozenset'>
```

