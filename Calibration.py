

import cv2 
import math
points = []
def mouse_callback(event, x, y, flags, param): 
    global points
    if event == cv2.EVENT_LBUTTONDOWN: #click left button of mouse indicating the known points 
        points.append((x, y))
        if len(points) == 2:
            print("Point 1 coordinates: ", points[0]) 
            print("Point 2 coordinates: ", points[1]) 
            dist = math.sqrt((points[1][0] - points[0][0]) ** 2 + (points[1][1] - points[0][1]) ** 2) 
            print("Number of pixels in between two points is: ", dist) #prints the number of pixels in that known points
img = cv2.imread("D:/scale.JPG") #set the directory of the image
cv2.namedWindow("image")
cv2.setMouseCallback("image", mouse_callback)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
