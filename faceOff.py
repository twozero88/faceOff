import cv2
import sys
import datetime as dt
from time import sleep

try:
    with open('config','r') as f:
        data = f.read()
except:
    input('You need to run setup.py first')
    exit()

print('Starting...')
timeOut = int(data.split('\n')[0])
sleepCt = 0
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
video_capture = cv2.VideoCapture(0)



def turnOffDisplay():
    if sys.platform.startswith('linux'):
        import os
        os.system("xset dpms force off")

    elif sys.platform.startswith('win'):
        import win32gui
        import win32con
        from os import getpid, system
        from threading import Timer
        
        def force_exit():
            pid = getpid()
            system('taskkill /pid %s /f' % pid)
        
        t = Timer(1, force_exit)
        t.start()
        SC_MONITORPOWER = 0xF170
        win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, SC_MONITORPOWER, 2)
        t.cancel()

    elif sys.platform.startswith('darwin'):
        import subprocess
        subprocess.call('echo \'tell application "Finder" to sleep\' | osascript', shell=True)

while True:
    sleep(5)
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    # To turnOff display
    if len(faces)==0:
        sleepCt += 1
        sleep(1)
        print(sleepCt)
        if sleepCt > timeOut:
            print("Turning off Display")
            turnOffDisplay()
    if len(faces)!=0:
        sleepCt=0
    # ends
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    if data.split('\n')[2].lower() == 'y':
        cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
