#Question 1 : Write a Python program to print all Prime numbers in an Interval. 
num1 = int(input("Enter the lower limit :"))
num2 = int(input("Enter the upper limit  :"))
print("Prime no between ",num1," and ",num2, "are :")
for n in range(num1,num2+1):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            print(n)
            


#Question 2 Write a Python Program for factorial of a numbe
num1 = int(input("Enter the number :"))
if num1<0 : 
    print("Error!Number less than 0")
else:
    print("Factorial of ",num1," is :")
    fact=1
    for n in range(1,num1+1):
        fact=fact*n
    print(fact)



#Question 3 Find the sum of n numbers by using the while loop
num1 = int(input("Enter the number :"))
print("Sum of ",num1," is :")
total=0
n=1
while (n<=num1):
    total=total+n
    n=n+1
print(total)