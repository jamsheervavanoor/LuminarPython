num=int(input("enter the number :"))
cube=0
while(num!=0):
    rev=num%10
    cube+=rev*rev*rev
    num//=10
print(cube)