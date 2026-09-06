#Connor Delk 
#COP 4045 Problem 3 Duplicated Substrings 

#This program is used to find a substring of a requested length that 
#appears at least twice in a string. 

#function to return the first occurring duplicated substring of length n 
def find_dup_str(s, n):
    #used to save the total number of characters in the string 
    length = len(s)
    #substring of length n cannot start after this index 
    last_index = length - n 
    #for looop to examine any possible substrings in given string 
    for i in range(0, last_index +1):
        #uses string slicing to select n characters which begins at i
        first_string = s[i:i + n] 
        #comparison begins at position after i
        j = i + 1 
        #compares first_string with every later substring with a length of n 
        while j <= last_index:
            #uses same string slicing as previous oop to select another substring 
            second_string = s[j:j +n] 
            #if first_string has a duplicate, return immediately 
            if first_string == second_string:
                return first_string 
            #moves the second substring one character to the right 
            j = j + 1 
     #returns "" if no duplicated substring is found        
    return "" 

#function to to return the longest duplicated substring that is found in s 
def find_max_dup(s): 
    length = len(s) 
    #longest is empty and will return empty unless a duplicate is found 
    longest = "" 
    #for loop that tests every substring length in increasing order 
    for n in range(1, length): 
        #calls first function to find the first duplicate of current length 
        current = find_dup_str(s, n) 
        #if current does not equal empty, current replaces previous longest 
        if current != "":
            longest = current 
     #returns the longest duplicate found        
    return longest 

#prompts user to enter a string 
string = input("Enter a string: ") 
#prompts user to enter length of substring 
n_string = input("Enter the substring length: ") 
#converts string to integer
n = int(n_string) 
#calls first function using user inputted string and substring length 
dupe = find_dup_str(string, n)
#prints the first duplicated substring 
print(dupe) 
#prompts user again for another string and stores in s 
s = input("Enter another string: ")
#calls second function to find the longest duplicated substring 
longest_dupe = find_max_dup(s)
#prints the longest duplicated substring 
print(longest_dupe) 