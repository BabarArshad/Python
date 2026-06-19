
# Python Dictionaries

## 1. What Is a Dictionary?

A **dictionary** stores data in **key:value** pairs.  
It is:

- **Ordered** (Python 3.7+)
- **Changeable**
- **Does not allow duplicate keys**

A **key** must be **immutable** (string, number, tuple).  
A **value** can be **any type**, including lists, tuples, or even other dictionaries.

### Example: Creating a Dictionary

```python
Person = { 'Name': 'John', 'Age': 30, 'City': 'New York' }
print(type(Person))  
print(Person)
```

**Output:**

```
<class 'dict'>
{'Name': 'John', 'Age': 30, 'City': 'New York'}
```

### Other Ways to Create Dictionaries

```python
d1 = dict(Name='John', Age=30, City='New York')
d2 = dict()  # recommended for empty dictionary
```

---

## 2. Working With Dictionaries

### Creating and Accessing Values

```python
person = {'name': 'John', 'age': 30, (1, 2, 3): 100}
print(len(person))  
```

**Output:**

```
3
```

### Updating Values

```python
person['name'] = 'Jane'
print(person)
```

### Adding New Key:Value Pairs

```python
person['location'] = 'New York'
print(person)
```

### Accessing Values

```python
a = person['age']
print(a)
```

### Using `get()`

```python
value = person.get('name', 'key does not exist')
print(value)
```

### Removing Items

```python
name = person.pop('name')
print(name, person)

del person['age']
print(person)
```

---

## 3. Nested Dictionaries

```python
Germany = {
    'cities': ['Berlin', 'Hamburg', 'Munich'],
    'info': {
        'population': 83000000,
        'people': ['Einstein', 'Beethoven', 'Goethe']
    }
}

print(Germany['cities'][0])
print(Germany['info']['people'])
print(Germany['info']['people'][1])
```

### List of Dictionaries

```python
Countries = [
    {
        'name': 'Germany',
        'cities': ['Berlin', 'Hamburg', 'Munich'],
        'info': {'population': 83000000, 'people': ['Einstein', 'Beethoven', 'Goethe']}
    },
    {
        'name': 'France',
        'cities': ['Paris', 'Lyon', 'Marseille'],
        'info': {'population': 67000000, 'people': ['Napoleon', 'Voltaire', 'Renoir']}
    }
]

print(Countries[0]['name'])
print(Countries[1]['cities'][2])
```

---

## 4. Dictionary Operations & Methods

### Assignment by Reference

```python
person = {'name': 'John', 'age': 30, 'location': 'USA'}
friend = person

friend['age'] = 25
print(person)
print(friend)
```

### Copying a Dictionary

```python
neighbor = person.copy()
person['location'] = 'Europe'
print(neighbor, person)
```

### Updating a Dictionary

```python
countries = {'USA': 'Washington, D.C.', 'France': 'Paris', 'Japan': 'Tokyo'}
countries.update({'Germany': 'Berlin', 'India': 'New Delhi'})
print(countries)
```

### Clearing a Dictionary

```python
person.clear()
print(person, friend)
```

---

## 5. Dictionary Views: Keys, Values, Items

### `keys()`

```python
person = {'name': 'Alice', 'age': 28, 'city': 'New York'}

k = person.keys()
print(k)
print(type(k))
print(list(k))
```

### `values()`

```python
print(person.values())
print(list(person.values()))
```

### `items()`

```python
print(person.items())
```

### Membership Tests

```python
print('name' in person)
print(10 in person.keys())
print('New York' in person.values())
print(('age', 28) in person.items())
```

---

## 6. Dictionary View Behavior

### Views Reflect Changes

```python
d1 = {10: 'a', 20: 'b', 30: 'c'}
v = d1.values()
d1[10] = 'x'
print(v)
```

### Set Operations on Keys

```python
d1 = {10: 'a', 20: 'b'}
d2 = {20: 'c', 30: 'c'}

k1 = d1.keys()
k2 = d2.keys()

print(k1 & k2)  # intersection
print(k1 | k2)  # union
```

---

## 7. Looping Through Dictionaries

### Loop Through Keys

```python
for k in person.keys():
    print(f'Key is {k}')
```

### Loop Through Values

```python
for v in person.values():
    print(f'Value is {v}')
```

### Loop Through Keys and Access Values

```python
for k in person.keys():
    print(f'Key is {k} and the value is {person[k]}')
```

### Loop Through Key:Value Pairs

```python
for k, v in person.items():
    print(f'Key is {k} and the value is {v}')
```

---

