

import cv2
import numpy as np
image = cv2.imread("D:/1.tiff") 
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
image = cv2.bitwise_not(image) 
blur = cv2.medianBlur(image,5) 
ret3, binary_image = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) 
ret3, image = cv2.threshold(blur, 0 ,255, cv2.THRESH_BINARY+cv2.THRESH_TRIANGLE) 
skeleton_image = cv2.ximgproc.thinning(image)
distance_transform = cv2.distanceTransform(binary_image, cv2.DIST_L2, 5)
pixel_size_cm = 0.0063
surface_area = 0
for y in range(skeleton_image.shape[0]):
    for x in range(skeleton_image.shape[1]):
        if skeleton_image[y, x] > 0: 
            radius = distance_transform[y, x] * pixel_size_cm
            circumference = 2 * np.pi * radius 
            surface_area += circumference
SA = surface_area * pixel_size_cm
print( SA)
