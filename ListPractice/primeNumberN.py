user_input = int(input("Tell me the number of the prime number you want to know:"))
number = 2
counter = 0

while True:
    isprime = True
    for i in range(2,number):
        if number % i == 0:
            isprime = False
    if isprime==True:
        counter = counter + 1
        if counter == user_input:
            print(number)
            break
    number = number + 1
