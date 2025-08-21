#Q1. Write a program to print the factorial of a number using a for loop.

i = int(input())
factorial = 1
for i in range(1, i+1):
    factorial *= i
print(factorial)

#Q2. Write a program that prints all numbers from 1 to 100 that are divisible by 7 but not a multiple of 5

for num in range(1,101):
    if num % 7 == 0 and num % 5 != 0:
            print(num)

#Q3. Write a program that takes a number and prints whether it is a palindrome or not.

n = input("enter number: ")
if n == n[::-1]:
    print("it is palindrome.")
else:
    print("it is not palindrome.")