from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

def lwphone():
    return "LW Phone Function"


app.run(host="0.0.0.0")
