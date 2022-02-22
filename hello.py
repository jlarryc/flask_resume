from flask import Flask, render_template
# export FLASK_APP=hello.py
# export FLASK_ENV=development

app = Flask(__name__)


# Create Index Page
msg = 2
@app.route('/') 
def index():
#	first_name = "Joe Bob" #input("Enter your name:")
#	favorite_pizza = ["Pepperoni", "Cheese", "Supreme", "Mushroom"]
#	if msg == 1:
#		return "Hello World! How Are You!!!! Doing Now"
#	else:
#		return render_template('index.html',f_name = first_name, pizza = favorite_pizza)
	return render_template('index.html')


# Create About Page
@app.route('/about')
def about():
	return render_template('about.html')


