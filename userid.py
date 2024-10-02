import csv
a=[["userid1","password1"],
   ["userid2","password2"],
   ["userid3","password3"],
   ["userid4","password4"],
   ["userid5","password5"]]
n=input("Enter username:")
file=open(r"sample.csv",'w+')
w1=csv.writer(file)
w1.writerows(a)
file.seek(0)
w2=csv.reader(file)
for i in w2:
    if i[0]==n:
        print("The password is: ",i[1])
        break 
file.close()
