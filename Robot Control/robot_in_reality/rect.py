#!/usr/bin/env python3

import cv2
import time
import numpy as np


from cars import Camera, Motors, Connection, RESOLUTIONS, Direction
camera_matrix = np.load('camera_calibration_data/cameraMatrix.npy')
camera_distortion = np.load('camera_calibration_data/distCoeffs.npy')
MARKER_SIDE = 0.042

dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_APRILTAG_16h5)
detectorParams = cv2.aruco.DetectorParameters_create()
detectorParams.cornerRefinementMethod = cv2.aruco.CORNER_REFINE_CONTOUR
map1, map2 = np.load('camera_calibration_data/map1.npy'), np.load('camera_calibration_data/map2.npy')
img0 = cv2.imread("images/photo3.png")
size = (img0.shape[1], img0.shape[0])
rect_camera_matrix = cv2.getOptimalNewCameraMatrix(camera_matrix, camera_distortion, size, alpha = 1)[0]


def main():
    while True:
        rect_img0 = cv2.remap(img0, map1, map2, cv2.INTER_LINEAR)
        cv2.imshow('', rect_img0)
        keypress = cv2.pollKey() & 0xFF
        if keypress == ord('q'):
            break
    

if __name__ == "__main__":
    main()