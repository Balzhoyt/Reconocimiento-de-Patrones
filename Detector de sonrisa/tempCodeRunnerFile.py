
import numpy as np
import cv2

import sys

# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('data_haarcascade/haarcascade_frontalface_default.xml')
# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('data_haarcascade/haarcascade_eye.xml')

smile_cascade = cv2.CascadeClassifier('data_haarcascade/haarcascade_smile.xml')