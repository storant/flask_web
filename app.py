from flask import Flask, render_template, request, redirect, url_for, flash
from progs import aggregator
from progs.aggregator import curr_time, choice_pass
from progs.customenter import get_balance, get_number
app = Flask(__name__,template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_nexmo')
def send_nexmo():
    time = curr_time()
    balance = get_balance()
    number = get_number()
    return render_template('send_nexmo.html',time=time,balance=balance,number=number)
    
@app.route('/send_nexmo',methods=['POST'])
def sending_nexmo(): 
    num = request.form['phone']
    text = request.form['text']
    choice = request.form['choice']
    aggregator.choice_help(num,text,choice)
    return render_template('pass_nexmo.html',number=num,choice=choice_pass(choice),text_sent=text)
'''
@app.route('/pass_nexmo')
def pass_nexmo():
    return render_template('pass_nexmo.html')
'''
@app.route('/pass_nexmo')
def pass_nexmo():
    flash('this did nuffin')
    return render_template('pass_nexmo.html')

@app.route('/mongodb', methods=['GET', 'POST'])
def mongodb():
    some_a = None
    some_b = None
    
    if request.method == 'POST':
        #if bool(request.form['username'])==1:
        some_a = request.form['username']
        some_b = request.form['password']
        #else:
            #some_a = request.form['username']
            #some_b = request.form['password']
    return render_template('mongodb.html',one=some_a,two=some_b)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error=error)