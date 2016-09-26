from flask import render_template, redirect, url_for, request, flash, session, g
from app import app
from uuid import uuid4
import datetime

# 현재 시각을 문자열로 반환
def current_time():
    c_time = datetime.datetime.now()
    return c_time.strftime('%Y-%m-%d %H:%M:%S')


import MySQLdb
@app.before_request
def before_request():
    # g.db = MySQLdb.connect(user="miika", passwd="minho1234", db="reading_test", charset='utf8',
    #                        cursorclass=MySQLdb.cursors.DictCursor)
    g.db = MySQLdb.connect('miika.mysql.pythonanywhere-services.com','miika','minho1234',"miika$reading_test")

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


def insert_answer(dict_values):
    query = '''INSERT INTO answer_log (uuid, exp_id, test_type, question, answer_value, is_real_test)
               VALUES ('{uuid}', '{exp_id}', '{test_type}', '{question}', {answer_value}, '{is_real}');'''
    return query.format(uuid=dict_values['uuid'],
                        exp_id=dict_values['exp_id'],
                        test_type=dict_values['test_type'],
                        question=dict_values['question'],
                        answer_value=dict_values['answer_value'],
                        is_real=dict_values['is_real'])

def insert_time(dict_values):
    query = '''INSERT INTO time_log (uuid, exp_id, test_type, question, category, time, is_real_test)
               VALUES ('{uuid}', '{exp_id}', '{test_type}', '{question}', '{category}', '{time}', '{is_real}');'''
    return query.format(uuid=dict_values['uuid'],
                        exp_id=dict_values['exp_id'],
                        test_type=dict_values['test_type'],
                        question=dict_values['question'],
                        category=dict_values['category'],
                        time=dict_values['time'],
                        is_real=dict_values['is_real'])

def insert_survey(dict_values):
    query = '''INSERT INTO survey (uuid, exp_id, survey01, survey02, survey03, survey04, survey05, survey06, end_time, is_real_test) VALUES ('{uuid}', '{exp_id}', '{s01}', '{s02}', '{s03}', '{s04}', '{s05}', {s06}, '{end_time}', '{is_real}');'''
    return query.format(uuid=dict_values['uuid'],
                        exp_id=dict_values['exp_id'],
                        s01=dict_values['s01'],
                        s02=dict_values['s02'],
                        s03=dict_values['s03'],
                        s04=dict_values['s04'],
                        s05=dict_values['s05'],
                        s06=dict_values['s06'],
                        end_time=dict_values['end_time'],
                        is_real=dict_values['is_real'])

# 쿼리 날리기
def send_query(query):
    try:
        cs = g.db.cursor()
        cs.execute(query)
        g.db.commit()
    except:
        # 로컬 실행
        print(query)

# 실제 테스트에서는 T로 변경하고 진행하자
IS_REAL_TEST = 'F'




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
# intro 페이지
@app.route('/exp1/intro')
def exp1_intro():
    test_no = 1
    test_type = ['스크롤', '페이지']
    next_page = '/exp1/a1/scroll'

    # uuid로 세션 등록
    session['uuid'] = str(uuid4())
    print(session['uuid'])
    print(current_time())
    return render_template('exp_intro.html', test_no=test_no, test_type=test_type, next_page=next_page)


@app.route('/exp1/a1/scroll', methods=['GET', 'POST'])
def exp1_a1_scroll():
    
    try:
        print(session['uuid'])
        common_dict = dict(uuid = session['uuid'], exp_id = 'exp1', test_type = 'scroll', is_real = IS_REAL_TEST)
        data_st = dict(common_dict, question='a1', category='start', time=current_time())

        if request.method == 'POST' and len(request.form) == 2:
            a1_1 = request.form['answer_a1_1']
            a1_2 = request.form['answer_a1_2']

            data_et = dict(common_dict, question='a1', category='end', time=current_time())
            data1 = dict(common_dict, question='a1_1', answer_value=int(a1_1))
            data2 = dict(common_dict, question='a1_2', answer_value=int(a1_2))
            send_query(query=insert_answer(data1))
            send_query(query=insert_answer(data2))
            send_query(query=insert_time(data_et))

            return redirect(url_for('exp1_a2_scroll'))
        send_query(query=insert_time(data_st))
        return render_template('a1_scroll.html')
    # 세션 정보 없을경우 index 페이지로 이동
    except:
        return redirect(url_for('index'))

@app.route('/exp1/a2/scroll', methods=['GET', 'POST'])
def exp1_a2_scroll():
    try:
        print(session['uuid'])
        common_dict = dict(uuid = session['uuid'], exp_id = 'exp1', test_type = 'scroll', is_real = IS_REAL_TEST)
        data_st = dict(common_dict, question='a2', category='start', time=current_time())

        if request.method == 'POST' and len(request.form) == 2:
            a2_1 = request.form['answer_a2_1']
            a2_2 = request.form['answer_a2_2']

            data_et = dict(common_dict, question='a2', category='end', time=current_time())
            data1 = dict(common_dict, question='a2_1', answer_value=int(a2_1))
            data2 = dict(common_dict, question='a2_2', answer_value=int(a2_2))

            send_query(query=insert_answer(data1))
            send_query(query=insert_answer(data2))
            send_query(query=insert_time(data_et))

            return redirect(url_for('exp1_a3_scroll'))

        send_query(query=insert_time(data_st))
        return render_template('a2_scroll.html')
    except:
        return redirect(url_for('index'))


