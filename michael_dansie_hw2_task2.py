"""
Michael Dansie
Feb-4-2019
PHYS 2300
Assignment 2 Task 2
Projectile Motion Plotter
"""

import numpy as np
import math as m
import matplotlib.pyplot as plt

# Function to calculate projectile motion
def position(x,v,t,a):
    """
    This calculates the x or y position of a projectile at a given time
    Param:x=>initial position
          v=>initial velocity
          t=>given time
          a=>acceleration(usually gravity)
    Return:position at given time
    """
    return x + v*t + 0.5*a*t**2 # pos = initial position + velocity*time + .5(acceleration)(time squared)

# Function to plot data
def plot_motion(x, y):
    """
    This plots the motion of an object
    Param:x=>x axis position(can be a collection)
          y=>y axis position(can be a collection)
    Return:none
    """
    plt.xlabel("X Position (m)")
    plt.ylabel("Y Position (m)")
    plt.plot(x, y)
    plt.show()
     
# "Main" Function
def main():
    """
    Receives user input for x and y position and velocity
    Calculates the motion of the projectile and plots it
    """
    
    def get_x_input():
        """
        This gets the initial x position and velocity values
        Param:none
        Return:Tuple with x pos and vel
        """
            # Ask for and validate user input for x pos and vel
        while True:
            try:
                posx = float(input("Please enter the initial x position in m: "))
            except ValueError:
                print("Invalid Input")
                continue
            else:
                break

        while True:
            try:
                velx = float(input("Please enter the initial x velocity in m/s: "))
            except ValueError:
                print("Invalid Input")
                continue
            else:
                break
            
        #return tuple
        xinput = (posx, velx)
        return xinput

    def get_y_input():
        """
        This gets the initial y position and velocity values
        Param:none
        Return:Tuple with y pos and vel
        """  
        # Ask for and validate user input for y pos and vel
        while True:
            try:
                posy = float(input("Please enter the initial y position in m: "))

                #start at ground
                if posy < 0:
                    print("Please enter a positive value.")
                    continue

            except ValueError:
                print("Invalid input")
                continue
            else:
                break

        while True:
            try:
                vely = float(input("Please enter the initial y velocity in m/s: "))
            except ValueError:
                print("Invalid Input")
                continue
            else:
                break
            
        # Return tuple
        yinput = (posy, vely)
        return yinput

    #Inital position and velocity of user input x and y
    posx0, velx0 = get_x_input()
    posy0, vely0 = get_y_input()
    
    #acceleration y acceleration is gravity
    accelx = 0.0
    GRAVITY = -9.8           
    
    #Initial time of 0s, time intervals of .01 s
    deltat = .01
    t = 0.0
    
    #lists of all x and y positions in the motion 
    x = [posx0]
    y = [posy0]
    
    #limit of time intervals to calculate
    intervals = 4000

    for i in range(0, intervals):
        #increment time, add xy positions at that time
        t = t + deltat
        x.append(position(posx0, velx0, t, accelx))
        y.append(position(posy0, vely0, t, GRAVITY))
        
        #if the projectile has hit the ground, break
        if y[i+1] <= 0:
            break

    plot_motion(x, y)
 
if __name__ == "__main__":
    main()
    exit(0)