from flask import render_template, redirect, url_for
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

# 실험 끝난 이후 리다이렉트용
@app.route('/practice_finished')
def practice_finished():
	return redirect(url_for('index'))

# 실험
@app.route('/exp1/intro')
def exp1_intro():
	return render_template('exp1_intro.html')

@app.route('/exp2/intro')
def exp2_intro():
	return render_template('exp2_intro.html')

@app.route('/exp1/a1/scroll')
def exp1_a1_scroll():
	return render_template('a1_scroll.html')

@app.route('/exp1/a2/scroll')
def exp1_a2_scroll():
	return render_template('a2_scroll.html')

@app.route('/exp1/a3/scroll')
def exp1_a3_scroll():
	return render_template('a3_scroll.html')

@app.route('/exp1/rest')
def rest():
	return render_template('rest_scroll.html')