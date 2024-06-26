
#  Summer of Code 2023 - Image Processing and Object Detection


## 1) Learning the basics of Python, Numpy, OpenCV

The week 1 was comprised of learning through the given resources and the other extra documentation.

##

## 2) Testing after the basics of Python and OpenCV

-   **Demo Project - Money Counter** (To implement both **edge detection** and **get no. of objects**) (video of demo provided)
  
    - Used guassian blur and canny edge detection functions to convert the feed from camera of phone to get only the edges of coins.
    - Basically detects the number of objects/circles in the screen.
    - Then based upon the area of the circle(edge of the coin) (PS - which was caliberated before hand in code), it detects the type/value of the coin.
    - Then the value of the coins is added up after every refresh. (the video demo of the final working testing model is also provided in the repo).
  
##

## 3) Final code for determining the Porosity of the Metal

-   **The Porosity calculator** (Use combination of image processing techniques such as blurs and different thresholding techniques)
  
    - `image_path` contains the path of the highly magnified image of the surface of metal.
    - The default `blur_rate` and `threshold_value` is set to the recommended value.
    - This can be adjusted using the **live slider** to get the best configuration to find the dark pores of the metal surface inside the contours and verify the threshold image matches the approximate pore structure
    - Once the desired configuration is obtained press `q` to exit the *image recaliberation* and the value of porosity in `%` will be displayed
    - *(if the desired value is not obtained just adjust the values to best cover all the pores(dark areas) in cntours)*
