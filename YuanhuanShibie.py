import datetime
import imutils
import cv2
import numpy as np

Tupian = cv2.imread("C:/Users/Jonathan/Desktop/Yuan.png")

#Tupian = imutils.resize(Tupian, height=500, width=500) #调整图片尺寸
huidu = cv2.cvtColor(Tupian, cv2.COLOR_BGR2GRAY)       #彩色图像转为灰度图像
huidu = cv2.GaussianBlur(huidu, (21, 21), 0)           #灰度图像高斯模糊去除噪声

circles = cv2.HoughCircles(huidu, cv2.HOUGH_GRADIENT, dp=1, minDist=100,
                            param1=100, param2=30, minRadius=10, maxRadius=500)
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(Tupian,(i[0],i[1]),i[2],(0,0,255),2)
    # draw the center of the circle
    cv2.circle(Tupian,(i[0],i[1]),2,(0,255,0),3)
    cv2.putText(Tupian, "ZhiLiang:{}{}".format(i[2], "g"), (int(i[0]), int(i[1]-i[2]-20)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (255, 0, 0), 1)

cv2.imshow('detected circles',Tupian)
cv2.waitKey(0)
cv2.destroyAllWindows()



'''
 thresh = cv2.threshold(frameDelta, 160, 255, cv2.THRESH_BINARY)[1]

# 扩展阀值图像填充孔洞，找到阀值图像上的轮廓
    thresh = cv2.dilate(thresh, None, iterations=2)
    im, cnts, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in cnts:
        if cv2.contourArea(c) < args["min_area"]:
            continue

        (x, y), radius = cv2.minEnclosingCircle(c)
        text = (x, y)
        center = (int(x), int(y))
        radius = int(radius)
        img = cv2.circle(frame, center, radius, (0, 255, 0), 2)

    cv2.putText(frame, "ball's coordinate: {}".format(text), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

    cv2.imshow("image1", frame)
    cv2.imshow("image2", thresh)
    cv2.imshow("image3", frameDelta)

    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        break

camera.release()
cv2.destroyAllWindows()
'''