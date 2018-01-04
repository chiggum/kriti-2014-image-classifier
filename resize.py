import cv2
import sys

img = cv2.imread(sys.argv[1])
img=cv2.resize(img, (300, 300))
cv2.imwrite(sys.argv[2], img)