''' Short demo to build abasic app '''

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'