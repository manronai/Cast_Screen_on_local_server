# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 18:57:44 2019
@author: seraj
"""
import time
import cv2
from flask import Flask, render_template, Response
from PIL import ImageGrab
import cv2, numpy as np

app = Flask(__name__)


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen():
    """Video streaming generator function."""
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    # Read until video is completed
    while (cap.isOpened()):
        # Capture frame-by-frame
        #f = ImageGrab.grab(bbox=(21, 32, 1341, 596))
        f = ImageGrab.grab()
        img = np.array(f)
        #ret, img = cap.read()
        if True == True:
            img = cv2.resize(img, (0, 0), fx=0.73, fy=0.75)
            frame = cv2.imencode('.jpg', img)[1].tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            #time.sleep(0.1)
        else:
            break


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
app.run(host='192.168.0.104', port=5555,debug=True, threaded=True)