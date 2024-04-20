devisorofInput = []
user_input = int(input("Enter a number and I will tell you which prime numbers it is made of:"))

for i in range(1, user_input+1):
    if user_input % i == 0:
        devisorofInput.append(i)
print(devisorofInput)

for j in devisorofInput:
    #if j is prime => print j
    isprime = True
    for k in range(2, j):
        if j % k == 0:
            isprime = False
    if isprime == True:
        print(j)

        