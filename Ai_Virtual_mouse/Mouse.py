import cv2
import numpy as np
#import HandTrackingModule as htm
from mediapipe.framework.formats import landmark_pb2
import time
#import autopy

#wcam,hcam=648,480

# np_draw = np.solutions.drawing_utils
# np_hand = np.solutions.hands
# click = 0

cap = cv2.VideoCapture(0)
# cap.set(3,wcam)
# cap.set(4,hcam)

while True :
    _,img=cap.read() # '_' means variable ta ke dorkar nei
    cv2.imshow("Photo",img)
    cv2.waitKey(1)