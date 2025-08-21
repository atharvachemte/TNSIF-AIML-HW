#Q1. Write a program to find the difference between the maximum and minimum elements in a list.

def diff(num_list):
    maxi = num_list[0]
    mini = num_list[0]
    for num in num_list:
        if num > maxi:
            maxi = num
        if num < mini:
            mini = num
    print(maxi - mini)
diff([1,2,3,4,100,8])                


# Q2. Write a program to remove all elements at odd indices from a list.

def my_list(lst):
    for i in range(len(lst)):
        if i % 2 != 0:
            print(i)
print(my_list([1,2,3,4,5,6]))

#Q3. Write a program that takes a list of integers and prints only the elements that appear exactly once.

count = {}
def count_ele(lst):
    for n in lst:
        count[n] = count.get(n,0)+1
        
    for num ,c in count.items():
        if c == 1:
            print(num)
count_ele([1,1,2,3,4,4,5,5,5,66,89,89,60])   

