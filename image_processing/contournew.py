import cv2
import numpy as np

image = cv2.imread('images/img3.jpg')
result = image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# _, thresholded = cv2.threshold(blurred, 195, 255, cv2.THRESH_BINARY)

_, thresholded = cv2.threshold(blurred,240,255, cv2.THRESH_BINARY)

edges = cv2.Canny(thresholded, 50, 150)

contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour_image = np.zeros_like(image)

cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)  # Green color, line thickness 2

boxes = []

for contour in contours:
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.04 * peri, True)

        if len(approx) == 4:
            boxes.append(approx)

for box in boxes:
    cv2.drawContours(result, [box], -1, (0, 255, 0), 2)



cv2.imshow('Original Image', image)
cv2.imshow('threshold Image', thresholded)
cv2.imshow('edge image', edges)
cv2.imshow('contour image', contour_image)
cv2.imshow('result image', result)


cv2.waitKey(0)
# Close the OpenCV windows
cv2.destroyAllWindows()
