import cv2 as cv
import numpy as np
vid = cv.VideoCapture("http://192.168.43.203:4747/video")

# def empty(a):
#     pass

# cv.namedWindow("Settings")
# cv.resizeWindow("Settings", 640, 240)
# cv.createTrackbar("thres1", "Settings", 10, 255, empty)
# cv.createTrackbar("thres2", "Settings", 10, 255, empty)
while True:
    # thres1 = cv.getTrackbarPos("thres1","Settings")
    # thres2 = cv.getTrackbarPos("thres2","Settings")

    ret, frame  = vid.read()
    cam = frame
    cv.imshow("camera", cam)
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame = cv.GaussianBlur(frame, (7,7), cv.BORDER_DEFAULT)
    frame = cv.Canny(frame, 0, 255)
    kernel = np.ones((3,3), np.uint8)
    frame = cv.morphologyEx(frame, cv.MORPH_CLOSE, kernel)
    frame = cv.dilate(frame, kernel, iterations=2)

    contours, hierarchy = cv.findContours(frame, 1, 2)
    
    money = 0
    
    for cnt in contours:
        area = cv.contourArea(cnt)
        # if area <= 12500 and area >= 12000:
        #     money += 1
        
        if area >= 17000 and area <= 19000:
            money += 10
        if area >= 12000 and area <= 14000:
            money += 5

        # print(area)
    if money != 0:
            print("Total amount in picture : ₹" + str(money))
            print("\n----------------------")

    cv.imshow("frame", frame)

    # framew = cv.GaussianBlur(frame, (5,5), cv. BORDER_DEFAULT)
    # # framew = cv.Canny(framew, 125, 255)
    # ret, thresh = cv.threshold(framew, 50, 100, cv.THRESH_BINARY)
    # cv.imshow("frameq", thresh)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    

vid.release()


cv.destroyAllWindows()