@app.route('/exp1/a3/scroll', methods=['GET', 'POST'])
def exp1_a3_scroll():
    try:
        print(session['uuid'])
        common_dict = dict(uuid = session['uuid'], exp_id = 'exp1', test_type = 'scroll', is_real = IS_REAL_TEST)
        data_st = dict(common_dict, question='a3', category='start', time=current_time())

        if request.method == 'POST' and len(request.form) == 2:
            a3_1 = request.form['answer_a3_1']
            a3_2 = request.form['answer_a3_2']

            data_et = dict(common_dict, question='a3', category='end', time=current_time())
            data1 = dict(common_dict, question='a3_1', answer_value=int(a3_1))
            data2 = dict(common_dict, question='a3_2', answer_value=int(a3_2))

            send_query(query=insert_answer(data1))
            send_query(query=insert_answer(data2))
            send_query(query=insert_time(data_et))

            return redirect(url_for('exp1_rest'))

        send_query(query=insert_time(data_st))
        return render_template('a3_scroll.html')
    except:
        return redirect(url_for('index'))


@app.route('/exp1/rest')
def exp1_rest():
    try:
        print(session['uuid'])

        test_type = ['스크롤', '페이지']
        next_page = '/exp1/b1/page'
        return render_template('rest.html', test_type=test_type, next_page=next_page)
    except:
        return redirect(url_for('index'))


@app.route('/exp1/b1/page', methods=['GET', 'POST'])
def exp1_b1_page():
    try:
        print(session['uuid'])
        common_dict = dict(uuid = session['uuid'], exp_id = 'exp1', test_type = 'page', is_real = IS_REAL_TEST)
        data_st = dict(common_dict, question='b1', category='start', time=current_time())

        if request.method == 'POST' and len(request.form) == 2:
            b1_1 = request.form['answer_b1_1']
            b1_2 = request.form['answer_b1_2']

            # data1 = dict(uuid = session['uuid'], exp_id = 'exp1', test_type = 'page', is_real = IS_REAL_TEST,
            #             question='b1_1', answer_value=int(b1_1))
            # data2 = dict(uuid = session['uuid'], exp_id = 'exp1', test_type = 'page', is_real = IS_REAL_TEST,
            #             question='b1_2', answer_value=int(b1_2))
            data_et = dict(common_dict, question='b1', category='end', time=current_time())
            data1 = dict(common_dict, question='b1_1', answer_value=int(b1_1))
            data2 = dict(common_dict, question='b1_2', answer_value=int(b1_2))
            send_query(query=insert_answer(data1))
            send_query(query=insert_answer(data2))
            send_query(query=insert_time(data_et))

            return redirect(url_for('exp1_b2_page'))

        send_query(query=insert_time(data_st))
        return render_template('b1_page.html')
    except:
        return redirect(url_for('index'))


@app.route('/exp1/b2/page', methods=['GET', 'POST'])
def exp1_b2_page():
    try:
        print(session['uuid'])
        common_dict = dict(uuid = session['uuid'], exp_id = 'exp1', test_type = 'page', is_real = IS_REAL_TEST)
        data_st = dict(common_dict, question='b2', category='start', time=current_time())

        if request.method == 'POST' and len(request.form) == 2:
            b2_1 = request.form['answer_b2_1']
            b2_2 = request.form['answer_b2_2']

            # data1 = dict(uuid = session['uuid'], exp_id = 'exp1', test_type = 'page', is_real = IS_REAL_TEST,
            #             question='b2_1', answer_value=int(b2_1))
            # data2 = dict(uuid = session['uuid'], exp_id = 'exp1', test_type = 'page', is_real = IS_REAL_TEST,
            #             question='b2_2', answer_value=int(b2_2))
            data_et = dict(common_dict, question='b2', category='end', time=current_time())
            data1 = dict(common_dict, question='b2_1', answer_value=int(b2_1))
            data2 = dict(common_dict, question='b2_2', answer_value=int(b2_2))
            send_query(query=insert_answer(data1))
            send_query(query=insert_answer(data2))
            send_query(query=insert_time(data_et))
            return redirect(url_for('exp1_b3_page'))

        send_query(query=insert_time(data_st))
        return render_template('b2_page.html')
    except:
        return redirect(url_for('index'))


@app.route('/exp1/b3/page', methods=['GET', 'POST'])
def exp1_b3_page():
    try:
        print(session['uuid'])
        common_dict = dict(uuid = session['uuid'], exp_id = 'exp1', test_type = 'page', is_real = IS_REAL_TEST)
        data_st = dict(common_dict, question='b3', category='start', time=current_time())

        if request.method == 'POST' and len(request.form) == 2:
            b3_1 = request.form['answer_b3_1']
            b3_2 = request.form['answer_b3_2']

            # data1 = dict(uuid = session['uuid'], exp_id = 'exp1', test_type = 'page', is_real = IS_REAL_TEST,
            #             question='b3_1', answer_value=int(b3_1))
            # data2 = dict(uuid = session['uuid'], exp_id = 'exp1', test_type = 'page', is_real = IS_REAL_TEST,
            #             question='b3_2', answer_value=int(b3_2))
            data_et = dict(common_dict, question='b3', category='end', time=current_time())
            data1 = dict(common_dict, question='b3_1', answer_value=int(b3_1))
            data2 = dict(common_dict, question='b3_2', answer_value=int(b3_2))
            send_query(query=insert_answer(data1))
            send_query(query=insert_answer(data2))
            send_query(query=insert_time(data_et))
            return redirect(url_for('exp1_outro'))

        send_query(query=insert_time(data_st))
        return render_template('b3_page.html')
    except:
        return redirect(url_for('index'))


