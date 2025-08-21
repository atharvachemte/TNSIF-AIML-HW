# Q1. Write a program to take two lists from the user and print the common elements using sets.
new = []
def is_set(list1, list2):
    list1 = set(list1)
    list2 = set(list2)
    for n in list1, list2:
        new = list1.intersection(list2)
    print(new)
is_set([1,2,3,10,14,50],[2,50,10,14,9,8])        

# Q2. Write a program to check if two sets are disjoint or not.
def is_disjoint(set1, set2):
    if set1.isdisjoint(set2):
        print("It is Disjoint")
    else:
        print("It isn't Disjoint") 

is_disjoint({1, 2, 3, 5},{10, 20, 40})

# Q3. Write a program to find all unique vowels present in a given string using set.

def vowels(my_str):
    new = []
    for chr in my_str:
        if chr in "aeiou":
            new += chr
    print(new)
vowels("he is a good boy")