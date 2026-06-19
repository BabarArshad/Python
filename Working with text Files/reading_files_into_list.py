# reading files into list

# 1. f.read().splitlines() method
with open('configuration.txt') as f:
    lines = f.read().splitlines()
print(lines)
print('*' * 50)

