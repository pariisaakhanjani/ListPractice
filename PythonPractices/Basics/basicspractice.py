randomlist = [9, 23, 45, 17, 32, 87, 11, 56, 3, 72, 8, 41, 25, 64]
numberofItems = len(randomlist)

for i in range(numberofItems):
    for j in range(i):
        print(randomlist[j], end = ' ')
    print()
    
print("\n##############\n")


for i in range(numberofItems):
    Sumofrows = 0
    for j in range(i):
        Sumofrows += randomlist[j]
    print(Sumofrows, end = ' ')
    print()
    
print("\n##############\n")

for i in range(numberofItems):
    Sumofrows = 0
    for j in range(i):
        Sumofrows += randomlist[j]
        if j != i-1:
            print(randomlist[j], end = '+')
        else:
            print(randomlist[j], end = '=')
    print(Sumofrows)
    print()
