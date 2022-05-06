from time import sleep
import pygame
pygame.init()

#init joystick
j = pygame.joystick.Joystick(0)
j.init()

#get controller info
print("name: ", j.get_name())
print("no. of axes: ",j.get_numaxes())
print("no. of buttons: ",j.get_numbuttons())
print("no. of hats: ",j.get_numhats())

while True:
    pygame.event.get()
    if j.get_axis(0) != 0.0 or j.get_axis(1) != 0.0:
        sleep(.5)
        print("left  x",j.get_axis(0),"| y",j.get_axis(1))
    elif j.get_axis(3) != 0.0 or j.get_axis(4) != 0.0:
        sleep(.5)
        print("right x",j.get_axis(3),"| y",j.get_axis(4))
    elif j.get_axis(2) > -1.0 and j.get_axis(2) != 0.0:
        sleep(.5)
        print("L TRIGGER ", j.get_axis(2))
    elif j.get_axis(5) > -1.0 and j.get_axis(5) != 0.0:
        sleep(.5)
        print("R TRIGGER ", j.get_axis(5))
