#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""
import math

def distance(p1,p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    dr = (dx**2 + dy**2)**(1/2)
    return dr

if __name__ == "__main__":
    d = distance( (2,4) , (6,3) )
    assert round(d,3) == 4.123
    d = distance( (-3,2.2) , (1,2))
    assert round(d,3) == 4.005


