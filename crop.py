import cv2
import matplotlib
img=cv2.imread('image.jpg')
img[y1:y2 ,x1:x2]  #-----lower and upper limit of x & y co-ordinate
cv2.imshow("image",img)
