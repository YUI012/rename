from django.shortcuts import redirect
from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/')
def open_c():
    return render_template('try_c.html')

@app.route('/try',methods=['POST'])
def try_c():
    ok=request.form.get('try_c')
    if ok==None:
        print('ăȘăă§ă')
        redirect('/')
if __name__=='__main__':
    app.run(host='0.0.0.0')
