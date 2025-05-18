from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return "Come and kiss me on my hot mouth, i'm feeling romentical."
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
