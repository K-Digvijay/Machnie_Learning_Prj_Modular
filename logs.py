from flask import Flask
from SRC.logger import logging

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():
    logging.info("We are testing Logging file")

    return "Welcome to the New Application"

if __name__ == '__main__':
    app.run(debug=True)