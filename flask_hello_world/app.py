# ---- Flask Hello World ---- #

# import the Flask class from the flask module
from flask import Flask

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route("/")
@app.route("/hello")
def hello_world():
	return "Hello, World!"

# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
	return search_query

# integer route
@app.route("/integer/<int:value>")
def int_type(value):
	print value + 1
	return "correct"

# float route
@app.route("/float/<float:value>")
def float_type(value):
	print value + 1
	return "correct"

# dynamic route that accepts slashes
@app.route("/path/<path:value>")
def path_type(value):
	print value
	return "correct"

# view to test HTTP response codes
@app.route("/name/<name>")
def index(name):
	if name.lower() == "eric":
		return "Hello, {}".format(name.capitalize()), 200
	else:
		return "Not Found", 404

# starts the development server using the run() method
if __name__ == "__main__":
	app.run()
