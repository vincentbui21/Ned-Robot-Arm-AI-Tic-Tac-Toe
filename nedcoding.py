from pyniryo import *

robot = NiryoRobot("10.10.10.10")
robot.calibrate_auto()
robot.update_tool()

obsevervation_pose = 0,-0.32,0,0,-1.568,0

#robot.move_joints(obsevervation_pose) #observation pose
robot.place_from_pose()

robot.close_connection()