import sys
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    if sys.platform == "darwin":
    	return "Nice Mac"
    elif sys.platform == "cygwin":
    	return "Fuckin windows"

if __name__ == "__main__":
    app.run()