# Even or Odd

num=int(input("enter a number: "))
if num % 2 == 0:
    print("even")
else:
    print("odd")

#factorial
num= int (input("enter a number: "))
fact=1
for i in range (1, num+1):
    fact*=i
print("factorial=", fact)

#sum of two numbers
a = int (input("First number :"))
b = int (input("Second number :"))

print("sum =", a+b)
