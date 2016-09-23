from flask import render_template
from app import app

@app.route('/')
def index():
	return render_template('index.html')

# 연습문제
@app.route('/practice')
def practice():
	return render_template('practice.html')

@app.route('/practice01')
def practice01():
	return render_template('practice01.html')

@app.route('/practice02')
def practice02():
	return render_template('practice02.html')

@app.route('/practice02-2')
def practice02_2():
	return render_template('practice02-2.html')

# 실험
@app.route('/exp1_intro')
def exp1_intro():
	return render_template('exp1_intro.html')

@app.route('/exp2_intro')
def exp2_intro():
	return render_template('exp2_intro.html')
