
# coding: utf-8

# In[248]:


import numpy as np
import cv2


# In[249]:


def Add_gaussian_Noise(image, pa, pb):
    row,col= image.shape
    mean = pa
    sigma = pb
    gauss = np.random.normal(mean,sigma,(row,col))
    gauss = gauss.reshape(row,col)
    noisy = np.copy(image)
    noisy = noisy + gauss 
    return noisy



# In[250]:


def Add_salt_pepper_Noise(image, pa, pb):
    row,col = image.shape
    out = np.copy(image)
    # Salt mode
    num_salt = np.ceil(row*col*pb)
    coords = [np.random.randint(0, i - 1, int(num_salt))
              for i in image.shape]
    out[coords] = 255
    # Pepper mode
    num_pepper = np.ceil(row*col*pa)
    coords = [np.random.randint(0, i - 1, int(num_pepper))
              for i in image.shape]
    out[coords] = 0
    return out


# In[251]:


image = cv2.imread("C:\\Users\\lenovo\\Desktop\\EC601\\OpenCV\\OpenCV_homework\\Test_images\\Lenna.png" ,0)

cv2.imshow("Original",image)
cv2.imwrite("C:\\Users\\lenovo\\Desktop\\EC601\\OpenCV\\OpenCV_homework\\exercise3 image\\Lenna_Original.png",image)
cv2.waitKey(0)


# In[252]:


mean = 0
sigma = 50
noise_img = Add_gaussian_Noise(image, mean, sigma)
cv2.imshow( "Gaussian Noise", noise_img)
cv2.imwrite("C:\\Users\\lenovo\\Desktop\\EC601\\OpenCV\\OpenCV_homework\\exercise3 image\\Lenna_Gaussian Noise.png", noise_img)
cv2.waitKey(0)


# In[253]:


noise_dst = np.copy(noise_img)
noise_dst = cv2.blur(noise_dst,(3,3))
cv2.imshow( "Box filter", noise_dst)
cv2.imwrite("C:\\Users\\lenovo\\Desktop\\EC601\\OpenCV\\OpenCV_homework\\exercise3 image\\Lenna_Gaussian Noise_Box filter_size3.png", noise_dst)
cv2.waitKey(0)


# In[254]:


noise_dst1 = np.copy(noise_img)
noise_dst1 = cv2.GaussianBlur(noise_dst1,(3,3),1.5)
cv2.imshow( "Gaussian filter", noise_dst1)
cv2.imwrite("C:\\Users\\lenovo\\Desktop\\EC601\\OpenCV\\OpenCV_homework\\exercise3 image\\Lenna_Gaussian Noise_Gaussian filter_size3.png", noise_dst1)
cv2.waitKey(0)


# In[260]:


noise_dst2 = np.copy(noise_img)
noise_dst2 = noise_dst2.astype(np.uint8)
noise_dst2 = cv2.medianBlur(noise_dst2,3)
cv2.imshow( "Median filter", noise_dst2)
cv2.imwrite("C:\\Users\\lenovo\\Desktop\\EC601\\OpenCV\\OpenCV_homework\\exercise3 image\\Lenna_Gaussian Noise_Median filter_size3.png", noise_dst2)
cv2.waitKey(0)


# In[231]:


pa=0.01
pb=0.01
noise_img2 = Add_salt_pepper_Noise(image, pa, pb)
cv2.imshow( "Salt and Pepper Noise",noise_img2)
cv2.imwrite("C:\\Users\\lenovo\\Desktop\\EC601\\OpenCV\\OpenCV_homework\\exercise3 image\\Lenna_Salt and Pepper Noise.png", noise_img2)
cv2.waitKey(0)


# In[239]:


noise_dst3 = np.copy(noise_img2)
noise_dst3 = cv2.blur(noise_dst3,(3,3))
cv2.imshow( "Box filter", noise_dst3)
cv2.imwrite("C:\\Users\\lenovo\\Desktop\\EC601\\OpenCV\\OpenCV_homework\\exercise3 image\\Lenna_Salt and Pepper Noise_Box filiter_size3.png", noise_dst3)
cv2.waitKey(0)


# In[243]:


noise_dst4 = np.copy(noise_img2)
noise_dst4 = cv2.GaussianBlur(noise_dst4,(3,3),1.5)
cv2.imshow( "Gaussian filter", noise_dst4)
cv2.imwrite("C:\\Users\\lenovo\\Desktop\\EC601\\OpenCV\\OpenCV_homework\\exercise3 image\\Lenna_Salt and Pepper Noise_Gaussian filiter_size3.png", noise_dst4)
cv2.waitKey(0)


# In[246]:


noise_dst5 = np.copy(noise_img2)
noise_dst5 = cv2.medianBlur(noise_dst5,7)
cv2.imshow( "Median filter", noise_dst5)
cv2.imwrite("C:\\Users\\lenovo\\Desktop\\EC601\\OpenCV\\OpenCV_homework\\exercise3 image\\Lenna_Salt and Pepper Noise_Median filiter_size7.png", noise_dst5)
cv2.waitKey(0)

