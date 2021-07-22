#在較複雜的環境中抓去車牌方框並且繪製出boundingbox
import cv2
import numpy as np
from numpy.lib.type_check import imag

#讀入相片檔案
image = cv2.imread("license2.jpg")

#轉成灰階
img = image.copy()
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow('gray',gray)
#濾波
blur = cv2.GaussianBlur(gray,(15,15),0)
#cv2.imshow('blur',blur)


#邊緣偵測模主建立
def auto_canny(image,sigma=0.33):
        v = np.median(image)
        lower = int(max(0,(1.0-sigma) * v))
        upper = int(min(255,(1.0+sigma) * v))
        edge = cv2.Canny(image,lower,upper)
        return edge
#使用邊緣偵測
edge = auto_canny(blur)
#cv2.imshow('edge',edge)

#尋找輪廓
(cnts,_) = cv2.findContours(edge,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

#尋找最大面積輪廓
i=0
maxArea = 0
maxAreaIdex = 0
for c in cnts:
        area = cv2.contourArea(c)  #計算面積
        if area > maxArea:
                maxArea = area
                maxAreaIdex = i
        i += 1

#繪製輪廓
mask = np.zeros(image.shape[:2],dtype="uint8") #建立與原圖大小一樣的全黑圖
cv2.drawContours(mask,[cnts[maxAreaIdex]],-1,(255,255,255),-1) #在mask上繪製最大輪廓的面積
#cv2.imshow('mask',mask)

#將遮罩與原圖相加輸出
output = cv2.bitwise_and(image,image,mask=mask)
#cv2.imshow('output',output)

#繪製boundbox
(x, y, w, h) = cv2.boundingRect(cnts[maxAreaIdex]) #從輪廓中提取xyhw
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2) #繪製方框
cv2.putText(img,"car plate",(x+2,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
cv2.imshow('boundingbox',img)

cv2.waitKey(0)
cv2.destroyAllWindows()