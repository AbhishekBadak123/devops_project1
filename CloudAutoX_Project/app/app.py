
from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>CloudAutoX Application</h1>
    <p>Running inside Kubernetes</p>
    <p>Pod Hostname: {socket.gethostname()}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
