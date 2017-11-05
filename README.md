# EC601_OpenCV_Exercise

OpenCV homework of EC601

## Exercise1

1. The class Mat represents an
n-dimensional dense numerical single-channel or multi-channel array. For
example, in a 2-dimensional array named X, the program can access the array by
a pointer. The program can access the ith row by using X.row(i), and the
program can access the jth column by using X.col(j). On top of this, the
program can access the element of the array by using M.at<typename>(i,j).


2. A image contains M channels,
the M bytes of every pixel are stored together. For a 3 channel image, the RGB
channels are stored in the order of Blue, Green and Red.

## Exercise2

I ran the cpp code and implemented the same thing in python.

Then I printed all the outputs in the exercise2 folder.

The values of pixel at (20,25) in the RGB, YCbCr and HSV versions of the image can be accessed in exercise2/exercise2_python.ipynb:

RGB: red:225,green:122,blue:106

YCbCr: Y:151,Cb:181,Cr:103

HSV: Hue:4,Saturation:135,Value:225

The ranges of pixel values in each channel are all from (0, 0) to (255, 255) and the number of channels are all three.

## Exercise3

I ran the cpp code and implemented the same thing in python.

Then I tried different values of mean and sigma in the Gaussian case and different values of pa and pb in the salt-and-pepper case.

I also tried to change the kernel sizes for all the filters with all different values for noisesand print the results for 3x3, 5x5 and 7x7 kernels. 

Then I printed all the outputs in the exercise3 folder.

It seems that the median filter of sizes 3 works better than others. 

## Exercise4

I ran the cpp code and implemented the same thing in python.

Then I printed all the outputs in the exercise4 folder.

The disadvantages of binary threshold are:

The application is restricted to tasks where internal detail is  not required as a distinguishing characteristic. It is hard to extend to 3D and it is difficult to obtain reliable binary images without restricting the environment.

When is Adaptive Threshold useful?

Thresholding is used to segment an image by setting all pixels whose intensity values are above a threshold to a foreground value and all the remaining pixels to a background value. Whereas the conventional thresholding operator uses a global threshold for all pixels, adaptive thresholding changes the threshold dynamically over the image. This more sophisticated version of thresholding can accommodate changing lighting conditions in the image. 

The Adaptive Threshold will be useful when we have to deal with a result of a strong illumination gradient or shadows.





