# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 09:19:22 2019

@author: beggr
"""
from keras.models import Sequential,Model,load_model
import cv2
#import os
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image
import tensorflow as tf

graph=tf.get_default_graph()

nogizaka_categories=["akimotomanatu","etoumisa","higutihina","horimiona","hosinominami","ikutaerika","inouesayuri",
            "itoujunnna","itouriria","iwamotorennka","kitanohinako","matumurasayuri","mukaihaduki","nakadakana",
            "nakamurareno","nisinonanase","oozonomomoko","saitouasuka","saitouyuuri","sakaguchitamami","sakuraireika",
            "sasakikotoko","satoukaede","sinnuchimai","siraisimai","suzukiayane","takayamakazumi",
            "teradarannze","umezawaminami","yamasitamiduki"]

hinatazaka_categories=["hamagisihiyori","higasimuramei","igutimao","kageyamayuuka","kakizakimemi","kanemuramiku",
            "katousiho","kawatahina","kosakanao","matudakonoka","nibuakari","saitoukyouko",
            "sasakikumi","sasakimirei","takamotoayaka","takasemana","tomitasuzuka","usiosarina","watanabemiho"]

keyakizaka_categories=["habumiduho","haradaaoi","hirateyurina","isimorinijika","kobayasiyui","koikeminami",
            "moriyaakane","nagahamaneru","nagasawananako","odanana","saitouhuyuka","satousiori","sugaiyuuka",
            "suzumotomiyu","uemurarina","watanaberika","watanaberisa"]

 

def face(image_path):
    image=cv2.imread(image_path)
    image_gs=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    cascade=cv2.CascadeClassifier(r"C:\Users\beggr\Anaconda3\pkgs\libopencv-3.4.1-h875b8b8_3\Library\etc\haarcascades\haarcascade_frontalface_alt.xml")
    face_list = cascade.detectMultiScale(image_gs,scaleFactor=1.1,minNeighbors=1,minSize=(100,100))
    
    if len(face_list)>0:
        for rect in face_list:
            image_gs_face = image[rect[1]:rect[1]+rect[3],rect[0]:rect[0]+rect[2]]
            return cv2.imwrite(r"C:\Users\beggr\OneDrive\python_machine\flask_API\goal\1.jpg", image_gs_face)
    else:
        return cv2.imwrite(r"C:\Users\beggr\OneDrive\python_machine\flask_API\goal\1.jpg", image_gs)



def nogizaka_model():
    model=load_model("C:\\Users\\beggr\\Downloads\\all7_model.h5")
    return model

def hinatazaka_model():
    model=load_model(r"C:\Users\beggr\Downloads\hinata2_model.h5")
    return model

def keyakizaka_model():
    model=load_model(r"C:\Users\beggr\Downloads\keyaki2_model.h5")
    return model

    
def nogizaka(image_path):
    global graph
    
    
    with graph.as_default():
        face(image_path)
        image=Image.open(r"C:\Users\beggr\OneDrive\python_machine\flask_API\goal\1.jpg")
        image=image.convert("RGB")
        image=image.resize((114,114))
        data=np.asarray(image)/255.0
        X=[]
        X.append(data)
        X=np.array(X)
        model=nogizaka_model()
        result=model.predict([X])[0]
        predicted=result.argmax()
        percentage=int(result[predicted] * 100)
    
        return nogizaka_categories[predicted], str(percentage)
        
def hinatazaka(image_path):
    global graph
    
    with graph.as_default():
        face(image_path)
        image=Image.open(r"C:\Users\beggr\OneDrive\python_machine\flask_API\goal\1.jpg")
        image=image.convert("RGB")
        image=image.resize((114,114))
        data=np.asarray(image)/255.0
        X=[]
        X.append(data)
        X=np.array(X)
        model=hinatazaka_model()
        result=model.predict([X])[0]
        predicted=result.argmax()
        percentage=int(result[predicted] * 100)
    
        return nogizaka_categories[predicted], str(percentage)
    
    
    
    
def keyakizaka(image_path):
    global graph
    
    with graph.as_default():
        face(image_path)
        image=Image.open(r"C:\Users\beggr\OneDrive\python_machine\flask_API\goal\1.jpg")
        image=image.convert("RGB")
        image=image.resize((114,114))
        data=np.asarray(image)/255.0
        X=[]
        X.append(data)
        X=np.array(X)
        model=keyakizaka_model()
        result=model.predict([X])[0]
        predicted=result.argmax()
        percentage=int(result[predicted] * 100)
    
        return nogizaka_categories[predicted], str(percentage)
    

        
