# Using flask to make an api 
# import necessary libraries and functions 
from main import *
from flask import Flask, jsonify, request 
  
# creating a Flask app 
app = Flask(__name__) 
  
# returns hello world when we use GET. 
# returns the data that we send when we use POST. 
@app.route('/checkStatus', methods = ['GET']) 
def home(): 
    if(request.method == 'GET'): 
        data = "System is LIVE!"
        return jsonify({'data': data}) 
  
  
# A simple function to calculate the square of a number 
# the number to be squared is sent in the URL when we use GET 
# on the terminal type: curl http://127.0.0.1:5000 / home / 10 
# this returns 100 (square of 10) 
@app.route('/waterPlants/<int:seconds>', methods = ['GET']) 
def disp(seconds): 
    waterPlants(seconds)
    return jsonify({'data': 'waterring the plants for' + str(seconds)}) 


@app.route('/blinkFor/<int:times>', methods = ['GET']) 
def blink(times): 
    blinkFor(times)
    return jsonify({'data': 'Blinking Light for' + str(times)}) 
  
  
# driver function 
if __name__ == '__main__': 
  
    app.run(debug = True, port=8080, host='0.0.0.0')