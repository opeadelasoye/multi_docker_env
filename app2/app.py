from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello():
	resp = requests.get("http://app1:5000")
	return resp.text
