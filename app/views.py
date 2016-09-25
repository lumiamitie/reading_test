from flask import render_template, redirect, url_for, request, flash
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

# 실험1
# @app.route('/exp1/intro')
# def exp1_intro():
#     return render_template('exp1_intro.html')

@app.route('/exp1/intro')
def exp1_intro():
    test_no = 1
    test_type = ['스크롤', '페이지']
    next_page = '/exp1/a1/scroll'
    return render_template('exp_intro.html', test_no=test_no, test_type=test_type, next_page=next_page)

@app.route('/exp1/a1/scroll')
def exp1_a1_scroll():
    next_page = '/exp1/a2/scroll'
    return render_template('a1_scroll.html', next_page=next_page)

@app.route('/exp1/a2/scroll')
def exp1_a2_scroll():
    next_page = '/exp1/a3/scroll'
    return render_template('a2_scroll.html', next_page=next_page)

@app.route('/exp1/a3/scroll')
def exp1_a3_scroll():
    next_page = '/exp1/rest'
    return render_template('a3_scroll.html', next_page=next_page)

@app.route('/exp1/rest')
def exp1_rest():
    # return render_template('rest_scroll.html')
    test_type = ['스크롤', '페이지']
    next_page = '/exp1/b1/page'
    return render_template('rest.html', test_type=test_type, next_page=next_page)

@app.route('/exp1/b1/page')
def exp1_b1_page():
    next_page = '/exp1/b2/page'
    return render_template('b1_page.html', next_page=next_page)

@app.route('/exp1/b2/page')
def exp1_b2_page():
    next_page = '/exp1/b3/page'
    return render_template('b2_page.html', next_page=next_page)

@app.route('/exp1/b3/page')
def exp1_b3_page():
    next_page = '/exp1/outro'
    return render_template('b3_page.html', next_page=next_page)

@app.route('/exp1/outro')
def exp1_outro():
    test_no = 1
    return render_template('exp_outro.html', test_no=test_no)


# 실험2
# @app.route('/exp2/intro')
# def exp2_intro():
#     return render_template('exp2_intro.html')

@app.route('/exp2/intro')
def exp2_intro():
    test_no = 2
    test_type = ['페이지', '스크롤']
    next_page = '/exp2/a1/page'
    return render_template('exp_intro.html', test_no=test_no, test_type=test_type, next_page=next_page)

@app.route('/exp2/a1/page')
def exp2_a1_page():
    next_page = '/exp2/a2/page'
    return render_template('a1_page.html', next_page=next_page)

@app.route('/exp2/a2/page')
def exp2_a2_page():
    next_page = '/exp2/a3/page'
    return render_template('a2_page.html', next_page=next_page)

@app.route('/exp2/a3/page')
def exp2_a3_page():
    next_page = '/exp2/rest'
    return render_template('a3_page.html', next_page=next_page)

@app.route('/exp2/rest')
def exp2_rest():
    test_type = ['페이지', '스크롤']
    next_page = '/exp2/b1/scroll'
    # return render_template('rest_page.html', next_page=next_page)
    return render_template('rest.html', test_type=test_type, next_page=next_page)

@app.route('/exp2/b1/scroll')
def exp2_b1_scroll():
    next_page = '/exp2/b2/scroll'
    return render_template('b1_scroll.html', next_page=next_page)

@app.route('/exp2/b2/scroll')
def exp2_b2_scroll():
    next_page = '/exp2/b3/scroll'
    return render_template('b2_scroll.html', next_page=next_page)

@app.route('/exp2/b3/scroll')
def exp2_b3_scroll():
    next_page = '/exp2/outro'
    return render_template('b3_scroll.html', next_page=next_page)

@app.route('/exp2/outro')
def exp2_outro():
    test_no = 2
    return render_template('exp_outro.html', test_no=test_no)


# 실험3
@app.route('/exp3/intro')
def exp3_intro():
    test_no = 3
    test_type = ['스크롤', '페이지']
    next_page = '/exp3/b1/scroll'
    return render_template('exp_intro.html', test_no=test_no, test_type=test_type, next_page=next_page)

