#!/usr/bin/env python3

from operator import le
import cv2
import time
import numpy as np
import math
from scipy.spatial.transform import Rotation as R


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
    ## przydatne funckje
    def get_vecs():
            cam.flash_on()
            connection.keep_stream_alive()
            img = cam.get_frame()
            img = cv2.remap(img, map1, map2, cv2.INTER_LINEAR)
            cv2.imshow("demo", img)
            corners, ids, _ = cv2.aruco.detectMarkers(img, dictionary = dictionary, parameters = detectorParams)
            rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(corners, MARKER_SIDE, rect_camera_matrix, 0)
            return img, corners, rvecs, tvecs, ids

    def look_at_center(tvecs, p):
        cam.flash_on()
        position = 'incorrect'
        while position == 'incorrect':
            img, corners, rvecs, tvecs, ids = get_vecs()
            cv2.imshow("demo", img)
            if ids != None:
                if tvecs[0][0][0] < -p:
                    motors.command(61, Direction.LEFT)
                elif tvecs[0][0][0] > p:
                    motors.command(61, Direction.RIGHT)
                else:
                    position = 'correct'
                    cam.flash_off()
    def get_closer():
        cam.flash_on()
        position = 'incorrect'
        while position == 'incorrect':
            img, corners, rvecs, tvecs, ids = get_vecs()
            cv2.imshow("demo", img)
            if ids != None:
                if tvecs[0][0][2] > 0.6:
                    look_at_center(tvecs, 0.07)
                    motors.command(70, Direction.FORWARD)
                else:
                    position = 'correct'
                    cam.flash_off()
    def finish():
        cam.flash_on()
        position = 'incorrect'
        while position == 'incorrect':
            img, corners, rvecs, tvecs, ids = get_vecs()
            cv2.imshow("demo", img)
            if ids != None:
                if tvecs[0][0][2] > 0.25:
                    look_at_center(tvecs, 0.03)
                    motors.command(70, Direction.FORWARD)
                else:
                    position = 'correct'
                    cam.flash_off()
    cv2.namedWindow("demo")
    connection = Connection()
    cam = Camera(connection=connection)
    motors = Motors(connection=connection)
    id_list = [3, 5, 6, 8]
    while True:
        for id in id_list:
            ids = None
            while ids != id :
                cam.flash_on()
                img, corners, rvecs, tvecs, ids = get_vecs()
                cv2.imshow("demo", img)
                print(ids)
                motors.command(61, Direction.RIGHT)
            cam.flash_off()
            get_closer()
            look_at_center(tvecs, 0.03)
            pitch = R.from_rotvec(rvecs[0]).as_euler('zyx')[0][1]
            pitch_degree = math.degrees(pitch)
            if abs(pitch_degree)>8:
                print(pitch_degree)
                for i in range(round(((math.pi/2)-pitch)/0.25)):
                        if pitch_degree > 0:
                            motors.command(65, Direction.RIGHT)
                            time.sleep(0.5)
                        else:
                            motors.command(65, Direction.LEFT)
                            time.sleep(0.5)

                time.sleep(1)
                print(abs(round((100*(np.cos((math.pi/2)-pitch)*abs(tvecs[0][0][2]))/5))))
                for i in range(abs(round((100*(np.cos(math.pi/2-pitch)*abs(tvecs[0][0][2]))/4)))):
                        motors.command(80, Direction.FORWARD)
                        time.sleep(0.5)
                time.sleep(1)
                if pitch_degree > 0:
                    for i in range(9):
                                motors.command(65, Direction.LEFT)
                                time.sleep(0.5) 
                if pitch_degree < 0:
                    for i in range(5):
                            motors.command(65, Direction.RIGHT)
                            time.sleep(0.5) 
                finish()
            else:
                finish()


            


        
            


        keypress = cv2.pollKey() & 0xFFa
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cam.flash_off()
            break
        if keypress == ord('w'):
            motors.command(80, Direction.FORWARD)
        if keypress == ord('s'):
            motors.command(80, Direction.BACKWARD)
        if keypress == ord('a'):
            motors.command(65, Direction.LEFT)
        if keypress == ord('d'):
            motors.command(65, Direction.RIGHT)
                        
                    #for rvec, tvec in zip(rvecs, tvecs):
                    #  cv2.aruco.drawAxis(img, rect_camera_matrix, 0, rvec, tvec, 0.1)
                    #cv2.imshow("demo", img)
                    #if tvecs[0][0][2]>0.2:
                    # motors.command(65, Direction.FORWARD)
                    # time.sleep(0.1)
                        #if rvecs[0][0][2]>0.4:
                        # motors.command(62, Direction.LEFT)
                        # time.sleep(0.1)
                    #cv2.imshow("demo", img)
        


if __name__ == "__main__":

    main()

# motors.command(80, Direction.FORWARD) ok. 6cm

#motors.command(65, Direction.LEFT) 39 oborotów = 360

