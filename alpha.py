count=0
f=open(r"C:\Users\aniru\Documents\intro.txt",'r')
rd=f.read()
for i in range(len(rd)):
    if rd[i].isupper():
        count+=1
print("Number of uppercase alphabet:",count)
f.close()
