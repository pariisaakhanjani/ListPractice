# Write a Python program to sum all the items in a list.
numbers = []
costumer_input = input ("please enter numbers separated by comma, so that I sum them up for you:")
costumer_input_splitted = costumer_input.split(",")
for item in costumer_input_splitted:
    itemchanged = int(item)
    numbers.append(itemchanged)
print(numbers)


print(sum(numbers))