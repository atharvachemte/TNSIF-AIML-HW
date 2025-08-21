#Q1. Write a function to check whether a given string is a pangram (contains all letters of the alphabet).

def is_pangram(sentence):
    if chr in sentence == "abcdefghijklmnopqrstuvwxyz":
        print("is pangram")
    else:
        print("is not pangram")
is_pangram("The quick brown fox jumps over the lazy dog.")

#Q2. Write a function that takes a sentence and returns the word with the maximum length.
def max_word(sentence):
    words = sentence.split()
    maximum = ""
    for word in words:
        if len(word) > len(maximum):
            maximum = word
    return maximum    
print(max_word("Atharva got 10 SGPA in sem6"))

#Q3. Write a function to count the number of uppercase and lowercase characters in a string.

def count_case(word):
    upper_count = 0
    lower_count = 0
    for ch in word:
        if ch == ch.upper():
            upper_count += 1
        if ch == ch.lower():
            lower_count += 1
    print(upper_count)            
    print(lower_count)
count_case("AtHarvA")                
