from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	file = open("/etc/data/hello.txt", "r")
	return file.read()
