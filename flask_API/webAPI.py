# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 09:18:16 2019

@author: beggr
"""

import flask 
import numpy as np
from keras.models import load_model
from PIL import Image
import cv2
import os,re
from werkzeug import secure_filename
from classify import nogizaka,keyakizaka,hinatazaka




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


    
@app.route("/predict/nogizaka",methods=["POST"])
def predict_nogizaka():

    
    if flask.request.method=="POST":
        img_file=flask.request.files["img_file"]
        if img_file and allowed_file(img_file.filename):
            filename=img_file.filename
            img_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            img_url = 'C:\\Users\\beggr\\OneDrive\\python_machine\\flask_API\\uploads\\' + filename
            
            result, percentage=nogizaka(img_url)
            os.remove(img_url)
            os.remove(r"C:\Users\beggr\OneDrive\python_machine\flask_API\goal\1.jpg")
            
                
        else:
            result=''' <p>許可されていない拡張子です</p> '''
            percentage="no"
        
    else:
        result="no"
        percentage="no"
        
    response={
            "result":result,
            "percentage":percentage
            }
    
    return flask.jsonify(response)

@app.route("/predict/hinatazaka",methods=["POST"])
def predict_hinatazaka():
    if flask.request.method=="POST":
        img_file=flask.request.files["img_file"]
        if img_file and allowed_file(img_file.filename):
            filename=img_file.filename
            img_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            img_url = 'C:\\Users\\beggr\\OneDrive\\python_machine\\flask_API\\uploads\\' + filename
            
            result, percentage=hinatazaka(img_url)
            os.remove(img_url)
            os.remove(r"C:\Users\beggr\OneDrive\python_machine\flask_API\goal\1.jpg")
            
                
        else:
            result=''' <p>許可されていない拡張子です</p> '''
            percentage="no"
        
    else:
        result="no"
        percentage="no"
        
    response={
            "result":result,
            "percentage":percentage
            }
    
    return flask.jsonify(response)

@app.route("/predict/keyakizaka",methods=["POST"])
def predict_keyakizaka():
    if flask.request.method=="POST":
        img_file=flask.request.files["img_file"]
        if img_file and allowed_file(img_file.filename):
            filename=img_file.filename
            img_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            img_url = 'C:\\Users\\beggr\\OneDrive\\python_machine\\flask_API\\uploads\\' + filename
            
            result, percentage=keyakizaka(img_url)
            os.remove(img_url)
            os.remove(r"C:\Users\beggr\OneDrive\python_machine\flask_API\goal\1.jpg")
            
                
        else:
            result=''' <p>許可されていない拡張子です</p> '''
            percentage="no"
        
    else:
        result="no"
        percentage="no"
        
    response={
            "result":result,
            "percentage":percentage
            }
    
    return flask.jsonify(response)
    
    
    
if __name__ == "__main__":
    app.debug=True
    app.run()