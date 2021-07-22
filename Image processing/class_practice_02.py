#對於攝影機下利用HSV跟CANNY進行邊緣偵測及繪製
#解答在cameraSkinContours.py
import cv2
import sys
import numpy as np
import math


def nothing(x):
    pass

# Creating a window for later use
cv2.namedWindow('hsv_demo',cv2.WINDOW_NORMAL)
cv2.namedWindow('canny_demo',cv2.WINDOW_NORMAL)
cv2.namedWindow('test')

# Starting with 100's to prevent error while masking
#h, s, v = 100, 100, 100

# Creating track bar
cv2.createTrackbar('hl', 'hsv_demo', 0,   255, nothing)
cv2.createTrackbar('hu', 'hsv_demo', 0,   255, nothing)
cv2.createTrackbar('sl', 'hsv_demo', 0,   255, nothing)
cv2.createTrackbar('su', 'hsv_demo', 0,   255, nothing)
cv2.createTrackbar('vl', 'hsv_demo', 0,   255, nothing)
cv2.createTrackbar('vu', 'hsv_demo', 0,   255, nothing)
cv2.createTrackbar('threshold',      'canny_demo', 0, 100, nothing) #建立滑桿
cv2.createTrackbar('increase_ratio', 'canny_demo', 0, 5,   nothing)


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  #WIN10下

while True:
    # 抓取滑桿值
    # get info from track bar and appy to result
    hl = cv2.getTrackbarPos('hl', 'hsv_demo')
    hu = cv2.getTrackbarPos('hu', 'hsv_demo')
    sl = cv2.getTrackbarPos('sl', 'hsv_demo')
    su = cv2.getTrackbarPos('su', 'hsv_demo')
    vl = cv2.getTrackbarPos('vl', 'hsv_demo')
    vu = cv2.getTrackbarPos('vu', 'hsv_demo')
    threshold = cv2.getTrackbarPos('threshold',      'canny_demo')
    ratio     = cv2.getTrackbarPos('increase_ratio', 'canny_demo')

    ret,frame = cap.read()
    # 轉換成HSV
    # Converting to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 建立HSV遮罩
    # Normal masking algorithm
    lower = np.array([hl, sl, vl])
    upper = np.array([hu, su, vu])
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("hsv_demo", result)

    #將HSV遮罩後圖轉為灰階
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    h, w = gray.shape
    #canny edge detection
    edges = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(edges, threshold, threshold * ratio, apertureSize=3)
    cv2.imshow("canny_demo", edges)


    (cnts, _) = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, cnts, -1, (0, 255, 0), 2)
    mask = np.zeros(edges.shape, dtype="uint8")
    try:
        cv2.drawContours(mask, cnts, -1, 255, -1) #255 →白色, -1→塗滿
    except:
        pass

    cv2.imshow("canny_demo", cv2.bitwise_and(frame, frame, mask=mask))

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break



cv2.destroyAllWindows()
cap.release()
