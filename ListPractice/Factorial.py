number = int(input("please enter a number and I will give you its factorial:"))
 
for i in range(1, number+1):
    print(i, end='')
    print("! =", end = '')
    myFactorial = 1
    for j in range(1, number+1):
        if j<=i:
            myFactorial = myFactorial*j
            print(j , end = '')
            if i==j:
                print("=", end = '')
            else:
                print("*", end = '')
        else:
            continue
    print(myFactorial)
