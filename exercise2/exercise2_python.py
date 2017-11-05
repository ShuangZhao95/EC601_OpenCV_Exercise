
# coding: utf-8

# In[1]:


import numpy as np
import cv2


# In[2]:


image = cv2.imread("C:\\Users\\lenovo\\Desktop\\EC601\\OpenCV\\OpenCV_homework\\Test_images\\Lenna.png")
cv2.imshow("Original",image)
cv2.waitKey(0)
cv2.imwrite("C:\\Users\\lenovo\\Desktop\\EC601\\OpenCV\\OpenCV_homework\\exercise2 image\\Lenna_Original.png",image)
(a,b,c)=image[20,25]
print("Original_red:%d,green:%d,blue:%d" %(c,b,a))
print(image.shape)


# In[3]:


input_planes = cv2.split(image)
cv2.imshow("Red",input_planes[2])
cv2.imwrite("C:\\Users\\lenovo\\Desktop\\EC601\\OpenCV\\OpenCV_homework\\exercise2 image\\Lenna_Red.png",input_planes[2])
r=input_planes[2][20,25]
print("red_red:%d" %r)
print(input_planes[2].shape)

cv2.imshow("Green",input_planes[1])
cv2.imwrite("C:\\Users\\lenovo\\Desktop\\EC601\\OpenCV\\OpenCV_homework\\exercise2 image\\Lenna_Green.png",input_planes[1])
g=input_planes[2][20,25]
print("green_green:%d" %g)
print(input_planes[1].shape)

cv2.imshow("Blue",input_planes[0])
cv2.imwrite("C:\\Users\\lenovo\\Desktop\\EC601\\OpenCV\\OpenCV_homework\\exercise2 image\\Lenna_Blue.png",input_planes[0])
b=input_planes[2][20,25]
print("blue_blue:%d" %b)
print(input_planes[0].shape)

cv2.waitKey(0)


# In[4]:


YCrCb = cv2.cvtColor(image,cv2.COLOR_BGR2YCrCb)
cv2.imshow("YCrCb",YCrCb)
cv2.imwrite("C:\\Users\\lenovo\\Desktop\\EC601\\OpenCV\\OpenCV_homework\\exercise2 image\\Lenna_YCrCb.png",YCrCb)
(a,b,c)=YCrCb[20,25]
print("YCrCb_Y:%d,Cb:%d,Cr:%d" %(a,b,c))
print(YCrCb.shape)

input_planes = cv2.split(YCrCb)
cv2.imshow("Y",input_planes[0])
cv2.imwrite("C:\\Users\\lenovo\\Desktop\\EC601\\OpenCV\\OpenCV_homework\\exercise2 image\\Lenna_Y.png",input_planes[0])
y=input_planes[0][20,25]
print("Y_Y:%d" %y)
print(input_planes[0].shape)

cv2.imshow("Cb",input_planes[1])
cv2.imwrite("C:\\Users\\lenovo\\Desktop\\EC601\\OpenCV\\OpenCV_homework\\exercise2 image\\Lenna_Cb.png",input_planes[1])
cb=input_planes[1][20,25]
print("Cb_Cb:%d" %cb)
print(input_planes[1].shape)

cv2.imshow("Cr",input_planes[2])
cv2.imwrite("C:\\Users\\lenovo\\Desktop\\EC601\\OpenCV\\OpenCV_homework\\exercise2 image\\Lenna_Cr.png",input_planes[2])
cr=input_planes[2][20,25]
print("Cr_Cr:%d" %cr)
print(input_planes[2].shape)

cv2.waitKey(0)


# In[6]:


hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow("hsv",hsv)
cv2.imwrite("C:\\Users\\lenovo\\Desktop\\EC601\\OpenCV\\OpenCV_homework\\exercise2 image\\Lenna_hsv.png",hsv)
(a,b,c)=hsv[20,25]
print("hsv_Hue:%d,Saturation:%d,Value:%d" %(a,b,c))
print(hsv.shape)

input_planes = cv2.split(hsv)
cv2.imshow("Hue",input_planes[0])
cv2.imwrite("C:\\Users\\lenovo\\Desktop\\EC601\\OpenCV\\OpenCV_homework\\exercise2 image\\Lenna_Hue.png",input_planes[0])
h=input_planes[0][20,25]
print("Hue_Hue:%d" %h)
print(input_planes[0].shape)

cv2.imshow("Saturation",input_planes[1])
cv2.imwrite("C:\\Users\\lenovo\\Desktop\\EC601\\OpenCV\\OpenCV_homework\\exercise2 image\\Lenna_Saturation.png",input_planes[1])
s=input_planes[1][20,25]
print("Saturation_Saturation:%d" %s)
print(input_planes[1].shape)

cv2.imshow("Value",input_planes[2])
cv2.imwrite("C:\\Users\\lenovo\\Desktop\\EC601\\OpenCV\\OpenCV_homework\\exercise2 image\\Lenna_Value.png",input_planes[2])
v=input_planes[2][20,25]
print("Value_Value:%d" %v)
print(input_planes[2].shape)

cv2.waitKey(0)