@app.route('/exp1/outro')
def exp1_outro():
    try:
        print(session['uuid'])

        test_no = 1
        return render_template('exp_outro.html', test_no=test_no)
    except:
        return redirect(url_for('index'))


# 실험2
@app.route('/exp2/intro')
def exp2_intro():
    test_no = 2
    test_type = ['페이지', '스크롤']
    next_page = '/exp2/a1/page'

    # uuid로 세션 등록
    session['uuid'] = str(uuid4())
    print(session['uuid'])

    return render_template('exp_intro.html', test_no=test_no, test_type=test_type, next_page=next_page)


@app.route('/exp2/a1/page', methods=['GET', 'POST'])
def exp2_a1_page():
    try:
        print(session['uuid'])
        common_dict = dict(uuid = session['uuid'], exp_id = 'exp2', test_type = 'page', is_real = IS_REAL_TEST)
        data_st = dict(common_dict, question='a1', category='start', time=current_time())

        if request.method == 'POST' and len(request.form) == 2:
            a1_1 = request.form['answer_a1_1']
            a1_2 = request.form['answer_a1_2']

            # data1 = dict(uuid = session['uuid'], exp_id = 'exp2', test_type = 'page', is_real = IS_REAL_TEST,
            #             question='a1_1', answer_value=int(a1_1))
            # data2 = dict(uuid = session['uuid'], exp_id = 'exp2', test_type = 'page', is_real = IS_REAL_TEST,
            #             question='a1_2', answer_value=int(a1_2))
            data_et = dict(common_dict, question='a1', category='end', time=current_time())
            data1 = dict(common_dict, question='a1_1', answer_value=int(a1_1))
            data2 = dict(common_dict, question='a1_2', answer_value=int(a1_2))
            send_query(query=insert_answer(data1))
            send_query(query=insert_answer(data2))
            send_query(query=insert_time(data_et))
            return redirect(url_for('exp2_a2_page'))

        send_query(query=insert_time(data_st))
        return render_template('a1_page.html')
    except:
        return redirect(url_for('index'))


@app.route('/exp2/a2/page', methods=['GET', 'POST'])
def exp2_a2_page():
    try:
        print(session['uuid'])
        common_dict = dict(uuid = session['uuid'], exp_id = 'exp2', test_type = 'page', is_real = IS_REAL_TEST)
        data_st = dict(common_dict, question='a2', category='start', time=current_time())

        if request.method == 'POST' and len(request.form) == 2:
            a2_1 = request.form['answer_a2_1']
            a2_2 = request.form['answer_a2_2']

            # data1 = dict(uuid = session['uuid'], exp_id = 'exp2', test_type = 'page', is_real = IS_REAL_TEST,
            #             question='a2_1', answer_value=int(a2_1))
            # data2 = dict(uuid = session['uuid'], exp_id = 'exp2', test_type = 'page', is_real = IS_REAL_TEST,
            #             question='a2_2', answer_value=int(a2_2))
            data_et = dict(common_dict, question='a2', category='end', time=current_time())
            data1 = dict(common_dict, question='a2_1', answer_value=int(a2_1))
            data2 = dict(common_dict, question='a2_2', answer_value=int(a2_2))
            send_query(query=insert_answer(data1))
            send_query(query=insert_answer(data2))
            send_query(query=insert_time(data_et))
            return redirect(url_for('exp2_a3_page'))

        send_query(query=insert_time(data_st))
        return render_template('a2_page.html')
    except:
        return redirect(url_for('index'))


@app.route('/exp2/a3/page', methods=['GET', 'POST'])
def exp2_a3_page():
    try:
        print(session['uuid'])
        common_dict = dict(uuid = session['uuid'], exp_id = 'exp2', test_type = 'page', is_real = IS_REAL_TEST)
        data_st = dict(common_dict, question='a3', category='start', time=current_time())

        if request.method == 'POST' and len(request.form) == 2:
            a3_1 = request.form['answer_a3_1']
            a3_2 = request.form['answer_a3_2']

            # data1 = dict(uuid = session['uuid'], exp_id = 'exp2', test_type = 'page', is_real = IS_REAL_TEST,
            #             question='a3_1', answer_value=int(a3_1))
            # data2 = dict(uuid = session['uuid'], exp_id = 'exp2', test_type = 'page', is_real = IS_REAL_TEST,
            #             question='a3_2', answer_value=int(a3_2))
            data_et = dict(common_dict, question='a3', category='end', time=current_time())
            data1 = dict(common_dict, question='a3_1', answer_value=int(a3_1))
            data2 = dict(common_dict, question='a3_2', answer_value=int(a3_2))
            send_query(query=insert_answer(data1))
            send_query(query=insert_answer(data2))
            send_query(query=insert_time(data_et))
            return redirect(url_for('exp2_rest'))

        return render_template('a3_page.html')
    except:
        return redirect(url_for('index'))


