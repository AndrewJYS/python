import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'number.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

with open(filename) as f:
    nums = json.load(f)

print(nums)