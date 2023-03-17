from pyniryo import *
import cv2
import time



def move_to(x ,robot):    
    for i in range (0,9):
        if i ==x :
            match x:
                case 0:
                    robot.move_joints(-0.38, -0.54, -0.73, 0.03, -0.38, -0.13)
                case 1:
                    robot.move_joints(-0.07, -0.51, -0.74, -0.02, -0.38, -0.13)
                case 2:
                    robot.move_joints(0.19, -0.53, -0.72, -0.05, -0.38, -0.13)
                case 3:
                    robot.move_joints(-0.29, -0.66, -0.48, 0.12, -0.38, -0.13)
                case 4:
                    robot.move_joints(-0.07, -0.66, -0.47, -0.06, -0.38, -0.13)
                case 5:
                    robot.move_joints(0.14, -0.67, -0.45, -0.11, -0.38, -0.13)
                case 6:
                    robot.move_joints(-0.25, -0.83, -0.14, -0.11, -0.38, -0.13)
                case 7:
                    robot.move_joints(-0.08, -0.82, -0.17, -0.12, -0.38, -0.13)
                case 8:
                    robot.move_joints(0.11, -0.82, -0.18, -0.13, -0.38, -0.13)        
    robot.push_air_vacuum_pump()
    time.sleep(3)
    
def move_to_observation_pose (robot):  
    obsevervation_pose = -0.05,-0.28,-0.19,0.02,-1.60,-0.12 #observation pose
    robot.move_joints(obsevervation_pose) 
    robot.push_air_vacuum_pump()


def move_to_pick_up_pose (robot):
    pick_pose = (0.48, -0.51, -0.51, 0.52, -0.75, -0.69)
    robot.move_joints(pick_pose)
    robot.pull_air_vacuum_pump()
    robot.move_joints(0.48, -0.18, -0.51, 0.52, -0.75, -0.69)
    

def uncompress_img(compressed_img):
    frame = uncompress_image(compressed_img)
    return frame

robot=NiryoRobot("10.10.10.10")
robot.calibrate_auto()

move_to_observation_pose(robot)

move_to_pick_up_pose(robot)
#robot.set_learning_mode(True)





