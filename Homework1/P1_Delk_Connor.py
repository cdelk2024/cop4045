#Connor Delk 
#COP 4045 Homework 1 Problem 1 - Quadratic Equations 
#ax^2 +bx + c = 0
#This program solves quadratic equations and graphs their functions
#The loop runs infinitely until blank input is entered for variable a. 

#import math and matplotlib libraries 
import math 
import matplotlib.pyplot as plt 
#use while loop to run infinitely until empty string is detected for variable a 
while True: 
    a_str = input("Enter a: ")
    
    if a_str == "":
        break 
    #convert input from user into floats 
    a = float(a_str)
    b_str = input("Enter b: ")
    c_str = input("Enter c: ")
    b = float(b_str)
    c = float(c_str) 
    #use d variable to represent sqrt(b^2 - 4ac) 
    d = b**2 - (4*a*c) 
    #if else statements to determine if 0, 1, or 2 roots are found
    if d < 0: 
        #if d < 0 and no roots are found, graph is centered at vertex 
        x_center = -b/(2*a)
        x_min = x_center -2 
        x_max = x_center +2 
        print("no real solutions")
    elif d == 0: 
        #if d = 0 there is one solution
        x1 = -b/(2*a)
        #centers the domain around the root 
        x_min = x1 -2
        x_max = x1 +2 
        print ("one solution: ", x1)
    else: 
        #if d is positive, there are two roots
        #x1 and x2 calculate the root using quadratic formula and math library 
        x1 = (-b - math.sqrt(d))/(2*a) 
        x2 = (-b + math.sqrt(d))/(2*a)
        #use min and max in case order changes 
        #use -3 and +3 to ensure both roots are visible 
        x_min = min(x1, x2) -3 
        x_max = max(x1, x2) +3 
        print("two solutions: ", x1, x2)
        #150 points in domain which includes endpoints 
        space = (x_max - x_min)/149
        #empty lists for the x and y coordinates for the graph
        x_values = []
        y_values = []
        #use for loop to generate all 150 points on x and y axis's 
        for i in range(150):
            #start at x_min and increment by i spaces
            x = x_min + i *(space) 
            #given y function
            y = a*(x**2) + (b*x) + c
            #append x and y values to their lists 
            x_values.append(x)
            y_values.append(y) 
        #load full coordinate lists into matplotlib
        plt.plot(x_values,y_values)
        #displays the graph 
        plt.show() 