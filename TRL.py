# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 17:37:10 2024

@author: USER
"""

import cv2
import numpy as np

image = cv2.imread("D:/1.tiff")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
image = cv2.bitwise_not(image) 
blur = cv2.medianBlur(image,5) 
ret3, image = cv2.threshold(blur, 0 ,255, cv2.THRESH_BINARY+cv2.THRESH_TRIANGLE) 
skeleton = cv2.ximgproc.thinning(image) 

def calculate_total_length(skeleton):
    num_components, labels, stats, centroids = cv2.connectedComponentsWithStats(skeleton)
    total_length = 0
    noise_threshold =1
    for i in range(1, num_components):  
        if stats[i, cv2.CC_STAT_AREA] > noise_threshold:
            component = (labels == i).astype(np.uint8)
            total_length += calculate_component_length(component)
    return total_length
def calculate_component_length(component):
    coords = np.column_stack(np.where(component > 0))
    length = 0
    for j in range(len(coords) - 1):
        dx = abs(coords[j+1][0] - coords[j][0])
        dy = abs(coords[j+1][1] - coords[j][1])       
        if dx == 1 and dy == 1:
            length += 1.4142
        else:
            length += 1
    return length

total_length = calculate_total_length(skeleton)
print("TRL is", total_length*0.0063)