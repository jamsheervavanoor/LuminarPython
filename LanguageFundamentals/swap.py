#swap
num1=10
num2=20
temp=num1
num1=num2
num2=temp
print(num1)
print(num2)

#without temporary variable

num1=num1+num2#num1=10+20=30
num2=num1-num2#num2=30-20=10
num1=num1-num2#num1=30-10=20

#simple logic

num1,num2=num2,num1