@app.route('/exp2/rest')
def exp2_rest():
    try:
        print(session['uuid'])

        test_type = ['페이지', '스크롤']
        next_page = '/exp2/b1/scroll'
        return render_template('rest.html', test_type=test_type, next_page=next_page)
    except:
        return redirect(url_for('index'))


@app.route('/exp2/b1/scroll', methods=['GET', 'POST'])
def exp2_b1_scroll():
    try:
        print(session['uuid'])
        common_dict = dict(uuid = session['uuid'], exp_id = 'exp2', test_type = 'scroll', is_real = IS_REAL_TEST)
        data_st = dict(common_dict, question='b1', category='start', time=current_time())

        if request.method == 'POST' and len(request.form) == 2:
            b1_1 = request.form['answer_b1_1']
            b1_2 = request.form['answer_b1_2']

            # data1 = dict(uuid = session['uuid'], exp_id = 'exp2', test_type = 'scroll', is_real = IS_REAL_TEST,
            #             question='b1_1', answer_value=int(b1_1))
            # data2 = dict(uuid = session['uuid'], exp_id = 'exp2', test_type = 'scroll', is_real = IS_REAL_TEST,
            #             question='b1_2', answer_value=int(b1_2))
            data_et = dict(common_dict, question='b1', category='end', time=current_time())
            data1 = dict(common_dict, question='b1_1', answer_value=int(b1_1))
            data2 = dict(common_dict, question='b1_2', answer_value=int(b1_2))
            send_query(query=insert_answer(data1))
            send_query(query=insert_answer(data2))
            send_query(query=insert_time(data_et))
            return redirect(url_for('exp2_b2_scroll'))

        send_query(query=insert_time(data_st))
        return render_template('b1_scroll.html')
    except:
        return redirect(url_for('index'))


@app.route('/exp2/b2/scroll', methods=['GET', 'POST'])
def exp2_b2_scroll():
    try:
        print(session['uuid'])
        common_dict = dict(uuid = session['uuid'], exp_id = 'exp2', test_type = 'scroll', is_real = IS_REAL_TEST)
        data_st = dict(common_dict, question='b2', category='start', time=current_time())

        if request.method == 'POST' and len(request.form) == 2:
            b2_1 = request.form['answer_b2_1']
            b2_2 = request.form['answer_b2_2']

            # data1 = dict(uuid = session['uuid'], exp_id = 'exp2', test_type = 'scroll', is_real = IS_REAL_TEST,
            #             question='b2_1', answer_value=int(b2_1))
            # data2 = dict(uuid = session['uuid'], exp_id = 'exp2', test_type = 'scroll', is_real = IS_REAL_TEST,
            #             question='b2_2', answer_value=int(b2_2))
            data_et = dict(common_dict, question='b2', category='end', time=current_time())
            data1 = dict(common_dict, question='b2_1', answer_value=int(b2_1))
            data2 = dict(common_dict, question='b2_2', answer_value=int(b2_2))
            send_query(query=insert_answer(data1))
            send_query(query=insert_answer(data2))
            send_query(query=insert_time(data_et))
            return redirect(url_for('exp2_b3_scroll'))

        send_query(query=insert_time(data_st))
        return render_template('b2_scroll.html')
    except:
        return redirect(url_for('index'))


@app.route('/exp2/b3/scroll', methods=['GET', 'POST'])
def exp2_b3_scroll():
    try:
        print(session['uuid'])
        common_dict = dict(uuid = session['uuid'], exp_id = 'exp2', test_type = 'scroll', is_real = IS_REAL_TEST)
        data_st = dict(common_dict, question='b3', category='start', time=current_time())

        if request.method == 'POST' and len(request.form) == 2:
            b3_1 = request.form['answer_b3_1']
            b3_2 = request.form['answer_b3_2']

            # data1 = dict(uuid = session['uuid'], exp_id = 'exp2', test_type = 'scroll', is_real = IS_REAL_TEST,
            #             question='b3_1', answer_value=int(b3_1))
            # data2 = dict(uuid = session['uuid'], exp_id = 'exp2', test_type = 'scroll', is_real = IS_REAL_TEST,
            #             question='b3_2', answer_value=int(b3_2))
            data_et = dict(common_dict, question='b3', category='end', time=current_time())
            data1 = dict(common_dict, question='b3_1', answer_value=int(b3_1))
            data2 = dict(common_dict, question='b3_2', answer_value=int(b3_2))
            send_query(query=insert_answer(data1))
            send_query(query=insert_answer(data2))
            send_query(query=insert_time(data_et))
            return redirect(url_for('exp2_outro'))

        send_query(query=insert_time(data_st))
        return render_template('b3_scroll.html')
    except:
        return redirect(url_for('index'))


@app.route('/exp2/outro')
def exp2_outro():
    try:
        print(session['uuid'])

        test_no = 2
        return render_template('exp_outro.html', test_no=test_no)
    except:
        return redirect(url_for('index'))




# 실험3
@app.route('/exp3/intro')
def exp3_intro():
    test_no = 3
    test_type = ['스크롤', '페이지']
    next_page = '/exp3/b1/scroll'

    # uuid로 세션 등록
    session['uuid'] = str(uuid4())
    print(session['uuid'])

    return render_template('exp_intro.html', test_no=test_no, test_type=test_type, next_page=next_page)


