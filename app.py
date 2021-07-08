from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!  Vinay here ... Very good learning."
