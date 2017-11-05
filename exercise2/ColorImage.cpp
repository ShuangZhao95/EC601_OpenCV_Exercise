#include "opencv2/core/core.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "iostream"

 // Author Rishab Shah

using namespace cv;
using namespace std;
 
int main(int argc, char** argv )
{
    Mat src;
    src = imread(argv[1], CV_LOAD_IMAGE_COLOR);
    namedWindow( "Original image", CV_WINDOW_AUTOSIZE );
    imshow( "Original image", src); //the original RGB image

	vector<Mat> input_planes(3);
	split(src,input_planes); //split image into channels
	Mat channel1_display, channel2_display, channel3_display;
        imshow("Red",   input_planes[2]); // the red channel of RGB image
        imshow("Green",   input_planes[1]); // the green channel of RGB image
        imshow("Blue",   input_planes[0]); // the blue channel of RGB image


	Mat ycrcb_image;
	cvtColor(src, ycrcb_image, CV_BGR2YCrCb); //change the RGB image src into YCrCb version
	split(ycrcb_image,input_planes); //split image into channels
        imshow("Y",   input_planes[0]);  // the Y channel of YCrCb image
        imshow("Cb",   input_planes[1]); // the Cb channel of YCrCb image
        imshow("Cr",   input_planes[2]); // the Cr channel of YCrCb image


	Mat hsv_image;
	cvtColor(src, hsv_image, CV_BGR2HSV); //change the RGB image src into HSV version
	vector<Mat> hsv_planes(3);
	split(hsv_image,hsv_planes); //split image into channels
        imshow("Hue",   hsv_planes[0]); // the hue channel of HSV image
        imshow("Saturation",   hsv_planes[1]); // the saturation channel of HSV image
        imshow("Value",   hsv_planes[2]); // the value channel of HSV image


	
    waitKey(0);                                       
    return 0;
} 