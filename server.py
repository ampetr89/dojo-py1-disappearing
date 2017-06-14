from flask import Flask, redirect, render_template

app = Flask(__name__)

secret_key = open('secret-key.txt', 'r').read().strip()
app.secret_key = secret_key

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/cities')
def cities():
	return render_template('cities.html')

@app.route('/cities/')
def cities1():
	return redirect('/cities')

@app.route('/cities/<city>')
def city(city):
	
	cities = {
		'new-york': {'name': 'New York', 'welcome':'Welcome!'},
		'cairo': {'name': 'New York', 'welcome':'أهلا وسهلا!'},
		'paris': {'name': 'New York', 'welcome':'Bienvenue!'},
		'rome':  {'name': 'New York', 'welcome':'Benvenuto!'}
	}
	if city in cities:
		return render_template('city.html',city=city, welcome=cities[city]['welcome'], cityname=cities[city]['name'])
	else:
		return redirect('/cities')

app.run(debug=True)