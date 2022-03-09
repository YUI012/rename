from django.shortcuts import redirect
from flask import Flask,request,render_template,redirect

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('try_c.html')

@app.route('/try',methods=['POST'])
def try_c():
    msg=request.form['try_c']
    return render_template('try_c.html',msg=msg)

if __name__=='__main__':
    app.run(host='0.0.0.0')
