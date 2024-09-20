first_string = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_string = ['Task', 'Git', 'Comprehensions', 'Java', 'Computer', 'Assembler']

first_result = [len(new_string) for new_string in first_string if len(new_string) >= 5]
second_result = [(x, y) for x in first_string for y in second_string if len(x) == len(y)]
third_result = {new_string: len(new_string) for new_string in (first_string + second_string)
                if len(new_string) % 2 == False}

print(first_result)
print(second_result)
print(third_result)
