from pyniryo import *

robot = NiryoRobot("10.10.10.10")
robot.calibrate_auto()
robot.update_tool()

obsevervation_pose = 0,-0.38,-0.08,0,-1.45,0

#robot.move_joints(obsevervation_pose) #observation pose
robot.place_from_pose()

robot.close_connection()