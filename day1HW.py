#Q1. Write a program that takes the radius as input and calculates the area and circumference of a circle.

r = int(input("Enter Radius: "))

area = 3.14 * r * r
circumference = 2 * 3.14 * r

print("area: ",area)
print("circumference: ",circumference)

#Q2. Write a program to check if a number is divisible by both 3 and 5.
num = int(input("Enter number: "))

if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible")


#Q3. Write a program that takes a 4-digit number from the user and prints the sum of its digits.

num = input("Enter number: ")
sum = 0
for n in num:
    sum += int(n)

print("sum of digits is ",sum)    