# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 01:13:12 2020

@author: Abhishek Tripathi
"""

import flask
from flask import request, render_template,send_file
import base64
import cv2

app = flask.Flask(__name__)
@app.route("/")
def viz_page():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':  
        f = request.files['image']
        print('saving the uploaded image ')
        f.save('temp/' + '1.jpg')
        #img = ms.serviceImage1()
        #cv2.imwrite('temp/1.jpg',img)
        image = cv2.imread('temp/1.jpg')
        gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print('image 1 read ')
        _, img_encoded = cv2.imencode('.jpg', gray)
        print('sending data back')
        return base64.b64encode(img_encoded)

if __name__ == '__main__':
    app.run(port=8080,debug=False, threaded=False)