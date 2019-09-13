# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 00:03:36 2019

@author: beggr
"""

import flask 
import numpy as np
from keras.models import load_model
from PIL import Image
import cv2
import os,re
from werkzeug import secure_filename




app = flask.Flask(__name__)







UPLOAD_FOLDER ="C:\\Users\\beggr\\OneDrive\\python_machine\\flask_API\\uploads"
ALLOWED_EXTENSIONS = set(['jpg',"png","bmp","gif","PNG","JPG","jpeg"])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = os.urandom(24)

#アップロードを許可する画像ファイル
def allowed_file(filename):
    # ファイル名の拡張子より前を取得し, フォーマット後のファイル名に変更
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS



    
@app.route("/predict",methods=["POST"])
def predict():

    
    if flask.request.method=="POST":
        img_file=flask.request.files["img_file"]
        if img_file and allowed_file(img_file.filename):
            filename=img_file.filename
        else:
            filename="no"
    else:
        filename="no"
            
            
            
 

        
    response={"result":filename}
    
    return flask.jsonify(response)
    
    
    
if __name__ == "__main__":
    app.debug=True
    app.run()
                

            
            
