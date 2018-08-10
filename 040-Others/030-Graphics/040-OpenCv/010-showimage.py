import cv2;

img = cv2.imread('test.jpg', 0);
cv2.imshow('test.jpg', img);
k = cv2.waitKey(0);
print(k);