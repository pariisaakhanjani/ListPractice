# Write a Python program to get the smallest number from a list.

numbers = []
user_input = input("please enter some numbers separated by comma. Then I will give you the smallest.")
user_input_splitted = user_input.split(",")
for item in user_input_splitted:
    number = int(item)
    numbers.append(number)
numbers.sort()
print(numbers)
smallest = numbers[0]
print(smallest)