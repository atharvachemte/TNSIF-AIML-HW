# Q1. Write a program to take 5 numbers from the user and store them in a tuple, then print the maximum and minimum.

a = list(map(int,input("Enter numbers: ").split()))

b = tuple(a)
maxi = 0
mini = 0
for n in b:
    if n > maxi:
        maxi = n
    if n < mini:
        mini = n
print("maximum is:" ,maxi, "minimum is: ",mini)        

# Q2. Given a tuple of integers, write a program to count how many elements are divisible by 3.

a = (3,6,9,10)
count = 0
for n in a:
    if n % 3 == 0:
        count += 1
print(count)

# Q3. Write a program to reverse the contents of a tuple without using reversed()

a = (1,2,3,4,5)

a = list(a)
a.reverse()

a = tuple(a)
print(a)