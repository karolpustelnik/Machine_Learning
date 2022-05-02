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
    def detect_color():
        connection.keep_stream_alive()
        cam.flash_on()
        img = cam.get_frame()
        img = cam.get_frame()
        img = cam.get_frame()
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower_green = np.array([50, 50,50])
        upper_green = np.array([70, 255, 255])
        cv2.imwrite(f'./images/photo{0}.png', img)
        mask1 = cv2.inRange(hsv, lower_green, upper_green)
        lower_red = np.array([0,50,50])
        upper_red = np.array([10,255,255])
        mask2 = cv2.inRange(img, lower_red, upper_red)
        cv2.imwrite(f'./images/photo{1}.png', mask1)
        cv2.imwrite(f'./images/photo{2}.png', mask2)
        print(np.mean(mask1))
        print(np.mean(mask2))
        if np.mean(mask2) > 3.5:
            id_list.append(6)
            basket = 0.08
        if np.mean(mask1) > 3.2:
            id_list.append(8)
            basket = 0.08
        else:
            basket = 0
        cam.flash_off()
        return basket


    def pick_up():
        for pos in range(1000,1901,10):
            motors.command_servo(pos)
            time.sleep(0.05)
    def pick_up_basket():
            time.sleep(0.5)
            for i in range(17):
                motors.command(62, Direction.FORWARD)
                time.sleep(0.5)
            time.sleep(1)
            pick_up()
            for i in range(17):
                time.sleep(0.1)
                motors.command(62, Direction.BACKWARD)
                time.sleep(0.1)
                motors.command(62, Direction.RIGHT)


    def release():
        for pos in reversed(range(1000,1901,10)):
            motors.command_servo(pos)
            time.sleep(0.05)
    def release_basket():
        release()
        time.sleep(1)
        for i in range(15):
            motors.command(65, Direction.BACKWARD)
            time.sleep(0.1)

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

    def look_at_center(tvecs, p, basket = 0):
        cam.flash_on()
        position = 'incorrect'
        while position == 'incorrect':
            img, corners, rvecs, tvecs, ids = get_vecs()
            cv2.imshow("demo", img)
            print(ids)
            if isinstance(ids,np.ndarray):
                if tvecs[0][0][0] < -p + basket:
                    motors.command(61, Direction.LEFT)
                elif tvecs[0][0][0] > p + basket:
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
    def finish(stop):
        cam.flash_on()
        position = 'incorrect'
        while position == 'incorrect':
            img, corners, rvecs, tvecs, ids = get_vecs()
            cv2.imshow("demo", img)
            if ids != None:
                if tvecs[0][0][2] > stop:
                    look_at_center(tvecs, 0.03, basket)
                    motors.command(62, Direction.FORWARD)
                else:
                    position = 'correct'
                    cam.flash_off()
    cv2.namedWindow("demo")
    connection = Connection()
    cam = Camera(connection=connection)
    motors = Motors(connection=connection)
    id_list = [3]
    release()
    basket = 0
    angle = 8
    stop = 0.2
    status = 'notdone'
    while status == 'notdone':
        for id in id_list:
            print(id)
            ids = None
            while ids != id :
                cam.flash_on()
                img, corners, rvecs, tvecs, ids = get_vecs()
                print(ids)

                hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                lower_green = np.array([50, 50,50])
                upper_green = np.array([70, 255, 255])
                lower_red = np.array([0,50,50])
                upper_red = np.array([10,255,255])
                mask1 = cv2.inRange(hsv, lower_green, upper_green)
                mask2 = cv2.inRange(hsv, lower_red, upper_red)
                print(np.mean(mask1))
                print(np.mean(mask2))
                if ids == 3:
                    if np.mean(mask2) > 5:
                        id_list.append(6)
                        basket = 0.05
                    if np.mean(mask1) > 5:
                        id_list.append(8)
                        basket = 0.05
                if ids == 6 or ids == 8:
                        angle = 20
                        basket = -0.05
                        stop = 0.25
                motors.command(61, Direction.RIGHT)
            cam.flash_off()
            print(id_list)
            get_closer()
            look_at_center(tvecs, 0.03)
            pitch = R.from_rotvec(rvecs[0]).as_euler('zyx')[0][1]
            pitch_degree = math.degrees(pitch)
            if abs(pitch_degree)>angle:
                print(pitch_degree)
                for i in range(round(((math.pi/2)-pitch)/0.5)):
                        if pitch_degree > 0:
                            motors.command(65, Direction.RIGHT)
                            time.sleep(0.5)
                        else:
                            motors.command(65, Direction.LEFT)
                            time.sleep(0.5)

                time.sleep(0.5)
                print(abs(round((100*(np.cos((math.pi/2)-pitch)*abs(tvecs[0][0][2]))/0.4))))
                for i in range(abs(round((100*(np.cos(math.pi/2-pitch)*abs(tvecs[0][0][2]))/4)))):
                        motors.command(80, Direction.FORWARD)
                        time.sleep(0.5)
                time.sleep(0.5)
                if pitch_degree > 0:
                    for i in range(7):
                                motors.command(65, Direction.LEFT)
                                time.sleep(0.5) 
                if pitch_degree < 0:
                    for i in range(5):
                            motors.command(65, Direction.RIGHT)
                            time.sleep(0.5) 
                
                time.sleep(0.5)
                look_at_center(tvecs, 0.05, basket)
                time.sleep(0.5)
                print(basket)
                finish(stop)
                if id == 3:
                    pick_up_basket()
                else:
                    release_basket()
                    status = 'done'
                    break
            else:
                time.sleep(0.5)
                look_at_center(tvecs, 0.05, basket)
                time.sleep(0.5)
                print(basket)
                finish(stop)
                if id == 3:
                    pick_up_basket()
                else:
                    release_basket()
                    status = 'done'
                    break
                
        


if __name__ == "__main__":

    main()

# motors.command(80, Direction.FORWARD) ok. 6cm

#motors.command(65, Direction.LEFT) 39 oborotów = 360

