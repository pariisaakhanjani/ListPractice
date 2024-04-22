#The last input number before user_input

user_input = int(input("please print a number and I will tell you the prime number before that number:"))

for i in range(user_input-1, 1, -1):
    isprime = True
    for j in range(2,i):
        if i % j == 0:
            isprime = False
    if isprime == True:
        print("the last prime number before", user_input, "is", i)
        break
    else:
        continue