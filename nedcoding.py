from pyniryo import *
import cv2
import time
import threading

robot =NiryoRobot("10.10.10.10")
sound=("let's begin.mp3","you may go first.mp3","it's your turn now.mp3", "I m thinking, I m thinking.mp3","well well well.mp3","great move.mp3", "hmmmmmm.mp3", "it's a tie.mp3", "don't cry, better luck next time.mp3" )

class Saved_position():
    #obsevervation_pose = -0.05,-0.28,-0.19,0.02,-1.60,-0.12 #observation pose for big board
    obsevervation_pose = [-0.04, -0.36, -0.45, 0.02, -1.23, -0.12] #observation pose for small board
    pick_pose = [0.50, -0.52, -0.41, 0.25, -0.75, 0.14]
    rest_pose = [0.48, -0.18, -0.51, 0.52, -0.75, -0.69]
    square0 = [-0.22, -0.60, -0.67, -0.04, -0.31, -0.13]
    square1 = [-0.06, -0.58, -0.70, 0.03, -0.30, -0.12]
    square2 = [0.11, -0.59, -0.69, 0.03, -0.29, -0.13]
    square3 = [-0.20, -0.68, -0.48, -0.08, -0.30, -0.13]
    square4 = [-0.05, -0.68, -0.50, -0.05, -0.30, -0.14]
    square5 = [0.10, -0.68, -0.49, -0.04, -0.30, -0.14]
    square6 = [-0.16, -0.79, -0.28, -0.19, -0.29, -0.14]
    square7 = [-0.04, -0.78, -0.30, -0.19, -0.29, -0.14]
    square8 = [0.09, -0.78, -0.29, -0.14, -0.28, -0.14]
    def access_pick_up_pose(self, saved_pose):
        self.pick_pose = saved_pose  

def move_to(x ,robot):    
    for i in range (0,9):
        if i ==x :
            match x:
                case 0:
                    robot.move_joints(Saved_position.square0)
                case 1:                  
                    robot.move_joints(Saved_position.square1)
                case 2:                   
                    robot.move_joints(Saved_position.square2)
                case 3:                   
                    robot.move_joints(Saved_position.square3)
                case 4:                    
                    robot.move_joints(Saved_position.square4)
                case 5:                   
                    robot.move_joints(Saved_position.square5)
                case 6:                   
                    robot.move_joints(Saved_position.square6)
                case 7:                   
                    robot.move_joints(Saved_position.square7)
                case 8:                   
                    robot.move_joints(Saved_position.square8)        
    robot.push_air_vacuum_pump()
    time.sleep(3)
    
def move_to_observation_pose (robot):  
    robot.move_joints(Saved_position.obsevervation_pose) 
    robot.push_air_vacuum_pump()

def move_to_pick_up_pose (robot):
    robot.move_joints(Saved_position.rest_pose)   
    print(Saved_position.pick_pose)
    robot.move_joints(Saved_position.pick_pose)
    robot.pull_air_vacuum_pump()
    robot.move_joints(Saved_position.rest_pose)
    
def uncompress_img(compressed_img):
    frame = uncompress_image(compressed_img)
    return frame

def play_sound(num, robot):
    robot.set_volume(100)
    match num:        
        case 10:
            robot.play_sound("it's a tie.mp3", True, 0, robot.get_sound_duration("it's a tie.mp3"))
        case 100:
            robot.play_sound("don't cry, better luck next time.mp3", True, 0, robot.get_sound_duration("don't cry, better luck next time.mp3"))
        case 0:
            robot.play_sound("you may go first.mp3", True, 0, robot.get_sound_duration("you may go first.mp3"))
        case 1:
            robot.play_sound("it's your turn now.mp3", True, 0, robot.get_sound_duration("it's your turn now.mp3"))
        case 2:
            robot.play_sound("I m thinking, I m thinking.mp3", True, 0, robot.get_sound_duration("I m thinking, I m thinking.mp3"))
        case 3:
            robot.play_sound("well well well.mp3", True, 0, robot.get_sound_duration("well well well.mp3"))
        case 4:
            robot.play_sound("great move.mp3", True, 0, robot.get_sound_duration("great move.mp3"))
                
def ring_light(num, robot):
    
    match num:
        case 0:
            robot.led_ring_solid([0,255,0]) #first time
        case 10:
            robot.led_ring_rainbow_chase(0,2,True) #tie
        case 100:
            robot.led_ring_solid([255,0,0])#ned win
        case _:
            robot.led_ring_solid([255,105,180]) #user is making move
    
def trajectory(robot):
    robot.execute_registered_trajectory("ending")


        






