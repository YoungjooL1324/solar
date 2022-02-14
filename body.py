#Author: Youngjoo Lee
#Date: 02/11/2022
#Purpose: Body Class of Lab 2

from cs1lib import *

class Body:

    #Purpose: constructor used to initialize instance variables of Body class
    def __init__(self, mass, x, y, vx, vy, pixel_radius, r, g, b):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.pixel_radius = pixel_radius
        self.r = r
        self.g = g
        self.b = b

    #Purpose: method to draw the body
    def draw(self, cx, cy, pixels_per_meter):
        set_fill_color(self.r, self.g, self.b)
        set_stroke_color(self.r, self.g, self.b)

        bx = (self.x * pixels_per_meter) + cx #creates the position of planet based on parameter and instance variables
        by = (self.y * pixels_per_meter) + cy #multiply self.y by pixels_per_meter to convert from meters to pixels


        draw_circle(bx, by, self.pixel_radius) #draws the actual circle


    # Purpose: updates the velocity of the body object
    def update_velocity(self, ax, ay, timestep):

        self.vx = self.vx + ax * timestep
        self.vy = self.vy + ay * timestep

    #Purpose: updates the position of the body object with timestep
    def update_position(self, timestep):
        self.x = self.x + self.vx * timestep
        self.y = self.y + self.vy * timestep













