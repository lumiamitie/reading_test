from flask import render_template
from app import app

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/practice')
def practice():
	return render_template('practice.html')

@app.route('/practice01')
def practice01():
	return render_template('practice01.html')