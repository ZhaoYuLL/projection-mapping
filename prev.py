#requirements.txt = pip3 install sympy
# Importing the libraries that are needed for the program to run.
import sympy as sp
import math as m
import scipy as sp
import numpy
###GLOBAL VARIABLES
ω = 40000
c_o = 343
k = ω/c_o
θ = 5

p_0 = 1
# j_0 = 2
#d_j = DJ(x,y,z)

φ_j = 2 #an int FOR NOW
i = complex(0+1j)
r = 0.5
###

#class Solution(object):
# > The class t_j is a class that has three attributes, x, y, and z, and one method, r
class t_j:
    def __init__(self,x,y,z) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.r = r
        self.φ_j = φ_j

def generate_2d_array():
    """
    It takes the values of x and i and returns a list of objects with the values of x, i, and the value
    of the function t_j(x,i,1)
    :return: A tuple of tuples.
    """
    objs = list()
    ###
    """
    for x in range(length)
        loop from the start of the x to the middle length of x
            loop from the start of the y to the middle of length y
            assign as 

    """
    length = 18
    for x in range(0,8):
        print(8-x)
    for x in range(0,length):
        for i in range(0,length):
            a = t_j(x,i,0)
            #points(x,i,0)- > start from origin (8,8)
            objs.append(a)
    #print(tuple(vars(a) for a in objs))
    #16 by 16
    return (tuple(vars(a) for a in objs))
#make the origin 0,0
arr = generate_2d_array()
print(arr)
print(arr[2])
print("\n")
###gets the object of the desired attributes
for i in range(len(arr)):
    if arr[i].get('x') == 0 and arr[i].get('y') == 0:
        print(arr[i])

"""
print(len(a))
print(a[255])
print(a[4].get('y'))
print(a)"""
#print(generate_2d_array())

# print(tuple(vars(a) for a in objs))
# print(tuple(a.y for a in objs))
# print(tuple(a.z for a in objs))
# print(tuple(a.r for a in objs))


# inf = float('inf')
# c = t_j(3,3,4)
# A = [[c.x,c.r,4,inf,3],
#     [1,0,2,inf,4],
#     [4,2,0,1,5],
#     [inf,inf,1,0,3],
#     [3,4,5,3,0]]

# #4 -> spacing between blocks
#print('\n'.join([''.join(['{:4}'.format(item) for item in a])]))




# def me23(j):
#     return 1 

def sin(t_j):
    """
    > The function `sin(t_j)` takes a vector `t_j` and returns the square root of the ratio of the sum
    of the squares of the x and y components of `t_j` to the sum of the squares of the x, y, and z
    components of `t_j`
    
    :param t_j: the angle between the vector and the z-axis
    :return: The square root of the ratio of the sum of the squares of the x and y components of the
    vector to the sum of the squares of the x, y, and z components of the vector.
    """
    #point.x - theta_j.x ->gives distance
    sqrt = ((t_j.x ** 2 + t_j.y ** 2)/(t_j.x ** 2 + t_j.y ** 2+ t_j.z ** 2)) ** 0.5
    # √ ((x^2+y^2) / (x^2+y^2+z^2)) w.r.t t_j
    return(sqrt)



def j_0(order,argument):
    """
    This function takes in an order and an argument and returns the bessel curve using the parameters.
    
    :param order: the order of the bessel function
    :param argument: the x-axis of the curve
    :return: A float
    """
    p_j = sp.special.jv(order,argument) #returns a float
    return p_j
#j_0(0,x)

###TEMP_theta_j###
a = t_j(3,4,5)
###TEMP_theta_j###

def M(t_j,θ_j):
    """
    > The function `M` takes a vector `t_j` and returns the complex amplitude of the field at the origin
    due to a point source at `t_j`
    
    :param t_j: the direction of the point source
    :return: The function M(t_j) is being returned.
    """
    arg = k * r *sin(t_j)
    j_not = j_0(0, arg)
    # d_j = (t_j.x ** 2 + t_j.y ** 2 + t_j.z ** 2) ** 0.5
    d_j = (t_j.x - θ_j.x) +(t_j.y - θ_j.y) + (t_j.z - θ_j.z)
    constants = (1/d_j) * m.e**(i*k*d_j)
    return p_0*j_not* constants
#p(j)


def p_j(t_j,θ_j):
    """
    > The function `p_j` takes in a value for `t_j` and returns the value of the complex number `p_j`
    for that value of `t_j`
    
    :param t_j: the angle of the jth particle
    :return: The output is a matrix of the form:
    """
    sum = 0 + 0j
    for i in range(18):
        t_j = arr[i]
        output = m.e**(i*φ_j) * M(t_j,θ_j)
    output = m.e**(i*φ_j) * M(t_j,θ_j)
    return output
#TODO
#change x,y,z to distance of theta_j from x,y,z of a point
#make 0 start from 'center'
#sum of all p_j
#change notation of θ_j to t_j

# print(p_j(a))
# if __name__ == "__main__":
#     sol = Solution()
#     sol.main(5)
