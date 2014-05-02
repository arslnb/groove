import sys
import os
from flask import Flask
app = Flask(__name__)

if sys.platform == "darwin":

	local = os.path.join(os.path.expanduser('~'), 'Groove/Local')
	shared = os.path.join(os.path.expanduser('~'), 'Groove/Shared')

	if not os.path.isdir(local) and not os.path.isdir(shared):
		os.makedirs(local)
		os.makedirs(shared)
		print "OS X Directory"
	else: 
		print "Welcome Back!"

elif sys.platform == "win32":
	print "Windows Directory"
	print "I'll add support for this soon."

@app.route("/")
def hello():
	return "success"

if __name__ == "__main__":
    app.run()