# 지문 B (스크롤)
@app.route('/exp3/b1/scroll', methods=['GET', 'POST'])
def exp3_b1_scroll():
    try:
        print(session['uuid'])
        common_dict = dict(uuid = session['uuid'], exp_id = 'exp3', test_type = 'scroll', is_real = IS_REAL_TEST)
        data_st = dict(common_dict, question='b1', category='start', time=current_time())

        if request.method == 'POST' and len(request.form) == 2:
            b1_1 = request.form['answer_b1_1']
            b1_2 = request.form['answer_b1_2']

            # data1 = dict(uuid = session['uuid'], exp_id = 'exp3', test_type = 'scroll', is_real = IS_REAL_TEST,
            #             question='b1_1', answer_value=int(b1_1))
            # data2 = dict(uuid = session['uuid'], exp_id = 'exp3', test_type = 'scroll', is_real = IS_REAL_TEST,
            #             question='b1_2', answer_value=int(b1_2))
            data_et = dict(common_dict, question='b1', category='end', time=current_time())
            data1 = dict(common_dict, question='b1_1', answer_value=int(b1_1))
            data2 = dict(common_dict, question='b1_2', answer_value=int(b1_2))
            send_query(query=insert_answer(data1))
            send_query(query=insert_answer(data2))
            send_query(query=insert_time(data_et))
            return redirect(url_for('exp3_b2_scroll'))

        send_query(query=insert_time(data_st))
        return render_template('b1_scroll.html')
    except:
        return redirect(url_for('index'))


@app.route('/exp3/b2/scroll', methods=['GET', 'POST'])
def exp3_b2_scroll():
    try:
        print(session['uuid'])
        common_dict = dict(uuid = session['uuid'], exp_id = 'exp3', test_type = 'scroll', is_real = IS_REAL_TEST)
        data_st = dict(common_dict, question='b2', category='start', time=current_time())

        if request.method == 'POST' and len(request.form) == 2:
            b2_1 = request.form['answer_b2_1']
            b2_2 = request.form['answer_b2_2']

            # data1 = dict(uuid = session['uuid'], exp_id = 'exp3', test_type = 'scroll', is_real = IS_REAL_TEST,
            #             question='b2_1', answer_value=int(b2_1))
            # data2 = dict(uuid = session['uuid'], exp_id = 'exp3', test_type = 'scroll', is_real = IS_REAL_TEST,
            #             question='b2_2', answer_value=int(b2_2))
            data_et = dict(common_dict, question='b2', category='end', time=current_time())
            data1 = dict(common_dict, question='b2_1', answer_value=int(b2_1))
            data2 = dict(common_dict, question='b2_2', answer_value=int(b2_2))
            send_query(query=insert_answer(data1))
            send_query(query=insert_answer(data2))
            send_query(query=insert_time(data_et))
            return redirect(url_for('exp3_b3_scroll'))

        send_query(query=insert_time(data_st))
        return render_template('b2_scroll.html')
    except:
        return redirect(url_for('index'))


@app.route('/exp3/b3/scroll', methods=['GET', 'POST'])
def exp3_b3_scroll():
    try:
        print(session['uuid'])
        common_dict = dict(uuid = session['uuid'], exp_id = 'exp3', test_type = 'scroll', is_real = IS_REAL_TEST)
        data_st = dict(common_dict, question='b3', category='start', time=current_time())

        if request.method == 'POST' and len(request.form) == 2:
            b3_1 = request.form['answer_b3_1']
            b3_2 = request.form['answer_b3_2']

            # data1 = dict(uuid = session['uuid'], exp_id = 'exp3', test_type = 'scroll', is_real = IS_REAL_TEST,
            #             question='b3_1', answer_value=int(b3_1))
            # data2 = dict(uuid = session['uuid'], exp_id = 'exp3', test_type = 'scroll', is_real = IS_REAL_TEST,
            #             question='b3_2', answer_value=int(b3_2))
            data_et = dict(common_dict, question='b3', category='end', time=current_time())
            data1 = dict(common_dict, question='b3_1', answer_value=int(b3_1))
            data2 = dict(common_dict, question='b3_2', answer_value=int(b3_2))
            send_query(query=insert_answer(data1))
            send_query(query=insert_answer(data2))
            send_query(query=insert_time(data_et))
            return redirect(url_for('exp3_rest'))

        send_query(query=insert_time(data_st))
        return render_template('b3_scroll.html')
    except:
        return redirect(url_for('index'))


# 휴식
@app.route('/exp3/rest')
def exp3_rest():
    try:
        print(session['uuid'])

        test_type = ['스크롤', '페이지']
        next_page = '/exp3/a1/page'
        return render_template('rest.html', test_type=test_type, next_page=next_page)
    except:
        return redirect(url_for('index'))


