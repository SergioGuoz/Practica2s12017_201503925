from flask import Flask
app=flask("Practica 2, EDD")

@app.route("/")
def hello():
	return "Hello World"

if __name__ == '__main__':
	app.run()