# 지문 B (스크롤)
@app.route('/exp3/b1/scroll')
def exp3_b1_scroll():
    next_page = '/exp3/b2/scroll'
    return render_template('b1_scroll.html', next_page=next_page)

@app.route('/exp3/b2/scroll')
def exp3_b2_scroll():
    next_page = '/exp3/b3/scroll'
    return render_template('b2_scroll.html', next_page=next_page)

@app.route('/exp3/b3/scroll')
def exp3_b3_scroll():
    next_page = '/exp3/rest'
    return render_template('b3_scroll.html', next_page=next_page)

# 휴식
@app.route('/exp3/rest')
def exp3_rest():
    test_type = ['스크롤', '페이지']
    next_page = '/exp3/a1/page'
    return render_template('rest.html', test_type=test_type, next_page=next_page)

# 지문 A (페이지)
@app.route('/exp3/a1/page')
def exp3_a1_page():
    next_page = '/exp3/a2/page'
    return render_template('a1_page.html', next_page=next_page)

@app.route('/exp3/a2/page')
def exp3_a2_page():
    next_page = '/exp3/a3/page'
    return render_template('a2_page.html', next_page=next_page)

@app.route('/exp3/a3/page')
def exp3_a3_page():
    next_page = '/exp3/outro'
    return render_template('a3_page.html', next_page=next_page)

# 실험3 outro
@app.route('/exp3/outro')
def exp3_outro():
    test_no = 3
    return render_template('exp_outro.html', test_no=test_no)



# 실험4 intro
@app.route('/exp4/intro')
def exp4_intro():
    test_no = 4
    test_type = ['페이지', '스크롤']
    next_page = '/exp4/b1/page'
    return render_template('exp_intro.html', test_no=test_no, test_type=test_type, next_page=next_page)

@app.route('/exp4/b1/page')
def exp4_b1_page():
    next_page = '/exp4/b2/page'
    return render_template('b1_page.html', next_page=next_page)

@app.route('/exp4/b2/page')
def exp4_b2_page():
    next_page = '/exp4/b3/page'
    return render_template('b2_page.html', next_page=next_page)

@app.route('/exp4/b3/page')
def exp4_b3_page():
    next_page = '/exp4/rest'
    return render_template('b3_page.html', next_page=next_page)

# 휴식
@app.route('/exp4/rest')
def exp4_rest():
    test_type = ['페이지', '스크롤']
    next_page = '/exp4/a1/scroll'
    return render_template('rest.html', test_type=test_type, next_page=next_page)


@app.route('/exp4/a1/scroll')
def exp4_a1_scroll():
    next_page = '/exp4/a2/scroll'
    return render_template('a1_scroll.html', next_page=next_page)

@app.route('/exp4/a2/scroll')
def exp4_a2_scroll():
    next_page = '/exp4/a3/scroll'
    return render_template('a2_scroll.html', next_page=next_page)

@app.route('/exp4/a3/scroll')
def exp4_a3_scroll():
    next_page = '/exp4/outro'
    return render_template('a3_scroll.html', next_page=next_page)

# 실험4 outro
@app.route('/exp4/outro')
def exp4_outro():
    test_no = 4
    return render_template('exp_outro.html', test_no=test_no)



# 설문 페이지
@app.route('/survey', methods = ['GET', 'POST'])
def survey():
    # outro 페이지에서 실험번호를 받아온다
    # 혹시라도 값이 없을경우에는 빈칸으로
    test_no = request.args.get('test_no', '')

    if request.method == 'POST':
        print(request.form)
        # 설문이 완료되면 완료페이지로 보낸다
        if len(request.form) == 6:
            return redirect(url_for('complete'))
        # 텍스트박스는 항상 POST로 전달되는 것 같다
        # 따라서 기본값으로 오는 경우에는 flash를 띄우지 않도록 한다
        elif len(request.form) == 2 and request.form['survey03'] == '' and request.form['survey06'] == '':
            pass
        # 설문을 완료하지 않은 경우 메세지를 띄운다
        else:
            flash('모든 항목의 설문을 완료해주세요')
    return render_template('survey.html')

# 실험종료 페이지
@app.route('/complete')
def complete():
    return render_template('complete.html')