# 지문 A (페이지)
@app.route('/exp3/a1/page', methods=['GET', 'POST'])
def exp3_a1_page():    
    try:
        print(session['uuid'])
        common_dict = dict(uuid = session['uuid'], exp_id = 'exp3', test_type = 'page', is_real = IS_REAL_TEST)
        data_st = dict(common_dict, question='a1', category='start', time=current_time())

        # 정답을 둘 다 제출한 경우!
        if request.method == 'POST' and len(request.form) == 2:
            a1_1 = request.form['answer_a1_1']
            a1_2 = request.form['answer_a1_2']

            # data1 = dict(uuid = session['uuid'], exp_id = 'exp3', test_type = 'page', is_real = IS_REAL_TEST,
            #             question='a1_1', answer_value=int(a1_1))
            # data2 = dict(uuid = session['uuid'], exp_id = 'exp3', test_type = 'page', is_real = IS_REAL_TEST,
            #             question='a1_2', answer_value=int(a1_2))
            data_et = dict(common_dict, question='a1', category='end', time=current_time())
            data1 = dict(common_dict, question='a1_1', answer_value=int(a1_1))
            data2 = dict(common_dict, question='a1_2', answer_value=int(a1_2))
            send_query(query=insert_answer(data1))
            send_query(query=insert_answer(data2))
            send_query(query=insert_time(data_et))
            return redirect(url_for('exp3_a2_page'))
        
        send_query(query=insert_time(data_st))
        return render_template('a1_page.html')
    except:
        return redirect(url_for('index'))


@app.route('/exp3/a2/page', methods=['GET', 'POST'])
def exp3_a2_page():
    try:
        print(session['uuid'])
        common_dict = dict(uuid = session['uuid'], exp_id = 'exp3', test_type = 'page', is_real = IS_REAL_TEST)
        data_st = dict(common_dict, question='a2', category='start', time=current_time())

        if request.method == 'POST' and len(request.form) == 2:
            a2_1 = request.form['answer_a2_1']
            a2_2 = request.form['answer_a2_2']

            # data1 = dict(uuid = session['uuid'], exp_id = 'exp3', test_type = 'page', is_real = IS_REAL_TEST,
            #             question='a2_1', answer_value=int(a2_1))
            # data2 = dict(uuid = session['uuid'], exp_id = 'exp3', test_type = 'page', is_real = IS_REAL_TEST,
            #             question='a2_2', answer_value=int(a2_2))
            data_et = dict(common_dict, question='a2', category='end', time=current_time())
            data1 = dict(common_dict, question='a2_1', answer_value=int(a2_1))
            data2 = dict(common_dict, question='a2_2', answer_value=int(a2_2))
            send_query(query=insert_answer(data1))
            send_query(query=insert_answer(data2))
            send_query(query=insert_time(data_et))
            return redirect(url_for('exp3_a3_page'))
        
        send_query(query=insert_time(data_st))
        return render_template('a2_page.html')
    except:
        return redirect(url_for('index'))


@app.route('/exp3/a3/page', methods=['GET', 'POST'])
def exp3_a3_page():
    try:
        print(session['uuid'])
        common_dict = dict(uuid = session['uuid'], exp_id = 'exp3', test_type = 'page', is_real = IS_REAL_TEST)
        data_st = dict(common_dict, question='a3', category='start', time=current_time())

        if request.method == 'POST' and len(request.form) == 2:
            a3_1 = request.form['answer_a3_1']
            a3_2 = request.form['answer_a3_2']

            # data1 = dict(uuid = session['uuid'], exp_id = 'exp3', test_type = 'page', is_real = IS_REAL_TEST,
            #             question='a3_1', answer_value=int(a3_1))
            # data2 = dict(uuid = session['uuid'], exp_id = 'exp3', test_type = 'page', is_real = IS_REAL_TEST,
            #             question='a3_2', answer_value=int(a3_2))
            data_et = dict(common_dict, question='a3', category='end', time=current_time())
            data1 = dict(common_dict, question='a3_1', answer_value=int(a3_1))
            data2 = dict(common_dict, question='a3_2', answer_value=int(a3_2))
            send_query(query=insert_answer(data1))
            send_query(query=insert_answer(data2))
            send_query(query=insert_time(data_et))
            return redirect(url_for('exp3_outro'))

        send_query(query=insert_time(data_st))
        return render_template('a3_page.html')
    except:
        return redirect(url_for('index'))


# 실험3 outro
@app.route('/exp3/outro')
def exp3_outro():
    try:
        print(session['uuid'])

        test_no = 3
        return render_template('exp_outro.html', test_no=test_no)
    except:
        return redirect(url_for('index'))



# 실험4 intro
@app.route('/exp4/intro')
def exp4_intro():
    test_no = 4
    test_type = ['페이지', '스크롤']
    next_page = '/exp4/b1/page'

    # uuid로 세션 등록
    session['uuid'] = str(uuid4())
    print(session['uuid'])

    return render_template('exp_intro.html', test_no=test_no, test_type=test_type, next_page=next_page)


@app.route('/exp4/b1/page', methods=['GET', 'POST'])
def exp4_b1_page():

    # 세션 정보 없을경우 index 페이지로 이동
    try:
        print(session['uuid'])
        common_dict = dict(uuid = session['uuid'], exp_id = 'exp4', test_type = 'page', is_real = IS_REAL_TEST)
        data_st = dict(common_dict, question='b1', category='start', time=current_time())

        if request.method == 'POST' and len(request.form) == 2:
            b1_1 = request.form['answer_b1_1']
            b1_2 = request.form['answer_b1_2']

            # data1 = dict(uuid = session['uuid'], exp_id = 'exp4', test_type = 'page', is_real = IS_REAL_TEST,
            #             question='b1_1', answer_value=int(b1_1))
            # data2 = dict(uuid = session['uuid'], exp_id = 'exp4', test_type = 'page', is_real = IS_REAL_TEST,
            #             question='b1_2', answer_value=int(b1_2))
            data_et = dict(common_dict, question='b1', category='end', time=current_time())
            data1 = dict(common_dict, question='b1_1', answer_value=int(b1_1))
            data2 = dict(common_dict, question='b1_2', answer_value=int(b1_2))
            send_query(query=insert_answer(data1))
            send_query(query=insert_answer(data2))
            send_query(query=insert_time(data_et))
            return redirect(url_for('exp4_b2_page'))

        send_query(query=insert_time(data_st))
        return render_template('b1_page.html')

    except:
        return redirect(url_for('index'))

    


