#requirements.txt = pip3 install sympy
# Importing the libraries that are needed for the program to run.
import sympy as sp
import math as m
import scipy as sp
import numpy as np
import cmath
import matplotlib.pyplot as plt
from functools import reduce
###GLOBAL VARIABLES
ω = 40000
c_o = 343
# k = ω/c_o
k = 116
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
class target_points:
    def __init__(self,x,y,z) -> None:
        self.x = x
        self.y = y
        self.z = z
class d_j:
    def __init__(self,x,y,z) -> None:
        self.x = x
        self.y = y
        self.z = z

# https://stackoverflow.com/questions/70819390/put-2d-coordinate-axis-at-the-center-of-an-array-in-python
# https://stackoverflow.com/questions/70012889/what-is-a-faster-way-to-get-the-center-points-of-objects-represented-in-a-2d-n


φ_j_array = np.zeros(shape=(16,16), dtype=np.uint8)
#PHASES FOR EACH TRANSDUCER, right now the phase is 0,
#UNUSED

def generate_t_j_array():
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
    length = 16

    for x in range(0,length):
        for j in range(0,length):
            a = t_j(x,j,0)
            objs.append(a)
    return (tuple(vars(a) for a in objs))
#make the origin 0,0
arr_t_j = generate_t_j_array()
#this is the array of transducers
# len -> 256

"""
change documnetation
"""
def generate_target_points_array():
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
    #TODO change length to 16
    length = 16
    # for x in range(0,8):
        # print(8-x)
    for x in range(0,length):
        for j in range(0,length):
            a = target_points(x,j,0.5)
            #points(x,i,0)- > start from origin (8,8)
            objs.append(a)
    #print(tuple(vars(a) for a in objs))
    #16 by 16
    return (tuple(vars(a) for a in objs))
target_points = generate_target_points_array()
#len -> 256
#
#TODO
#TODO target points only has one so far
#TODO -> change it to array of length 256 for loop
#TODO ##

#TODO -> HAS TO DO WITH TARGET POINT
def generate_d_j_array(index):
    objs = list()
    for j in range(len(arr_t_j)):
        #TODO change target_points[0] to target_points[i]
        a = \
            ((target_points[index].get('x') - arr_t_j[index].get('x'))**2  + (target_points[index].get('y') - arr_t_j[index].get('y'))**2  + (target_points[index].get('z') - arr_t_j[index].get('z'))**2)**0.5
        objs.append(a)
    return objs

# array_d_j= generate_d_j_array()
#len - > 256

#TODO -> HAS TO DO WITH TARGET POINT
def generate_e_j_array(index):
    objs = list()
    for j in range(len(arr_t_j)):
        #TODO CHANGE target_points[0] to target_points[index]
        a = d_j(target_points[index].get('x') - arr_t_j[j].get('x'),target_points[index].get('y') - arr_t_j[j].get('y'),target_points[index].get('z') - arr_t_j[j].get('z'))
        objs.append(a)
    return (tuple(vars(a) for a in objs))


# arr_e_j= generate_e_j_array()
#len -> 256


def generate_sinj_array(arr_e_j):
    """
    helper for Mj array
    """
    objs  = list()
    for j in range(len(arr_e_j)):
        a = ((arr_e_j[j].get('x') ** 2 + arr_e_j[j].get('y') ** 2)/(arr_e_j[j].get('x') ** 2 + arr_e_j[j].get('y') ** 2+ arr_e_j[j].get('z') ** 2)) ** 0.5
        objs.append(a)
    return objs
# arr_sinj= generate_sinj_array()

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

def generate_Mj_array(arr_sinj,array_d_j):
    objs = list()
    for j in range(len(arr_sinj)):
        c = cmath.exp(i*k*array_d_j[j])
        a = (p_0 * j_0(0,k*r*arr_sinj[j]) * c)/(array_d_j[j])
        objs.append(a)
    return objs

# arr_Mj = generate_Mj_array()
# print(f"Mj: {arr_Mj}")
# print(len(arr_Mj))
# print("\n")

def generate_pj_array(arr_Mj):
    objs = []
    for j in range(256):
        # c = φ_j_array[j]
        a = cmath.exp(i*0) * arr_Mj[j]
        # print(a)
        objs.append(a)
    return objs
def addComplex(a,b):
    return a + b

# arr_p_j = generate_pj_array()
#this is for one target point


def sum_of_pj_array():
    """
    sums the pj_array for one target point"""
    objs = []
    for j in range(256):
        index = j
        array_d_j = generate_d_j_array(index)
        arr_e_j = generate_e_j_array(index)
        arr_sinj = generate_sinj_array(arr_e_j)
        arr_Mj = generate_Mj_array(arr_sinj,array_d_j)
        arr_p_j = generate_pj_array(arr_Mj)
        a = abs(reduce(addComplex,arr_p_j))
        print(f"a is {a}")
        objs.append(a)
    return objs

sum = sum_of_pj_array()
x_axis = np.arange(0,17)
plt.plot(sum)
plt.xlim(0,16)
plt.ylabel("sum of the forces on target points")
plt.grid(True)
plt.show()
#each element of `sum` array would correspond to the same element of the target_points array
#for example the sum of the forces of index[0] would be for the target_point 0, which
#is {'x': 0, 'y': 0, 'z': 0.5}

# print(f"sum of the total pressure (right now is one): {abs(reduce(addComplex,arr_p_j))}")



###TEMP_theta_j###
a = t_j(2,2,1)
###TEMP_theta_j###






#TODO
#change the graph to a grid
#plot the graph of ALL the sum of total pressures to a point in a grid
#max pressure is red
#ranges from low to high
#lowest pressureis blue

#change x,y,z to distance of theta_j from x,y,z of a point
#make 0 start from 'center'
#sum of all p_j
#change notation of θ_j to t_j

# print(p_j(a))
# if __name__ == "__main__":
#     sol = Solution()
#     sol.main(5)
