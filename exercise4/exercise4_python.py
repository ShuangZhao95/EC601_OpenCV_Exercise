
# coding: utf-8

# In[1]:


import numpy as np
import cv2


# In[2]:


src = cv2.imread("C:\\Users\\lenovo\\Desktop\\EC601\\OpenCV\\OpenCV_homework\\Test_images\\Lenna.png")
gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
cv2.imshow("Input Image", src)
cv2.imwrite("C:\\Users\\lenovo\\Desktop\\EC601\\OpenCV\\OpenCV_homework\\exercise4 image\\Lenna_Input Image.png",src)
cv2.waitKey(0)


# In[3]:


threshold_type = 2
threshold_value = 128
[x,dst] = cv2.threshold(gray, threshold_value, 255, threshold_type)
cv2.imshow("Thresholded Image", dst)
cv2.imwrite("C:\\Users\\lenovo\\Desktop\\EC601\\OpenCV\\OpenCV_homework\\exercise4 image\\Lenna_Thresholded Image.png",dst)
cv2.waitKey(0)


# In[4]:


current_threshold = 128
max_threshold = 255
[x,thresholded] = cv2.threshold(gray, current_threshold, max_threshold, cv2.THRESH_BINARY)
cv2.imshow("Binary threshold",thresholded)
cv2.imwrite("C:\\Users\\lenovo\\Desktop\\EC601\\OpenCV\\OpenCV_homework\\exercise4 image\\Lenna_Binary threshold.png",thresholded)
cv2.waitKey(0)


# In[5]:


threshold1 = 27
threshold2 = 125
[x,binary_image1] = cv2.threshold(gray, threshold1, max_threshold, cv2.THRESH_BINARY)
[x,binary_image2] = cv2.threshold(gray, threshold2, max_threshold, cv2.THRESH_BINARY_INV)
band_thresholded_image = cv2.bitwise_and(binary_image1,binary_image2)
cv2.imshow("Band Thresholding", band_thresholded_image)
cv2.imwrite("C:\\Users\\lenovo\\Desktop\\EC601\\OpenCV\\OpenCV_homework\\exercise4 image\\Lenna_Band Thresholding.png",band_thresholded_image)
cv2.waitKey(0)


# In[6]:


[x,semi_thresholded_image] = cv2.threshold(gray, current_threshold, max_threshold, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
semi_thresholded_image = cv2.bitwise_and(gray,semi_thresholded_image)
cv2.imshow("Semi Thresholding", semi_thresholded_image)
cv2.imwrite("C:\\Users\\lenovo\\Desktop\\EC601\\OpenCV\\OpenCV_homework\\exercise4 image\\Lenna_Semi Thresholding.png",semi_thresholded_image)
cv2.waitKey(0)


# In[7]:


adaptive_thresh = cv2.adaptiveThreshold(gray, 255.0, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 101, 10 )
cv2.imshow("Adaptive Thresholding", adaptive_thresh);
cv2.imwrite("C:\\Users\\lenovo\\Desktop\\EC601\\OpenCV\\OpenCV_homework\\exercise4 image\\Lenna_Adaptive Thresholding.png",adaptive_thresh)
cv2.waitKey(0)

