#Connor Delk
#COP 4045 Problem 2 Pythagorean Numbers 
#a^2 + b^2 = c^2 

#This program finds every unique set of triples whose values are positive
# and <= a number n inputted by the user 

#funciton used to find and return all triples up to a value n
def find_Pythagorean(n) : 
    triple_set = []#initialize an emtpy set to find triples successfully found 
    #use three nested for loops to inerate through every value between
    #1 and n, including n 
    for a in range(1,n+1): 
        for b in range(1, n+1):
            for c in range(1, n+1):
                #if statement ensure no duplicates are added and that the 
                #values for a b c satisfy the equation
                if a < b < c and (a**2 + b**2) == c**2:
                    #appends any successful triples to the empty set 
                    triple_set.append((a,b,c))
        
    #returns the set of successfull triples 
    return triple_set   
#prompts the user to input a positive integer and stores in n_string
n_string = input("Enter a positibe integer: ")
#converts the value from a string to an integer
n = int(n_string) 
#calls the function find_Pythagorean and saves the list it returnes
triple_set_success = find_Pythagorean(n)
#displays every succesfull triple that was found 
print(triple_set_success)