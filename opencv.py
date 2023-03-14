import cv2
import numpy as np

# Create a blank image with a white background
img=cv2.VideoCapture(0)


while True:
    ret,frame = img.read()
    frame = cv2.flip(frame, 1)

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


    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100:
            cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)
            x, y, w, hei = cv2.boundingRect(contour)
            
            if x > a and y > 0 and x + w < a+c and y + hei < c: #first square
                print("Object found inside the 1st square.")
                break            
            elif x > a+c and y > 0 and x + w < a+d and y + hei < c: #second square
                print("Object found inside the 2nd square.")
                break           
            elif x > a+d and y > 0 and x + w < (a+h) and y + hei < c: #third square
                print("Object found inside the 3rd square.")
                break
            elif x > a and y > c and x + w < a+c and y + hei < d: #forth square
                print("Object found inside the 4th square.")
                break    
            elif x > a+c and y > c and x + w < a+d and y + hei < d: #fifth square
                print("Object found inside the 5th square.")
                break
            elif x > a+d and y > c and x + w < a+h and y + hei < d: #sixth square
                print("Object found inside the 6th square.")
                break
            elif x > a and y > d and x + w < a+c and y + hei < h: #seventh square
                print("Object found inside the 7th square.")
                break
            elif x > a+c and y > d and x + w < a+d and y + hei < h: #eighth square
                print("Object found inside the 8th square.")
                break
            elif x > a+d and y > d and x + w < a+h and y + hei < h: #ninth square
                print("Object found inside the 9th square.")
                break
           

    cv2.imshow("",frame)
    if cv2.waitKey(1)==ord("q"):
        break
img.release()

