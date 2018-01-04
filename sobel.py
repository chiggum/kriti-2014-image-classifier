import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys

img = cv2.imread(sys.argv[1],0)
sobelx = cv2.Sobel(img,cv2.CV_64F,2,2,ksize=9)
img=abs(sobelx)
cv2.imwrite(sys.argv[2], img)