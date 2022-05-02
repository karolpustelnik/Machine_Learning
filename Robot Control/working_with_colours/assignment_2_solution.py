import pybullet as p
p.connect(p.GUI)
from assignment_2_lib import take_a_photo, drive
import cv2
import numpy as np
import random
#TODO: add imports and functions
from assignment_2_lib import *
car = build_world_with_car()

s = p.createVisualShape(shapeType=p.GEOM_CYLINDER,
  visualFramePosition=[-2,-1,0], rgbaColor=[0, 0, 1, 1],
  radius=0.1, length=10)
p.createMultiBody(baseVisualShapeIndex=s)
s = p.createVisualShape(shapeType=p.GEOM_CYLINDER,
  visualFramePosition=[-2,1,0], rgbaColor=[0, 0, 1, 1],
  radius=0.1, length=10)
p.createMultiBody(baseVisualShapeIndex=s)
pos1 = [1.9560342718892494, 0, 1]
p.loadURDF("sphere2red.urdf", pos1, globalScaling = 0.4)
for _ in range(200):
    p.stepSimulation()

####### MY FUNCTIONS ########

def mask_image(image):
    image = image[0:525, :, :]
    image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
# positive red hue margin
    lower1 = np.array([0, 100, 50])
    upper1 = np.array([10, 255, 255])
    mask1 = cv2.inRange(image, lower1, upper1)
#negative red hue margin
    lower2 = np.array([160,100,50])
    upper2 = np.array([179,255,255])
    mask2 = cv2.inRange(image, lower2, upper2)
    mask = mask1 + mask2
    return mask
#####


def ball_width(image):
# image crop
  mask = mask_image(image)
  X = np.sum(mask, axis = 1)
  x = min(np.where(X == X[X>0][0])[0])
  y = max(np.where(X == X[X>0][-1])[0])
  ball_width = y-x
  return ball_width



### TASK 1
def forward_distance(image):
# image crop
  mask = mask_image(image)
  X = np.sum(mask, axis = 1)
  x = min(np.where(X == X[X>0][0])[0])
  y = max(np.where(X == X[X>0][-1])[0])
  ball_width = y-x
  steps = (10*(300/ball_width) - 8)*250
  print(steps)
  steps = round(steps)
  return steps

###END OF TASK 1

  

# TASK 2

def find_a_ball(car):
  image = take_a_photo(car)
  mask = mask_image(image)
  X = np.sum(mask, axis = 0)
  if any(X)>0:
    center_x = np.argmax(X)
  else:
    center_x = 0
  while abs(center_x - 315)>159:  #keep turning until you find the center of the ball
    drive(car, True, -1)
    drive(car, False, 1)
    image = take_a_photo(car)
    mask = mask_image(image)
    X = np.sum(mask, axis = 0)
    if any(X)>0:
      center_x = np.argmax(X)
    else:
      center_x = 0
    print(center_x)
  diameter = ball_width(image)
  print(diameter)
  steps = (10*(300/diameter) - 8)  #determine number of steps
  dist = round(steps)
  for i in range (dist):
    drive(car, True, 0)

### END OF TASK 2



### TASK 3
def move_a_ball(car):
  for i in range(12):
      drive(car, False, 0)
  image = take_a_photo(car)
  mask = mask_image(image)
  X = np.sum(mask, axis = 0)
  center_x = np.argmax(X)
  print('srodek kulki', center_x)
  dist = round(forward_distance(image)/250)
  additional_steps = 0 # determine additional steps depending on horizontal position of ball
  if center_x > 16:
    additional_steps = 1
  if dist > 21:
    additional_steps = 2
  if dist > 20 and (center_x < 110 or center_x > 530):
    additional_steps = 3
  if dist > 22 and (center_x < 110 or center_x > 530):
    additional_steps = 4
  print('dist wynosi', dist)
  print(additional_steps)
  p = 0
  additional_accuracy = 0
  if center_x < 315:
    k = 1
  else:
    k = -1
  if (center_x > -1) and (center_x < 270): # how far is the ball from the center at the begining
    p = 1
  if (center_x > 360 and center_x < 640): # how far is the ball from the center at the begining
    p = -1
  print(p)
  if p == 1 or p == -1: # if it is far, use the route below
    for i in range(dist+13):
      drive(car, True, 0)
    for i in range(7):
      drive(car, True, k)
      drive(car, False, -k)
    for i in range(round((abs(center_x-315)/33))+additional_steps):   #expression in parenthasis is used to determine horizontal posistion
      drive(car, True, 0)
    for i in range(7):
      drive(car, True, k)
      drive(car, False, -k)
  elif ((center_x <= 360) and (center_x >= 315)) or ((center_x >= 270) and (center_x <= 315)): # if the ball is close to center, use this route
    additional_accuracy = 1
    for i in range(3):
      drive(car, True, -k)
    for i in range(dist+3):
      drive(car, True, 0)
    for i in range(17):
      drive(car, True, k)
    for i in range(7):
      drive(car, True, k)
      drive(car, False, -k)

  image = take_a_photo(car)
  mask = mask_image(image)
  X = np.sum(mask, axis = 0)
  center_x = np.argmax(X)
  if additional_accuracy == 1:
    drive(car, False, 0)
    drive(car, False, 0)
    if center_x < 270:
      drive(car, True, 1)
    if center_x > 355:
      drive(car, True, -1)
    drive(car, True, 0)
    drive(car, True, 0)
  drive(car, True, 0)
  print('liczba steps', dist)
  for i in range(dist+19):
    image = take_a_photo(car)
    mask = mask_image(image)
    X = np.sum(mask, axis = 0)
    center_x = np.argmax(X)
    if center_x < 220:   #correct the route if the ball is escaping
      drive(car, False, -1)
      drive(car, True, 1)

    if center_x > 410:  #correct the route if the ball is escaping
      drive(car, False, 1)
      drive(car, True, -1)
    drive(car, True, 0)
    print(center_x)

### END OF TASK 3

move_a_ball(car)





