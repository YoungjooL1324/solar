#Author: Youngjoo Lee
#Date: 02/11/2022
#Purpose: System Class of Lab 2

from body import Body
from cs1lib import *
from math import sqrt

#CONSTANT:

G = 6.67384e-11 #universal gravitational constant

class System:

    #Purpose: Constructor class that creates body_list instance variable that will store body objects
    def __init__(self, body_list):
        self.body_list = body_list

    #Purpose: calls draw on each body in the body_list
    def draw(self, cx, cy, pixels_per_meter):
        for planet in self.body_list:
            planet.draw(cx, cy, pixels_per_meter)

    #Purpose: calls compute_acceleration on every body in body_list and updates their respective velocities and positions
    def update(self, timestep):
        for i in range(len(self.body_list)):

            (ax, ay) = self.compute_acceleration(i) #create (ax, ay) tuple

            self.body_list[i].update_velocity(ax, ay, timestep) #update velocity of body object

            self.body_list[i].update_position(timestep) #update position of body object


    #computes the acceleration of a body object
    def compute_acceleration(self, n):
        totalAX = 0
        totalAY = 0
        current_planet = self.body_list[n]

        for i in range(len(self.body_list)):
            if i != n: #makes sure not to calculate force of object on itself
                dx = self.body_list[i].x - current_planet.x
                dy = self.body_list[i].y - current_planet.y

                r = sqrt((dx ** 2) + (dy ** 2)) #straight-line distance using distance formula

                a = G * (self.body_list[i].mass / (r**2)) #acceleration magnitude

                ax = a * dx / r #acceleration x component
                ay = a * dy / r #acceleartion y componenet

                totalAX += ax #add acceleration componenets of each body to the total AX that will be applied
                totalAY += ay #same as x

        return (totalAX, totalAY)

