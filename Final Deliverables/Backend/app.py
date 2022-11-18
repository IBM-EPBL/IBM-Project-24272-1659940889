from flask import Flask,render_template, request
from gevent.pywsi import WSGIServer
import joblib
import os
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('hp.html')

@app.route('/search',methods =['GET', 'POST'])
def search():
	gre=float(request.form['gre'])
	tofl=float(request.form['tofl'])
	rank=int(request.form['rank'])
	sop=float(request.form['sop'])
	lop=float(request.form['lop'])
	cgpa=float(request.form['cgpa'])
	rs=int(request.form['rs'])
	x=[[gre,tofl,rank,sop,lop,cgpa,rs]]
	print(gre)
	print(rank)
	model=joblib.load('obj.pkl')
	amt=(model.predict(x)[0])
	print(amt)
	if(amt==True):
		return render_template('resss.html')
	else:
		return render_template('neg res.html')
port = os.getenv('VCAP_APP_PORT','5000')



if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=port)
    
