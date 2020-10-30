from flask import Flask 


app=Flask(__name__)


@app.route("/")
def home():
	return "welcome to Azure DevOps thru  python"

@app.route("/hello")
def hello():
	return "hell azure devops"



if __name__   == "__main__" :
	app.run(ssl_context='adhoc',
host='0.0.0.0',port=91)

