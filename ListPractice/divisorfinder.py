devisorofInput = []
user_input = int(input("Enter a number and I will give you its devisors:"))

for i in range(1, user_input+1):
    if user_input % i == 0:
        devisorofInput.append(i)
print(devisorofInput)