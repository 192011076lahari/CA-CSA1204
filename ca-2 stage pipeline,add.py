a= int(input("enter a no.1:"))
b= int (input(" enter a no.2"))
c=4
f=0
ch=int(input("1.add,2.sub,3.mul,4.div"))
if ch==1:
    res=a+b
elif ch==2:
    res=a-b
elif ch==3:
    res=a*b
elif ch==4:
    if(b==0):
        print("wrong input")
        f=1
    else:
        res=a/b
else:
    print("wrong input")
    f=1
if f==0:
    print("the cycle value is:",c)
ins=int(input("enter no. of instructions:"))
print("the performance measure:",ins/c)
print("res=",res)
