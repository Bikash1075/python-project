# declare 3 varibles (f0,f1,f2)
# assign values, f0=0, f1=1,f2=0
# for creating fibonacci series
# take input from user



n=int(input("Enter last number "))
f0=0
f1=1
f2=0 #will hold the sum for later durt=ing iteration
for i in range(0,n+1):
    if n<=0:
       f1=f0+f1
    else:
        f0=f1
        f1=f2
        f2=f0+f1
        print(f2,end=" ")
