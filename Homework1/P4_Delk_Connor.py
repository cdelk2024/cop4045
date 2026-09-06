#Connor Delk
#COP 4045 Homework 1 Problem 4 Function visualization 

#This program reads an expression, domain, and number of sample points from 
#the user and calculates x-values, evaluates the expression for those values
#prints a table of final results and graphs the function using matplotlib


#import math and matplotlib modules 
import math 
import matplotlib.pyplot as plt 

#function used to print and graph a mathematical expression 
def plot_function(fun_str, domain, ns): 
    #x_min is first item in the domain and x_max is second item 
    x_min = domain[0]
    x_max = domain[1]  
    #ns sample points have ns -1 spaces between them 
    num_of_spaces = ns -1
    #calculates distance between x values 
    space = (x_max - x_min) / (num_of_spaces) 
    #empty list to hold x values 
    xs = []
    #for loop that generates ns amount of x values 
    for i in range(ns):
        #begins at x_min and finishes when x = x_max
        x = x_min + space * i 
        #appends the xvalue to the end of list 
        xs.append(x)   
    #empty list for y values 
    ys = [] 
    #for loop that iterates through each x value from above 
    for x in xs: 
        #evaluates expression entered by user
        y = eval(fun_str) 
        #appends y value in the empty list at same position as corresponding x 
        ys.append(y)  
        
    #prints heading for the two table columns 
    print("{:^12s}{:^12s}".format("x", "y")) 
    #uses for loop to print one table row for each corresponding x and y 
    for i in range (ns): 
        print("{:+12.4f}{:+12.4f}".format(xs[i], ys[i]))  
        
    #uses matplotlib to plot the calculates x and y values
    #label both axes, use entered expression as graph title
    #and display the completed graph 
    plt.plot(xs, ys)
    plt.xlabel("x") 
    plt.ylabel("y") 
    plt.title(fun_str) 
    plt.show() 
    
#prompts user to enter mathematical function
fun_str = input("Enter function with variable x: ")
#prompt user to enter number of samples and convert string to integer
ns_string = input("Enter number of samples: ")
ns = int(ns_string) 
#prompt user to enter xmin and xmax values and convert both to floats 
x_min_string = input("Enter xmin: ") 
x_min = float(x_min_string) 
x_max_string = input("Enter xmax: ")
x_max = float(x_max_string) 
#combine both domain boundaries into tuple and call plot_function with
#expression, domain, and sample as arguments 
domain = (x_min, x_max) 
plot_function(fun_str, domain, ns)