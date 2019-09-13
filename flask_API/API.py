# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 13:33:28 2019

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

categories=["akimotomanatu","etoumisa","higutihina","horimiona","hosinominami","ikutaerika","inouesayuri",
            "itoujunnna","itouriria","iwamotorennka","kitanohinako","matumurasayuri","mukaihaduki","nakadakana",
            "nakamurareno","nisinonanase","oozonomomoko","saitouasuka","saitouyuuri","sakaguchitamami","sakuraireika",
            "sasakikotoko","satoukaede","sinnuchimai","siraisimai","suzukiayane","takayamakazumi",
            "teradarannze","umezawaminami","yamasitamiduki"] 





UPLOAD_FOLDER ="C:\\Users\\beggr\\OneDrive\\python_machine\\flask_API\\uploads"
ALLOWED_EXTENSIONS = set(['jpg',"png","bmp","gif","PNG","JPG","jpeg"])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = os.urandom(24)

#アップロードを許可する画像ファイル
def allowed_file(filename):
    # ファイル名の拡張子より前を取得し, フォーマット後のファイル名に変更
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def build_model():
    
    model=load_model("C:\\Users\\beggr\\Downloads\\all7_model.h5")
    
    return model

def main(im):
    image=Image.fromarray(im)
    image=image.convert("RGB")
    image=image.resize((114,114))
    data=np.asarray(image)/255.0
    X=[]
    X.append(data)
    X=np.array(X)
    model=build_model()
    result=model.predict([X])[0]
    predicted=result.argmax()
    percentage=int(result[predicted] * 100)
    return ("{0} ({1} %)".format(categories[predicted], percentage))
    
@app.route("/predict",methods=["POST"])
def predict():

    
    if flask.request.method=="POST":
        img_file=flask.request.files["img_file"]
        if img_file and allowed_file(img_file.filename):
            filename=img_file.filename
            img_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            img_url = 'C:\\Users\\beggr\\OneDrive\\python_machine\\flask_API\\uploads\\' + filename
            
            image= cv2.imread(img_url)
            
            image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# 顔認識用特徴量ファイルを読み込む --- （カスケードファイルのパスを指定）
            cascade = cv2.CascadeClassifier(r"C:\Users\beggr\Anaconda3\pkgs\libopencv-3.4.1-h875b8b8_3\Library\etc\haarcascades\haarcascade_frontalface_alt.xml")
# 顔認識の実行
            face_list = cascade.detectMultiScale(image_gs,scaleFactor=1.1,minNeighbors=1,minSize=(100,100))
 
#顔が１つ以上検出された時
            if len(face_list) > 0:
                for rect in face_list:
                    image_gs = image[rect[1]:rect[1]+rect[3],rect[0]:rect[0]+rect[2]]
                im=image_gs
                predict=main(im)
                
                
                
            else:
                predict="no face"
                
        else:
            predict=''' <p>許可されていない拡張子です</p> '''
        
    else:
        predict="no"
        
    response={"result":predict}
    
    return flask.jsonify(response)
    
    
    
if __name__ == "__main__":
    app.debug=True
    app.run()
                

            
            
