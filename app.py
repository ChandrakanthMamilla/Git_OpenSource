from flask import Flask
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route("/", methods=["GET"])
def welcome():
    return "Hello World"

if __name__ == "__main__":
    app.run()