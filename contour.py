import cv2
import numpy as np

image = cv2.imread('images/img3.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)

_, thresholded = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour_image = np.zeros_like(image)
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)  # Green color, line thickness 2

filtered_contour_image = np.zeros_like(image)

# Define a minimum contour area threshold
min_contour_area =400

# Filter and draw the contours based on their area
for contour in contours:
    contour_area = cv2.contourArea(contour)
    print(contour_area)
    if contour_area > min_contour_area:
        cv2.drawContours(filtered_contour_image, [contour], -1, (0, 255, 0), 2) 

cv2.imshow('Original Image', image)
cv2.imshow('threshold Image', thresholded)
# cv2.imshow('Contour Image',filtered_contour_image)
cv2.waitKey(0)
cv2.destroyAllWindows()