@app.route('/exp4/b2/page', methods=['GET', 'POST'])
def exp4_b2_page():
    try:
        print(session['uuid'])
        common_dict = dict(uuid = session['uuid'], exp_id = 'exp4', test_type = 'page', is_real = IS_REAL_TEST)
        data_st = dict(common_dict, question='b2', category='start', time=current_time())

        if request.method == 'POST' and len(request.form) == 2:
            b2_1 = request.form['answer_b2_1']
            b2_2 = request.form['answer_b2_2']

            # data1 = dict(uuid = session['uuid'], exp_id = 'exp4', test_type = 'page', is_real = IS_REAL_TEST,
            #             question='b2_1', answer_value=int(b2_1))
            # data2 = dict(uuid = session['uuid'], exp_id = 'exp4', test_type = 'page', is_real = IS_REAL_TEST,
            #             question='b2_2', answer_value=int(b2_2))
            data_et = dict(common_dict, question='b2', category='end', time=current_time())
            data1 = dict(common_dict, question='b2_1', answer_value=int(b2_1))
            data2 = dict(common_dict, question='b2_2', answer_value=int(b2_2))
            send_query(query=insert_answer(data1))
            send_query(query=insert_answer(data2))
            send_query(query=insert_time(data_et))
            return redirect(url_for('exp4_b3_page'))

        send_query(query=insert_time(data_st))
        return render_template('b2_page.html')
    except:
        return redirect(url_for('index'))


@app.route('/exp4/b3/page', methods=['GET', 'POST'])
def exp4_b3_page():
    try:
        print(session['uuid'])
        common_dict = dict(uuid = session['uuid'], exp_id = 'exp4', test_type = 'page', is_real = IS_REAL_TEST)
        data_st = dict(common_dict, question='b3', category='start', time=current_time())

        if request.method == 'POST' and len(request.form) == 2:
            b3_1 = request.form['answer_b3_1']
            b3_2 = request.form['answer_b3_2']

            # data1 = dict(uuid = session['uuid'], exp_id = 'exp4', test_type = 'page', is_real = IS_REAL_TEST,
            #             question='b3_1', answer_value=int(b3_1))
            # data2 = dict(uuid = session['uuid'], exp_id = 'exp4', test_type = 'page', is_real = IS_REAL_TEST,
            #             question='b3_2', answer_value=int(b3_2))
            data_et = dict(common_dict, question='b3', category='end', time=current_time())
            data1 = dict(common_dict, question='b3_1', answer_value=int(b3_1))
            data2 = dict(common_dict, question='b3_2', answer_value=int(b3_2))
            send_query(query=insert_answer(data1))
            send_query(query=insert_answer(data2))
            send_query(query=insert_time(data_et))
            return redirect(url_for('exp4_rest'))

        send_query(query=insert_time(data_st))
        return render_template('b3_page.html')
    except:
        return redirect(url_for('index'))


# 휴식
@app.route('/exp4/rest')
def exp4_rest():
    try:
        print(session['uuid'])

        test_type = ['페이지', '스크롤']
        next_page = '/exp4/a1/scroll'
        return render_template('rest.html', test_type=test_type, next_page=next_page)
    except:
        return redirect(url_for('index'))


@app.route('/exp4/a1/scroll', methods=['GET', 'POST'])
def exp4_a1_scroll():
    try:
        print(session['uuid'])
        common_dict = dict(uuid = session['uuid'], exp_id = 'exp4', test_type = 'scroll', is_real = IS_REAL_TEST)
        data_st = dict(common_dict, question='a1', category='start', time=current_time())

        if request.method == 'POST' and len(request.form) == 2:
            a1_1 = request.form['answer_a1_1']
            a1_2 = request.form['answer_a1_2']

            # data1 = dict(uuid = session['uuid'], exp_id = 'exp4', test_type = 'scroll', is_real = IS_REAL_TEST,
            #             question='a1_1', answer_value=int(a1_1))
            # data2 = dict(uuid = session['uuid'], exp_id = 'exp4', test_type = 'scroll', is_real = IS_REAL_TEST,
            #             question='a1_2', answer_value=int(a1_2))
            data_et = dict(common_dict, question='a1', category='end', time=current_time())
            data1 = dict(common_dict, question='a1_1', answer_value=int(a1_1))
            data2 = dict(common_dict, question='a1_2', answer_value=int(a1_2))
            send_query(query=insert_answer(data1))
            send_query(query=insert_answer(data2))
            send_query(query=insert_time(data_et))
            return redirect(url_for('exp4_a2_scroll'))

        send_query(query=insert_time(data_st))
        return render_template('a1_scroll.html')
    except:
        return redirect(url_for('index'))


