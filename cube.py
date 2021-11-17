#Program name: cube.py
#this program prints out the cube of odd numbers from 0 to 19 or
#   the numbers themselves if they are even
#made by Joshua Gillespie 11/16/2021


#making function cb for cubing 
def cr(x):
    v=x*x*x
    return v


#range of numbers from 0 to 19
for i in range (20):
    print "the value of x is:"#printing value of i
    print i
    if i % 2 == 0: continue#checking if the value of i is odd. if it is it calculates cubed value
    print "the cubed value of x is odd! the value is:"
    print cr(i)
    print


