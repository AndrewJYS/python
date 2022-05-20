# part 1
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)


# part 2
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())


# part 3
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
print(lines)
for line in lines:
    print(line.rstrip())