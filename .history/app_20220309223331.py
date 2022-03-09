from django.shortcuts import redirect
from flask import Flask,request,render_template,redirect
import qrcode
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('try_c.html')

@app.route('/try',methods=['POST'])
def try_c():
    msg=request.form['try_c']
    name=request.form['try_n']
    if name==None:
        name='qrcode'
    img=qrcode.make(msg)
    img=img.save('./static/'+name+'.png')
    return render_template('try_c.html',msg=str(name)+'.png',img=img)
if __name__=='__main__':
    app.run(host='0.0.0.0')
