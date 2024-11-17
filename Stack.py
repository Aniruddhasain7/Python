def push(a):
    v=int(input("Enter value to insert: "))
    a.append(v)
    print("Elements inserted successfully...")
def popitem(a):
    x=a.pop()
    print("Popped element=",x)
def peek(a):  
    print("Topmost item ->",a[-1])
def display(a):
    for i in range(len(a)-1,-1,-1):
        print(a[i])
a=[]
while True:
    ch=int(input(" 1-> Push \n 2-> Pop \n 3-> Peek \n 4-> Display \n 5-> Exit \n Enter your Choice: "))
    if ch==1:
        push(a)
    elif ch==2:
        if len(a)>0:
            popitem(a)
        else:
            print('underflow')
    elif ch==3:
        if len(a)>0:
            peek(a)
        else:
            print("underflow")
    elif ch==4:
        if len(a)>0:
            display(a)
        else:
            print("underflow")
    elif ch==5:
        break
    else: 
        print("Invalid choice!!!")
