#此檔案練習攝影機下HSV跟濾波加上滑桿的應用

import cv2
import sys
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  #WIN10下
cv2.namedWindow('Gaussian_Blur')
cv2.createTrackbar('ksize', 'Gaussian_Blur', 0, 10, nothing)

while True:
    ret,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  #轉換為HSV
    #HSV下膚色的範圍
    lower = np.array([0,10,60])
    upper = np.array([20,150,255])
    #創建膚色遮罩
    binary = cv2.inRange(hsv,lower,upper)
    #高斯
    ksize  = cv2.getTrackbarPos('ksize', 'Gaussian_Blur')

    blur = cv2.GaussianBlur(binary, (2*ksize+1, 2*ksize+1), 0)
    #利用高斯後的遮罩與原圖比對得出剩膚色的原圖
    bitwise_and = cv2.bitwise_and(frame,frame,mask=blur)


    cv2.imshow('Gaussian_Blur', bitwise_and)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
cap.release()
