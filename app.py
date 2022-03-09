from flask import Flask,request
from flask import render_template,redirect
import qrcode

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('try_c.html')

@app.route('/try',methods=['POST'])
def try_c():
    msg=request.form['try_c']
    name=request.form['try_n']
    img=qrcode.make(msg)
    qr_route='./static/'+name+'.png'
    img.save(qr_route)
    return render_template('try_o.html',msg=msg,qr_name=str(name)+'.png',qr_route=qr_route)
if __name__=='__main__':
    app.run()
