#Author: Youngjoo Lee
#Date: 02/11/2022
#Purpose: solar system of Lab 2

from cs1lib import *
from system import System
from body import Body

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 100000  * 50        # real seconds per simulation second
PIXELS_PER_METER = 7 / 1e10  # distance scale for the simulation

FRAMERATE = 30              # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame

#Mass
SUN_MASS = 1.98892e30
MERCURY_MASS = 0.330e24
VENUS_MASS = 4.87e24
EARTH_MASS = 5.9736e24
MARS_MASS = 0.642e24

#Radius
SUN_PIXEL_RADIUS = 15
MERCURY_PIXEL_RADIUS = 3
VENUS_PIXEL_RADIUS = 6
EARTH_PIXEL_RADIUS = 7
MARS_PIXEL_RADIUS = 4

#Position
SUN_X = 0
SUN_Y = 0
MERCURY_X = 57.9e9
MERCURY_Y = 0
VENUS_X = 108.2e9
VENUS_Y = 0
EARTH_X = 149.6e9
EARTH_Y = 0
MARS_X = 228.0e9
MARS_Y = 0

#Velocities
SUN_VX = 0
SUN_VY = 0
MERCURY_VX = 0
MERCURY_VY = 47890
VENUS_VX = 0
VENUS_VY = 35040
EARTH_VX = 0
EARTH_VY = 29790
MARS_VX = 0
MARS_VY = 24100

#Purpose: Sets the black background, and clears frame each frame change
def background():
    set_clear_color(0, 0, 0)  # black background

    clear()

#Purpose: function to be passed into start_graphics
def main():

    background()

    #Draws solar system for each frame
    solarSystem.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    solarSystem.update(TIMESTEP * TIME_SCALE)


#Create and reference the body object
sun = Body(SUN_MASS, SUN_X, SUN_Y, SUN_VX, SUN_VY, SUN_PIXEL_RADIUS, 1, 1, 0)# yellow sun
mercury = Body(MERCURY_MASS, MERCURY_X, MERCURY_Y, MERCURY_VX, MERCURY_VY, MERCURY_PIXEL_RADIUS, 1, .4, 0)# orange mercury
venus = Body(VENUS_MASS, VENUS_X, VENUS_Y, VENUS_VX, VENUS_VY, EARTH_PIXEL_RADIUS, 0, .6, .2)# green venus
earth = Body(EARTH_MASS, EARTH_X, EARTH_Y, EARTH_VX, EARTH_VY, EARTH_PIXEL_RADIUS, 0, 0, 1)#blue earth
mars = Body(MARS_MASS, MARS_X, MARS_Y, MARS_VX, MARS_VY, MARS_PIXEL_RADIUS, 1, 0, 0)#red mars

#Create and reference system object with body object list as parameter
solarSystem = System([sun, mercury, venus, earth, mars])


start_graphics(main, 2400, framerate=FRAMERATE)

