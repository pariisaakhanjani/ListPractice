devisorofInput = []
user_input = int(input("Enter a number and I will tell you which prime numbers it is made of:"))
biggest = 0
for i in range(1, user_input+1):
    if user_input % i == 0:
        devisorofInput.append(i)
print(devisorofInput)



def IsPrime(x):
    isprime = True
    for k in range(2, j):
        if j % k == 0:
            isprime = False
    return isprime




for j in devisorofInput:
    #if j is prime => print j
    
    if IsPrime(j) == True:
        print(j)
        if biggest < j:
            biggest = j
print("the biggest factor is", biggest)




