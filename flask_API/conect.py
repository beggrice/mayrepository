# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 23:08:35 2019

@author: beggr
"""

import requests


picture=open(r"C:\Users\beggr\Downloads\testing\3.bmp","rb")


response=requests.post("http://127.0.0.1:5000/predict/nogizaka",files={"img_file":picture})
picture.close()
print(response.status_code)
print(response.text)
