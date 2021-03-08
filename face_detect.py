#! /usr/bin/python3


import cv2
import time
import os


def open_camera():
    path = 'haarcascade_frontalface_default.xml'
    video = cv2.VideoCapture(0)
    cascade = cv2.CascadeClassifier(cv2.data.haarcascades + path) 
    while(True):
        try:
            return_code,frame = video.read()
            grey_image = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces = cascade.detectMultiScale(grey_image,1.1)
            for x,y,w,h in faces:
                rect = cv2.rectangle(grey_image,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.imshow("video",rect)
            if cv2.waitKey(2) &0xFF  == ord('e'):
                break
        except KeyboardInterrupt:
            print()
            print("Exiting..")
            time.sleep(1)
            os.sys.exit(0)
    video.release()
    cv2.destroyAllWindows()
    

def main():
    if __name__ == "__main__":
        print("Starting...")
        time.sleep(1)
        open_camera()

main()