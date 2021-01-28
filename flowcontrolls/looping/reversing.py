num=int(input("enter the number :"))
result=""
while(num!=0):
    rev=num%10
    result+=str(rev)
    num=num//10
print(result)