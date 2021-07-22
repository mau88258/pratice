#此檔案練習在攝影機下輸出HSV遮罩過後的圖

import cv2
import sys
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  #WIN10下
while True:
    ret,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  #轉換為HSV
    #HSV下膚色的範圍
    lower = np.array([3,10,63])
    upper = np.array([27,82,242])
    #創建膚色遮罩
    binary = cv2.inRange(hsv,lower,upper)
    #利用遮罩與原圖比對得出剩膚色的原圖
    bitwise_and = cv2.bitwise_and(frame,frame,mask=binary)
    cv2.imshow("hsv_demo", bitwise_and)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
cap.release()
