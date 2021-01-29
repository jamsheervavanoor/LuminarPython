num=int(input("enter the number :"))
sum=0
for i in range(1,(num+1)):
    temp=str(num)*i
    sum+=int(temp)
print(sum)
