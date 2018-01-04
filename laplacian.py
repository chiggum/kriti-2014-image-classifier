import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys

img = cv2.imread(sys.argv[1],0)

laplacian = cv2.Laplacian(img,cv2.CV_64F)

cv2.imwrite(sys.argv[2], laplacian)