@app.route('/exp4/a2/scroll', methods=['GET', 'POST'])
def exp4_a2_scroll():
    try:
        print(session['uuid'])
        common_dict = dict(uuid = session['uuid'], exp_id = 'exp4', test_type = 'scroll', is_real = IS_REAL_TEST)
        data_st = dict(common_dict, question='a2', category='start', time=current_time())

        if request.method == 'POST' and len(request.form) == 2:
            a2_1 = request.form['answer_a2_1']
            a2_2 = request.form['answer_a2_2']

            # data1 = dict(uuid = session['uuid'], exp_id = 'exp4', test_type = 'scroll', is_real = IS_REAL_TEST,
            #             question='a2_1', answer_value=int(a2_1))
            # data2 = dict(uuid = session['uuid'], exp_id = 'exp4', test_type = 'scroll', is_real = IS_REAL_TEST,
            #             question='a2_2', answer_value=int(a2_2))
            data_et = dict(common_dict, question='a2', category='end', time=current_time())
            data1 = dict(common_dict, question='a2_1', answer_value=int(a2_1))
            data2 = dict(common_dict, question='a2_2', answer_value=int(a2_2))
            send_query(query=insert_answer(data1))
            send_query(query=insert_answer(data2))
            send_query(query=insert_time(data_et))
            return redirect(url_for('exp4_a3_scroll'))

        send_query(query=insert_time(data_st))
        return render_template('a2_scroll.html')
    except:
        return redirect(url_for('index'))


@app.route('/exp4/a3/scroll', methods=['GET', 'POST'])
def exp4_a3_scroll():
    try:
        print(session['uuid'])
        common_dict = dict(uuid = session['uuid'], exp_id = 'exp4', test_type = 'scroll', is_real = IS_REAL_TEST)
        data_st = dict(common_dict, question='a3', category='start', time=current_time())

        if request.method == 'POST' and len(request.form) == 2:
            a3_1 = request.form['answer_a3_1']
            a3_2 = request.form['answer_a3_2']

            # data1 = dict(uuid = session['uuid'], exp_id = 'exp4', test_type = 'scroll', is_real = IS_REAL_TEST,
            #             question='a3_1', answer_value=int(a3_1))
            # data2 = dict(uuid = session['uuid'], exp_id = 'exp4', test_type = 'scroll', is_real = IS_REAL_TEST,
            #             question='a3_2', answer_value=int(a3_2))
            data_et = dict(common_dict, question='a3', category='end', time=current_time())
            data1 = dict(common_dict, question='a3_1', answer_value=int(a3_1))
            data2 = dict(common_dict, question='a3_2', answer_value=int(a3_2))
            send_query(query=insert_answer(data1))
            send_query(query=insert_answer(data2))
            send_query(query=insert_time(data_et))
            return redirect(url_for('exp4_outro'))

        send_query(query=insert_time(data_st))
        return render_template('a3_scroll.html')
    except:
        return redirect(url_for('index'))


# 실험4 outro
@app.route('/exp4/outro')
def exp4_outro():
    try:
        print(session['uuid'])

        test_no = 4
        return render_template('exp_outro.html', test_no=test_no)
    except:
        return redirect(url_for('index'))



# 설문 페이지
@app.route('/survey', methods = ['GET', 'POST'])
def survey():
    try:
        print(session['uuid'])

        # outro 페이지에서 실험번호를 받아온다
        # 혹시라도 값이 없을경우에는 빈칸으로
        test_no = request.args.get('test_no', '')

        if request.method == 'POST':
            print(request.form)
            # 설문이 완료되면 완료페이지로 보낸다
            if len(request.form) == 6:
                data_survey = dict(uuid = session['uuid'], exp_id = 'exp' + str(test_no), 
                                   s01=request.form['survey01'], s02=request.form['survey02'], 
                                   s03=request.form['survey03'], s04=request.form['survey04'], 
                                   s05=request.form['survey05'], s06=request.form['survey06'],
                                   end_time=current_time(), is_real=IS_REAL_TEST)
                # 데이터 전송
                # 여기만 쿼리가 안가서 컨넥션 한번 더 불러보자
                #send_query(insert_survey(data_survey))
                try:
                    print('prepare connections')
                    db_con = MySQLdb.connect('miika.mysql.pythonanywhere-services.com','miika','minho1234',"miika$reading_test")
                    print('prepare cursor')
                    cs = db_con.cursor()
                    print('prepare query execution')
                    cs.execute(insert_survey(data_survey))
                    print('prepare commit')
                    db_con.commit()
                    print('prepare conn close')
                    db_con.close()
                except:
                    print(insert_survey(data_survey))
                return redirect(url_for('complete'))

            # 텍스트박스는 항상 POST로 전달되는 것 같다
            # 따라서 기본값으로 오는 경우에는 flash를 띄우지 않도록 한다
            elif len(request.form) == 2 and request.form['survey03'] == '' and request.form['survey06'] == '':
                pass
            # 설문을 완료하지 않은 경우 메세지를 띄운다
            else:
                flash('모든 항목의 설문을 완료해주세요')
        return render_template('survey.html')
    except:
        return redirect(url_for('index'))


# 실험종료 페이지
@app.route('/complete')
def complete():
    try:
        print(session['uuid'])

        # 세션 제거
        del session['uuid']

        return render_template('complete.html')

    except:
        return redirect(url_for('index'))
