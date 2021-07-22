#利用HSV跟canny數值滑桿對於圖中目標的色彩輸出直線繪製
import cv2
import sys
import numpy as np
import math



def nothing(x):
    pass

# Creating a window for later use
cv2.namedWindow('hsv_demo',cv2.WINDOW_NORMAL)
cv2.namedWindow('canny_demo',cv2.WINDOW_NORMAL)


# Starting with 100's to prevent error while masking
#h, s, v = 100, 100, 100

# Creating track bar
cv2.createTrackbar('hl', 'hsv_demo', 0,   179, nothing)
cv2.createTrackbar('hu', 'hsv_demo', 0,   179, nothing)
cv2.createTrackbar('sl', 'hsv_demo', 0,   255, nothing)
cv2.createTrackbar('su', 'hsv_demo', 0,   255, nothing)
cv2.createTrackbar('vl', 'hsv_demo', 0,   255, nothing)
cv2.createTrackbar('vu', 'hsv_demo', 0,   255, nothing)
cv2.createTrackbar('threshold',      'canny_demo', 0, 100, nothing) #建立滑桿
cv2.createTrackbar('increase_ratio', 'canny_demo', 0, 5,   nothing)


try:
    imagePath = "wm3.jpg"
    image = cv2.imread(imagePath)
except:
    image = cv2.imread("lena256rgb.jpg")


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
    # 轉換成HSV
    # Converting to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 建立HSV遮罩
    # Normal masking algorithm
    lower = np.array([hl, sl, vl])
    upper = np.array([hu, su, vu])
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow("hsv_demo", result)

    #threshold = cv2.getTrackbarPos('threshold',      'canny_demo')
    #ratio     = cv2.getTrackbarPos('increase_ratio', 'canny_demo')
    #將HSV遮罩後圖轉為灰階
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    h, w = gray.shape
    #canny edge detection
    edges = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(edges, threshold, threshold * ratio, apertureSize=3)
    cv2.imshow("canny_demo", edges)

    key = (cv2.waitKey(1) & 0xFF)

    newImage = image.copy()

    try:
        plines = cv2.HoughLines(edges, 1, np.pi/180, 80)
        for lines in plines:
            for (rho, theta) in lines:
                x0 = np.cos(theta)*rho 
                y0 = np.sin(theta)*rho
                pt1 = ( int(x0 + (h+w)*(-np.sin(theta))), int(y0 + (h+w)*np.cos(theta)) )
                pt2 = ( int(x0 - (h+w)*(-np.sin(theta))), int(y0 - (h+w)*np.cos(theta)) )
                cv2.line(newImage, pt1, pt2, (0, 0, 255), 3) 

        #cal = (math.atan((pt2[1]-pt1[1])/(pt2[0]-pt1[0]))*180)%360
        #print(cal)

        cv2.imshow("redline", newImage)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            cv2.imwrite("water_meter.png", newImage)
            break

    except TypeError:
        print("The Houghlines function returns None, try decrease the threshold!")

cv2.destroyAllWindows()
