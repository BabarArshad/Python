# WORKING WITH DICTIONARIES IN PYTHON

person = {'name': 'John', 'age': 30, (1, 2, 3): 100}  # example of creating a dictionary with a tuple as a key
print (len(person))  # Output: 3 because there are 3 key:value pairs in the dictionary

person ['name'] = 'Jane'  # example of changing the value of an existing key in the dictionary
print(person)  # Output: {'name': 'Jane', 'age': 30, (1, 2, 3): 100}

person['location'] = 'New York'  # example of adding a new key:value pair to the dictionary
print(person)  # Output: {'name': 'Jane', 'age': 30,
a = person['age']  # example of accessing the value of a key in the dictionary
print(a)  # Output: 30

value = person.get('name', 'key does not exist')  # example of accessing the value of a key in the dictionary using the get() method
print(value)  # Output: Jane

name = person.pop('name')  # example of removing a key:value pair from the dictionary using the pop() method
print(name, person)  # Output: Jane {'age': 30, (1, 2, 3): 100, 'location': 'New York'}

del person['age']  # example of removing a key:value pair from the dictionary using the del statement
print(person)  # Output: {(1, 2, 3): 100, 'location': 'New York'}   

Germany = {
    'cities': ['Berlin', 'Hamburg', 'Munich'],
    'info': {'population': 83000000, 'people': ['Einstein', 'Beethoven', 'Goethe']}
}
print(Germany['cities'][0])  # Output: Berlin
print(Germany['info']['people'])  # Output: ['Einstein', 'Beethoven', 'Goethe']
print(Germany['info']['people'][1])  # Output: Beethoven


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

print(Countries[0]['name'])  # Output: Germany
print(Countries[1]['cities'][2])  # Output: Marseille




