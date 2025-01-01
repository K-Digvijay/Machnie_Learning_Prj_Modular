from flask import Flask
from SRC.logger import logging
from SRC.exception import CustomException
import os,sys

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():
    try:
        raise Exception("we are testing our Exception File")
    
    except Exception as e:
        ML = CustomException(e,sys)
        logging.info(ML.error_message)
        logging.info("We are testing Logging file")

        return "Welcome to the New Application"

if __name__ == '__main__':
    app.run(debug=True)