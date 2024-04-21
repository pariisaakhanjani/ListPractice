Sum = 0
multiple = 0
user_input = int(input("Give me a number and I will give you its Sum Square Difference:"))

for i in range(1, user_input+1):
    multiple = multiple + (i*i)
    Sum = Sum + i
    
print(Sum*Sum)
print(multiple)
print(Sum*Sum - multiple)