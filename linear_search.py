L=[1,2,3,4,5,6,7]
n=int(input("Enter item to be searched:"))
a=len(L)
for i in range(a):
    if L[i]==n:
        print("Item found")
    else:
        print("Item not found")
        break
