#!/usr/bin/python3

from glob import glob
from time import time, sleep
import cv2


period = 1000//(40)
frame_count = 0
start_time = time()

for file in sorted(glob('../tmp/*')):
    print(file)

    cap = cv2.VideoCapture(file)

    while True:

        ret, frame = cap.read()

        if ret:
            frame_count += 1
            cv2.imshow('Frame', frame)
            cv2.waitKey(period)
        else:
            break

    cap.release()

print('Frames: {}'.format(frame_count))
print('Time: {}'.format(time() - start_time))
cv2.destroyAllWindows()
