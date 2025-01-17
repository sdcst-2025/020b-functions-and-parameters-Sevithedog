#!python3
"""
NOTE:
If you complete this extension, call your teacher over to have it assessed


Create a program to determine the solutions for a quadratic equation
in the format ax^2 + bx + c = 0
A key is the discriminant: b^2 - 4 * a * c
If the discriminant is negative, there are no solutions
If the discriminant is zero, there is only 1 solution
If the discriminant is positive, there are 2 solutions

If the discriminant is a perfect square, then the equation can
be factored

If the discriminant is non zero, the solutions are:
x = (-b + sqrt(b^2 - 4 * a * c)) / 2a
x = (-b - sqrt(b^2 - 4 * a * c)) / 2a

Assignment criteria:
Create a program that inputs 3 float values: a, b, c
function numSolutions(a,b,c) returns an integer with the number of solutions
function solutions(a,b,c) returns a tuple with the solutions (note that if 1 solution,
then both solutions will be the same)

If there are no solutions:
output is: "There are no real solutions"

If there is one solution:
output is "There is 1 solution, x=??"

If there are two solutions:
output is: "The solutions are x=?? and x=??"
"""

def numSolutions(a,b,c):
    if b**2 - 4 * a * c < 0:
        nsol = 0
    elif b**2 - 4 * a * c == 0:
        nsol = 1
    elif b**2 - 4 * a * c == 2:
        nsol = 2
    return nsol

def solutions(a,b,c,nsol):
    import math
    if nsol == 1:
        x1 = (-b + (b**2 - 4 * a * c)**(1/2)) / (2*a)
        x2 = (-b - (b**2 - 4 * a * c)**(1/2)) / (2*a)
    l = (x1,x2)
    return l

def title():
    # inputs none
    # return str of All the title and instructions on one line
    t = "Use this program to solve quadractics." "Enter the quadratic in the form ax^2 + bx + c"
    return t


def main():
    # Display Title and Instructions
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    n = numSolutions(a,b,c)
    if n == 0:
        print("There is no solution.") 
        exit()
    awnswer = solutions(a,b,c,n)
    print(awnswer)



    print( title() )
    # Your code and function calls should go here



main()