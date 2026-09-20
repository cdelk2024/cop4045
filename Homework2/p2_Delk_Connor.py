# Connor Delk 
# Homework 2, Problem 2 

# This program uses list and dictionary comprehensions. 

# Part a 
# create tuples containing 4 distinct integers ranging from 1 to 10
# keeps only the tuples where a**2 + b**2 = c**2 + d**2 is true 
# each variable uses its own for statement to ensure they each have an 
# independent value between 1-10 
num_tuples = [(a, b, c, d) for a in range(1, 11) for b in range(1, 11) 
                 for c in range(1,11) for d in range(1,11)
                 if ( a != b and a != c and a != d 
                     and b != c and b != d and c != d
                     and a**2 + b**2 == c**2 + d**2 )]
# Displays all valid tuples 
print("Part a:") 
print(num_tuples) 

# Part b 
# Given list of strings 
given_strings = ["One", "SEVEN", "three", "two", "Ten"]
# for each word that is shorter than five characters, create a tuple which contains
# the lowercase version and its original length 
words = [(word.lower(), len(word)) 
         for word in given_strings
         if len(word) < 5 ]
# Display the lowercase words and their respective lengths 
print("Part b:") 
print(words) 


# Part c 
# Given strings with format: First Middle Last 
names = ["Christopher Ashton Kutcher", "Elizabeth Stamatina Fey"]
# use split() to separate each name into a list of three parts using their indexes
# index[0] = first name, index[1] = middle name, index[2] = last name 
# index [1][0] selects the first character of the middle name which would be the middle initial 
new_names = ["{} {}. {}".format(name.split()[0], name.split()[1][0], name.split()[2])
             for name in names]
# Displays the formatted full names as strings 
print("Part c:")
print(new_names) 

# Part d 
# lst1 and lst2 are given lists that may contain anagram pairs 
lst1 = ["Spam", "Trams", "Elbows", "Tops", "Astral"]

lst2 = ["Bowels", "Sample", "Altars", "Stop", "Course", "Smart"]
# compare every word from lst1 with every word from lst2 to find any pairs of anagrams
# use lower to make comparison case-insensitive and sorted() to create sorted list of the letters
# in each word
anagrams = [(word1, word2)
            for word1 in lst1
            for word2 in lst2 
            if sorted(word1.lower()) == sorted(word2.lower()) ]
# Display all pairs of anagrams 
print("Part d:")
print(anagrams) 

# Part e 
# given list of strings 
s = ['one', 'two', 'three'] 
# create a dictionary that maps each string to its length
# the dictionary key and value use the for statement and len() to get the word and length 
word_dict = {word: len(word)
             for word in s}
# Displays the words and their lengths 
print("Part e:")
print(word_dict) 

# Part f 
# Given string 
text = "Hello world" 
# range(len(text)) creates every valid character index 
# index i becomes the key and the character text[i] becomes the value
# lower() is used in comparison to ensure case insensitivity for finding vowels 
vowels = {i: text[i]
          for i in range(len(text))
          if text[i].lower() in "aeiou"}
# Displays each vowel index and their corresponding character 
print("Part f:")
print(vowels)
print()
print("Connor Delk") 