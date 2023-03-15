import cv2
import numpy as np
import time
from pyniryo import * 
import ttt
"""
robot = NiryoRobot("10.10.10.10")
robot.calibrate_auto()
obsevervation_pose = 0,-0.38,-0.08,0,-1.45,0
robot.move_joints(obsevervation_pose) #observation pose
"""


def detect_move():
    img=cv2.VideoCapture(0)
    arr=[0,0,0,0,0,0,0,0,0]
    while True:
        time_count = img.get(cv2.CAP_PROP_FPS) * 3
        ret,frame = img.read()
        frame = cv2.flip(frame, 1)
        #frame = cv2.flip(frame, -1)

        w = int(img.get(3))
        h = int(img.get(4))
        a=int((w-h)/2)
        c=int(h*(1/3))
        d=int(h*(2/3))


        cv2.rectangle(frame,(a,0), (a+c,c),(0,0,0),5)
        cv2.rectangle(frame,(a+c, 0), (a+d,c), (0,0,0), 5)
        cv2.rectangle(frame,(a+d, 0), (a+h,c), (0,0,0), 5)

        cv2.rectangle(frame,(a, c), (a+c,d), (0,0,0), 5)
        cv2.rectangle(frame,(a+c, c), (a+d,d), (0,0,0), 5)
        cv2.rectangle(frame,(a+d, c), (a+h,d), (0,0,0), 5)

        cv2.rectangle(frame,(a, d), (a+c,h), (0,0,0), 5)
        cv2.rectangle(frame,(a+c, d), (a+d,h), (0,0,0), 5)
        cv2.rectangle(frame,(a+d, d), (a+h,h), (0,0,0), 5)

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_blue = np.array([90, 50, 50])
        upper_blue = np.array([130, 255, 255])

        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        blur = cv2.GaussianBlur(mask, (5, 5), 0)

        contours, hierarchy = cv2.findContours(blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        start_time = 0
        


        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 2000:
                cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)
                x, y, w, hei = cv2.boundingRect(contour)
                
                if x > a and y > 0 and x + w < a+c and y + hei < c and ttt.board[0][0]==0: #first square                                               
                    arr[0]+=1
                    if arr[0]==time_count:
                        print("Object found inside 1st square")
                        return 0,0
                                    
                elif x > a+c and y > 0 and x + w < a+d and y + hei < c and ttt.board[0][1]==0: #second square
                    arr[1]+=1
                    if arr[1]==time_count:
                        print("Object found inside 2nd square")
                        return 0,1
                                      
                elif x > a+d and y > 0 and x + w < (a+h) and y + hei < c and ttt.board[0][2]==0: #third square
                    arr[2]+=1
                    if arr[2]==time_count:
                        print("Object found inside 3rd square")
                        return 0,2
                            
                elif x > a and y > c and x + w < a+c and y + hei < d and ttt.board[1][0]==0: #forth square
                    arr[3]+=1
                    if arr[3]==time_count:
                        print("Object found inside 4th square")
                        return 1,0
                               
                elif x > a+c and y > c and x + w < a+d and y + hei < d and ttt.board[1][1]==0: #fifth square
                    arr[4]+=1
                    if arr[4]==time_count:
                        print("Object found inside 5th square")
                        return 1,1
                            
                elif x > a+d and y > c and x + w < a+h and y + hei < d and ttt.board[1][2]==0: #sixth square
                    arr[5]+=1
                    if arr[5]==time_count:
                        print("Object found inside 6th square")
                        return 1,2
                                
                elif x > a and y > d and x + w < a+c and y + hei < h and ttt.board[2][0]==0: #seventh square
                    arr[6]+=1
                    if arr[6]==time_count:
                        print("Object found inside 7th square")
                        return 2,0
                                 
                elif x > a+c and y > d and x + w < a+d and y + hei < h and ttt.board[2][1]==0: #eighth square
                    arr[7]+=1
                    if arr[7]==time_count:
                        print("Object found inside 8th square")
                        return 2,1
                                  
                elif x > a+d and y > d and x + w < a+h and y + hei < h and ttt.board[2][2]==0: #ninth square
                    arr[8]+=1
                    if arr[8]==time_count:
                        print("Object found inside 9th square")
                        return 2,2
                                 
                else:
                    pass   

        cv2.imshow("",frame)
        if cv2.waitKey(1)==ord("q"):
            break           
    img.release()

