# -*- coding: utf-8 -*-
import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

in_jpg=("D:\\nogizaka\\satoukaede\\")
out_jpg=("D:\\nogizaka\\out_satoukaede\\")


def get_file(dir_path):
    filenames=os.listdir(dir_path)
    return filenames
pic=get_file(in_jpg)

for i in pic:
    image=cv2.imread(in_jpg+i)
    image_gs=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade=cv2.CascadeClassifier(r"C:\Users\beggr\Anaconda3\pkgs\libopencv-3.4.2-h20b85fd_0\Library\etc\haarcascades\haarcascade_frontalface_alt.xml")
    face_list=cascade.detectMultiScale(image_gs,scaleFactor=1.1,minNeighbors=2,minSize=(30,30))
                                                                                    

    no=1;   
    for rect in face_list:
        x=rect[0]
        y=rect[1]
        width=rect[2]
        height=rect[3]
        dst=image[y:y+height,x:x+width]
        save_path=out_jpg+"\\"+"out_("+str(i)+")"+str(no)+".jpg"
        a=cv2.imwrite(save_path,dst)
        print(no)
        no=no+1
        