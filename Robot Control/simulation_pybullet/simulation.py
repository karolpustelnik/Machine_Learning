#!/usr/bin/env python3

import pybullet as p
import pybullet_data
import time
import numpy as np
import random
# start the simulation with a GUI (p.DIRECT is without GUI)
p.connect(p.GUI)

# we can load plane and cube from pybullet_data
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# load a plane
p.loadURDF("plane.urdf", [0, 0, -0.1], useFixedBase=True)

#setup gravity (without it there is no gravity at all)
p.setGravity(0,0,-10)

# load our robot definition
robot = p.loadURDF("robot.urdf")
# load a cube
cube_1 = p.loadURDF("cube.urdf", [random.uniform(0,0.9), random.uniform(0,0.9), 0], globalScaling = 0.05)
p.changeVisualShape(cube_1, -1, rgbaColor=[1,0.5,0.7,1])
cube_2 = p.loadURDF("cube.urdf", [-random.uniform(0,0.9), random.uniform(0,0.9), 0], globalScaling = 0.05)
p.changeVisualShape(cube_2, -1, rgbaColor=[1,0.5,0.7,1])
cube_3 = p.loadURDF("cube.urdf", [random.uniform(0,0.9), -random.uniform(0,0.9), 0], globalScaling = 0.05)
p.changeVisualShape(cube_3, -1, rgbaColor=[1,0.5,0.7,1])
cube_4 = p.loadURDF("cube.urdf", [-random.uniform(0,0.9), -random.uniform(0,0.9), 0], globalScaling = 0.05)
p.changeVisualShape(cube_4, -1, rgbaColor=[1,0.5,0.7,1])
cubs=[cube_1,cube_2,cube_3,cube_4]
base1=p.getBasePositionAndOrientation(cube_1)
base2=p.getBasePositionAndOrientation(cube_2)
base3=p.getBasePositionAndOrientation(cube_3)
base4=p.getBasePositionAndOrientation(cube_4)
print(base1[0][1])
# display info about robot joints
numJoints = p.getNumJoints(robot)


# add four sliders to GUI
p0_id = p.addUserDebugParameter("z", -0.1, 0, 0)
p1_id = p.addUserDebugParameter("y", -1, 1, 0)
p2_id = p.addUserDebugParameter("x", -1, 1, 0)
p3_id = p.addUserDebugParameter("pos", 0.0, 6.28, 0)
p.stepSimulation()
time.sleep(0.01)

for i in range(4):
  p.stepSimulation()
  time.sleep(0.01)
  x = p.getBasePositionAndOrientation(cubs[i])[0][0]  
  y = p.getBasePositionAndOrientation(cubs[i])[0][1]
  p.setJointMotorControl2(robot, 0, p.POSITION_CONTROL, targetPosition=0.05, maxVelocity=20)
  for _ in range(10):
    p.stepSimulation()
    time.sleep(0.01)
  p.setJointMotorControl2(robot, 2, p.POSITION_CONTROL, targetPosition=p.getBasePositionAndOrientation(cubs[i])[0][0]+np.sign(p.getBasePositionAndOrientation(cubs[i])[0][0])*0.1, maxVelocity=20)
  p.setJointMotorControl2(robot, 1, p.POSITION_CONTROL, targetPosition=p.getBasePositionAndOrientation(cubs[i])[0][1], maxVelocity=20)
  for _ in range(40):
    p.stepSimulation()
    time.sleep(0.01)
  p.stepSimulation()
  p.setJointMotorControl2(robot, 0, p.POSITION_CONTROL, targetPosition=-0.08, maxVelocity=20)
  for _ in range(20):
    p.stepSimulation()
    time.sleep(0.01)
  p.setJointMotorControl2(robot, 2, p.POSITION_CONTROL, targetPosition=np.sign(p.getBasePositionAndOrientation(cubs[i])[0][0])*0.180, maxVelocity=2)
  for _ in range(100):
    p.stepSimulation()
    time.sleep(0.01)
  p.setJointMotorControl2(robot, 0, p.POSITION_CONTROL, targetPosition=0.05, maxVelocity=20)
  for _ in range(10):
    p.stepSimulation()
    time.sleep(0.01)
  p.setJointMotorControl2(robot, 1, p.POSITION_CONTROL, targetPosition=p.getBasePositionAndOrientation(cubs[i])[0][1]+np.sign(p.getBasePositionAndOrientation(cubs[i])[0][1])*0.1, maxVelocity=20)
  for _ in range(10):
    p.stepSimulation()
    time.sleep(0.01)
  p.setJointMotorControl2(robot, 2, p.POSITION_CONTROL, targetPosition=p.getBasePositionAndOrientation(cubs[i])[0][0], maxVelocity=20)
  for _ in range(20):
    p.stepSimulation()
    time.sleep(0.01)
  p.setJointMotorControl2(robot, 0, p.POSITION_CONTROL, targetPosition=-0.08, maxVelocity=20)
  for _ in range(20):
    p.stepSimulation()
    time.sleep(0.01)
  p.setJointMotorControl2(robot, 1, p.POSITION_CONTROL, targetPosition=np.sign(p.getBasePositionAndOrientation(cubs[i])[0][1])*0.165, maxVelocity=2)
  for _ in range(100):
    p.stepSimulation()
    time.sleep(0.01)
