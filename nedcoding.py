from pyniryo import *
import cv2



def move_to(board, x ,robot):
    position={
        board[0]:(-0.38, -0.54, -0.73, 0.03, -0.38, -0.13),
        board[1]:(-0.07, -0.51, -0.74, -0.02, -0.38, -0.13),
        board[2]:(0.19, -0.53, -0.72, -0.05, -0.38, -0.13),
        board[3]:(-0.29, -0.66, -0.48, 0.12, -0.38, -0.13),
        board[4]:(-0.07, -0.66, -0.47, -0.06, -0.38, -0.13),
        board[5]:(0.14, -0.67, -0.45, -0.11, -0.38, -0.13),
        board[6]:(-0.25, -0.83, -0.14, -0.11, -0.38, -0.13),
        board[7]:(-0.08, -0.82, -0.17, -0.12, -0.38, -0.13),
        board[8]:(0.11, -0.82, -0.18, -0.13, -0.38, -0.13),       
        }
    
    robot.move_joints([board[x]])
    
def move_to_observation_pose (robot):  
    obsevervation_pose = -0.05,-0.28,-0.19,0.02,-1.60,-0.12 #observation pose
    robot.move_joints(obsevervation_pose) 

def get_frame(robot):
    img_compressed = robot.get_img_compressed()
    frame = uncompress_image(img_compressed)
    time_count = 90
    frame = cv2.flip(frame, 1)
    frame = cv2.flip(frame, -1)
    w = 640
    h = 480
    return frame, w, h

def move_to_pick_up_pose (robot):
    pick_pose = ("")
    robot.move_joints(pick_pose)


robot=NiryoRobot("10.10.10.10")
robot.calibrate_auto()

move_to_observation_pose(robot)







