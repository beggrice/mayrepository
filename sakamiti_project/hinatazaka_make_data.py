# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 18:44:49 2019

@author: beggr
"""

from PIL import Image
import os,glob
import numpy as np
import random,math
import cv2

root_dir="D:\\keyakizakaout\\"
categories=["out_habumiduho","out_haradaaoi","out_hirateyurina","out_isimorinijika","out_kobayasiyui","out_koikeminami",
            "out_moriyaakane","out_nagahamaneru","out_nagasawananako","out_odanana","out_saitouhuyuka","out_satousiori","out_sugaiyuuka",
            "out_suzumotomiyu","out_uemurarina","out_watanaberika","out_watanaberisa"]




nb_classes=len(categories)
image_size=128

X=[]
Y=[]

def data_append(data,cat):
    X.append(data)
    Y.append(cat)
    
def add_sample(cat,fname,is_train):
    img=Image.open(fname)
    img=img.convert("RGB")
    img=img.resize((image_size,image_size))
    data=np.asarray(img)
    X.append(data)
    Y.append(cat)
    if not is_train: 
        return
    filter1=np.ones((3,3))
    flip=lambda x: cv2.flip(x,1)
    thr=lambda x: cv2.threshold(x,100,255,cv2.THRESH_TOZERO)[1]
    filt=lambda x:cv2.GaussianBlur(x,(5,5),0)
    
    methods=[flip,thr,filt]
    
    for f in methods:
        processing_data=f(data)
        data_append(processing_data,cat)
        
    for f in methods[1:]:
        processing_data=flip(f(data))
        data_append(processing_data,cat)
        
    data_append(thr(filt(data)),cat)
    data_append(flip(thr(filt(data))),cat)
    
    
def make_sample(files,is_train):
    global X,Y
    X=[]; Y=[]
    for cat,fname in files:
        add_sample(cat,fname,is_train)
    return np.array(X),np.array(Y)
allfiles=[]
for idx,cat in enumerate(categories):
    image_dir=root_dir+"\\"+cat
    files=glob.glob(image_dir+"\*.jpg")
    for f in files:
        allfiles.append((idx,f))
print(len(allfiles))
        
random.shuffle(allfiles)
th=math.floor(len(allfiles)*0.8)
train=allfiles[0:th]
test=allfiles[th:]
X_train,y_train=make_sample(train,True)
X_test,y_test=make_sample(test,False)
print(len(X_train))
xy=(X_train,X_test,y_train,y_test)
np.save("D:\\train_test\\keyakiaobj.npy",xy)
print("ok",len(y_train))