#! /usr/bin/python3

class Walk_2:

    def __init__(self, driver):

        # assign servos

        self.hip_roll_joint_left = driver.servo[5]
        self.hip_roll_joint_right = driver.servo[2]

        self.knee_joint_left = driver.servo[6]
        self.knee_joint_right = driver.servo[1]

        self.ankle_joint_left = driver.servo[7]
        self.ankle_joint_right = driver.servo[0]

        self.dt = 0.02

    def goto_init(self,):

        self.hip_roll_joint_left.angle = 90
        self.hip_roll_joint_right.angle = 90

        self.knee_joint_left.angle = 90
        self.knee_joint_right.angle = 90

        self.ankle_joint_left.angle = 90
        self.ankle_joint_right.angle = 90

    def start(self, angle = 15):

        print("START")

        for i in range(angle):

            self.hip_roll_joint_right.angle = 90 + i*4
    
            self.knee_joint_right.angle = 90 - i*5

            self.ankle_joint_right.angle = 90 - i*2

            time.sleep(self.dt)

    def transfer_left(self, angle=15):

        print("Transfer_left")

        for i in range(angle):

                self.hip_roll_joint_left.angle = 90 - i
        
                self.knee_joint_left.angle = 90 

                self.ankle_joint_left.angle = 90 + i

                time.sleep(self.dt)

 
    def raise_left(self, angle = 15):

        print("Raise_left")

        for i in range(angle):

            self.hip_roll_joint_left.angle = 60 + i*5
    
            self.knee_joint_left.angle = 90 - i*4

            self.ankle_joint_left.angle = 120   #OPP

            self.hip_roll_joint_right.angle =  135 - i*3
    
            self.knee_joint_right.angle =  30 + i*4

            self.ankle_joint_right.angle =  60 + i*2

            time.sleep(self.dt)

    def transfer_right(self, angle=30):

        print("Transfer_right")

        for i in range(angle):

                self.hip_roll_joint_right.angle = 90 - i
        
                self.knee_joint_right.angle = 90 

                self.ankle_joint_right.angle = 90 - i

                time.sleep(self.dt)        

    def raise_right(self, angle = 15):

        print("Raise_right")

        for i in range(angle):

            self.hip_roll_joint_right.angle = 60 + i*5
    
            self.knee_joint_right.angle = 90 - i*4 - 20

            self.ankle_joint_right.angle = 45

            self.hip_roll_joint_left.angle =  135 - i*3
    
            self.knee_joint_left.angle =  30 + i*4

            self.ankle_joint_left.angle =  120 - i*2

            time.sleep(self.dt)

    def check_r (self):

        print(self.hip_roll_joint_right.angle)
        print(self.knee_joint_right.angle)
        print(self.ankle_joint_right.angle)
    def check_l (self):

        print(self.hip_roll_joint_left.angle)
        print(self.knee_joint_left.angle)
        print(self.ankle_joint_left.angle)

from adafruit_servokit import ServoKit
import time
import math

driver = ServoKit(channels=16)

r = Walk_2(driver)

r.goto_init()
time.sleep(5)

for _ in range(3):

    r.start()
    time.sleep(0.02)

    r.transfer_left()
    time.sleep(0.02)

    r.raise_left()
    time.sleep(0.02)

    r.transfer_right()
    time.sleep(0.02)

    # r.check_r()
    # r.check_l()

    r.raise_right()
    time.sleep(0.02)