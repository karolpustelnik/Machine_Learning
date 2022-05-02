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



def main():
    marker_detected = False
    cv2.namedWindow("demo")
    connection = Connection()
    cam = Camera(connection=connection)
    motors = Motors(connection=connection)
    while True:
        cam.flash_on()
        connection.keep_stream_alive()
        #if marker_detected == False:
            #motors.command(61, Direction.LEFT)
        #time.sleep(0.1)
        img = cam.get_frame()
        cv2.imshow("demo", img)
        corners, ids, _ = cv2.aruco.detectMarkers(img, dictionary = dictionary, parameters = detectorParams, cameraMatrix = camera_matrix)
        if ids != None:
            marker_detected = True
            if ids == 6:
                motors.command(65, Direction.FORWARD)
            elif ids == 8:
                motors.command(65, Direction.BACKWARD)
            elif ids == 5:
                motors.command(65, Direction.LEFT)
            elif ids == 3:
                motors.command(65, Direction.RIGHT)
                
            '''cv2.aruco.drawDetectedMarkers(img, corners, ids)
            #rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(corners, MARKER_SIDE, camera_matrix, camera_distortion)
            print(tvecs[0])
            cv2.aruco.drawAxis(img, camera_matrix, camera_distortion, rvecs[0], tvecs[0], 0.1)
            cv2.imshow("demo", img)'''
        #cv2.imwrite(f"turn_around_blurred/{i}.jpg", img)
        keypress = cv2.pollKey() & 0xFF
        if keypress == ord('q'):
            cam.flash_off()
            break


if __name__ == "__main__":

    main()