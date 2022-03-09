from django.shortcuts import redirect
from flask import Flask
from flask import render_template,request

app=Flask(__name__)

@app.route('/')
def open_c():
    return render_template('oepn_c.html')

@app.route('/try',methods=['POST'])
def try_c():
    ok=request.form()
    if ok:
        print('ないです')
        redirect('/')
if __name__=='__main__':
    app.run(host='0.0.0.0')
