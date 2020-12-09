###########################################################################
# READING QR CODE SHOWN ON THE CAMERA AND DETECTING THE TEXT ON THE SCREEN
###########################################################################
# CODE STARTED FROM HERE AND IMPORTING ESSENTIALS FROM PYTHON LIBRARY
###########################################################################
# UNUSED MODULES
# import numpy as np
###########################################################################

import cv2
import pyzbar.pyzbar as pyzbar
import pyautogui

img = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

def MainFunc():
    while True:
        if pyautogui.keyDown('c'):
            return False
        _, frame = img.read()
        # cv2.addText("Sachin Accharya")
        decodedObjects = pyzbar.decode(frame)
        for obj in decodedObjects:
            output =f'''Output: {str(obj.data).split("'")[1]}'''
            cv2.putText(frame, output, (50, 50), font, 1, (255, 0, 0), 1)
        cv2.imshow("Output Video", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break