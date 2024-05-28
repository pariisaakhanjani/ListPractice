def add(x : int,y : int):
    return x + y

def mul(x : int,y : int):
    return x * y

userInput1 = int(input("please print first number you want to add/multiply:"))
userInput2 = int(input("please print second number you want to add/multiply:"))

resultAdd = add(userInput1, userInput2)
resultMul = mul(userInput1, userInput2)

print(resultAdd, resultMul)
