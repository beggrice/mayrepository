# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:40:14 2019

@author: beggr
"""
import flask
from flask import Flask, render_template,request,redirect,url_for
import json

app=Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    
    
    if request.method=="POST":
        title=request.form["title"]
        user=request.form["user"]
    else:
        title="no"
        user="no"
        
    response={"title:":title,
              "user:":user
                              }
    
    
    
    
        
    return flask.jsonify(response)

if __name__=="__main__":
    app.debug=True
    app.run()    