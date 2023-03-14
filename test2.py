import cv2
import numpy as np

# Create a blank image with a white background
img=cv2.VideoCapture(0)


while True:
    ret,frame = img.read()

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
            x, y, w, h = cv2.boundingRect(contour)
            if x > a and y > 0 and x + w < a+c and y + h < c:
                print("Blue object found inside the square.")
                break

    cv2.imshow("",frame)
    if cv2.waitKey(1)==ord("q"):
        break
img.release()

