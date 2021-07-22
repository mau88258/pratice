#單純車牌輪廓抓取及繪製車牌框
import cv2

#讀入相片檔案
image = cv2.imread("license1.jpg")

#轉為灰階
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#使用Canny抓出邊緣，75及200這兩個值請參考之前的文章來設定。
edged = cv2.Canny(gray, 75, 200)

#顯示原始圖片及Canny邊緣處理後的圖片
cv2.imshow("Original", image)
cv2.imshow("Edge Map", edged)

#找出所有的輪廓。記得要使用cv2.RETR_EXTERNAL參數，才能排除掉發票內的字體。
(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#使用Python sorted指令，將所有Contours依面積大小由大至小排列，並僅取前七個。
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:7]

# 依序來處理這七個contours
for index, c in enumerate(cnts):
        # 取得其周長並進行Contour Approximation處理（\epsilon 值取周長的1%）
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.01 * peri, True)

        # 參考用，顯示周長點數以及經Approximation處理後的點數。
        print("index: {}, original: {}, approx: {}".format(index, len(c), len(approx)))

        # 如果有四個頂點，且是面積最大那個
        if len(approx) == 4 and index == 0:
                # 畫出輪廓線
                cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)

# 顯示結果
cv2.imshow("Output", image)
cv2.waitKey(0)
cv2.destroyAllWindows() 
