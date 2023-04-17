import cv2
import numpy as np
import time
from pyniryo import *
import nedcoding


#robot = NiryoRobot("10.10.10.10")

def detect_move():
    from aicode import board
    from nedcoding import robot
    #img=cv2.VideoCapture(0)
    robot=nedcoding.robot

    arr=[0,0,0,0,0,0,0,0,0]
    while True:       
        #time_count = img.get(cv2.CAP_PROP_FPS) * 3
        #ret,frame = img.read()  
                 
        img_compressed = robot.get_img_compressed()
        frame = nedcoding.uncompress_img(img_compressed)
        
        #frame = cv2.flip(frame, 1)
        frame = cv2.flip(frame, -1)

        time_count = 90
        w = 640
        h = 480    

        #w = int(img.get(3))
        #h = int(img.get(4))
       
        a=int((w-h)/2)
        c=int(h*(1/3))
        d=int(h*(2/3))

        y1=int((1/6)*h)
        y2=int((1/2)*h)
        y3=int((5/6)*h)

        x1=int(a + (1/6)*h)
        x2=int(a + (1/2)*h)
        x3=int(a + (5/6)*h)

        radius = y1

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

        lower_green = np.array([36, 25, 25]) #need to be update
        upper_green = np.array([86, 255, 255]) #need to be update

        mask = cv2.inRange(hsv, lower_green, upper_green)
        blur = cv2.GaussianBlur(mask, (5, 5), 0)

        contours, hierarchy = cv2.findContours(blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
       
        for i in range(0,9):
            match i:
                case 0:
                    if board[i] == "X":
                        cv2.line(frame, (a,0), (a+c,c),(0,255,0), 3)
                        cv2.line(frame, (a+c,0), (a,c),(0,255,0), 3)
                    elif board[i]=="O":
                        cv2.circle(frame,(x1,y1), radius, (0,255,0),3)
                case 1:
                    if board[i] == "X":
                        cv2.line(frame, (a+c,0), (a+d,c),(0,255,0), 3)
                        cv2.line(frame, (a+d,0), (a+c,c),(0,255,0), 3)
                    elif board[i]=="O":
                        cv2.circle(frame,(x2,y1), radius, (0,255,0),3)
                case 2:
                    if board[i] == "X":
                        cv2.line(frame, (a+d,0), (a+h,c),(0,255,0), 3)
                        cv2.line(frame, (a+h,0), (a+d,c),(0,255,0), 3)
                    elif board[i]=="O":
                        cv2.circle(frame,(x3,y1), radius, (0,255,0),3)
                case 3:
                    if board[i] == "X":
                        cv2.line(frame, (a,c), (a+c,d),(0,255,0), 3)
                        cv2.line(frame, (a+c,c), (a,d),(0,255,0), 3)
                    elif board[i]=="O":
                        cv2.circle(frame,(x1,y2), radius, (0,255,0),3)
                case 4:
                    if board[i] == "X":
                        cv2.line(frame, (a+c,c), (a+d,d),(0,255,0), 3)
                        cv2.line(frame, (a+d,c), (a+c,d),(0,255,0), 3)
                    elif board[i]=="O":
                        cv2.circle(frame,(x2,y2), radius, (0,255,0),3)
                case 5:
                    if board[i] == "X":
                        cv2.line(frame, (a+d,c), (a+h,d),(0,255,0), 3)
                        cv2.line(frame, (a+h,c), (a+d,d),(0,255,0), 3)
                    elif board[i]=="O":
                        cv2.circle(frame,(x3,y2), radius, (0,255,0),3)
                case 6:
                    if board[i] == "X":
                        cv2.line(frame, (a,d), (a+c,h),(0,255,0), 3)
                        cv2.line(frame, (a+c,d), (a,h),(0,255,0), 3)
                    elif board[i]=="O":
                        cv2.circle(frame,(x1,y3), radius, (0,255,0),3)
                case 7:
                    if board[i] == "X":
                        cv2.line(frame, (a+d,d), (a+c,h),(0,255,0), 3)
                        cv2.line(frame, (a+c,d), (a+d,h),(0,255,0), 3)
                    elif board[i]=="O":
                        cv2.circle(frame,(x2,y3), radius, (0,255,0),3)
                case 8:
                    if board[i] == "X":
                        cv2.line(frame, (a+d,d), (a+h,h),(0,255,0), 3)
                        cv2.line(frame, (a+h,d), (a+d,h),(0,255,0), 3)
                    elif board[i]=="O":
                        cv2.circle(frame,(x3,y3), radius, (0,255,0),3)

        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 2000:
                cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)
                x, y, w, hei = cv2.boundingRect(contour)
                
                if x > a and y > 0 and x + w < a+c and y + hei < c and board[0]==' ': #first square                                               
                    arr[0]+=1
                    if arr[0]==time_count:
                        print("Object found inside 1st square")                      
                        return 0
                                    
                elif x > a+c and y > 0 and x + w < a+d and y + hei < c and board[1]==' ': #second square
                    arr[1]+=1
                    if arr[1]==time_count:
                        print("Object found inside 2nd square")
                        return 1
                                      
                elif x > a+d and y > 0 and x + w < (a+h) and y + hei < c and board[2]==' ': #third square
                    arr[2]+=1
                    if arr[2]==time_count:
                        print("Object found inside 3rd square")
                        return 2
                            
                elif x > a and y > c and x + w < a+c and y + hei < d and board[3]==' ': #forth square
                    arr[3]+=1
                    if arr[3]==time_count:
                        print("Object found inside 4th square")
                        return 3
                               
                elif x > a+c and y > c and x + w < a+d and y + hei < d and board[4]==' ': #fifth square
                    arr[4]+=1
                    if arr[4]==time_count:
                        print("Object found inside 5th square")
                        return 4
                            
                elif x > a+d and y > c and x + w < a+h and y + hei < d and board[5]==' ': #sixth square
                    arr[5]+=1
                    if arr[5]==time_count:
                        print("Object found inside 6th square")
                        return 5
                                
                elif x > a and y > d and x + w < a+c and y + hei < h and board[6]==' ': #seventh square
                    arr[6]+=1
                    if arr[6]==time_count:
                        print("Object found inside 7th square")
                        return 6
                                 
                elif x > a+c and y > d and x + w < a+d and y + hei < h and board[7]==' ': #eighth square
                    arr[7]+=1
                    if arr[7]==time_count:
                        print("Object found inside 8th square")
                        return 7
                                  
                elif x > a+d and y > d and x + w < a+h and y + hei < h and board[8]==' ': #ninth square
                    arr[8]+=1
                    if arr[8]==time_count:
                        print("Object found inside 9th square")
                        return 8
                                 
                else:
                    pass   

        cv2.imshow("Player turn",frame)
        if cv2.waitKey(1)==ord("q"):
            break           
    

