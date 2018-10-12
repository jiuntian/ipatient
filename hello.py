from flask import Flask, flash, redirect, render_template, request, session, abort
import os, time
from flask_qrcode import QRcode
app = Flask(__name__)
QRcode(app)
pop = False
ali = {
	'name' : 'Gan Ah Bek',
	'address' : 'A123, University of Malaya',
	'age' : 40,
	'rn':'27261166',
	'nric' : "780513-02-5123",
	'mobile' : "0123456789",
	'nextofkin': "Try binti Test",
	'nok_no': "0112223344",
	'appointment' : [{'department': "Blood Taking Center", 'time' : '8:00', 'date' : '2018-11-12', 'id': 0},
					{'department': "Bio Imaging - MRI", 'time' : '9:00', 'date' : '2018-11-12', 'id': 1},
					{'department': "RUKA", 'time' : '14:00', 'date' : '2018-11-19', 'id': 2}],
	'last_diag': [{'problem': "Fever", 'detail': "Fever at 50 degree celcius."}],
	'medication': [{'name': 'Metformin', 'time_taken': "08:00, 16:00, 00:00", 'day': "Everyday", 'link': "https://www.webmd.com/drugs/2/drug-11285-7061/metformin-oral/metformin-oral/details"},
					{'name': 'Glargine', 'time_taken': "08:00", 'day': "Everyday", 'link': "https://www.webmd.com/drugs/2/drug-20805/insulin-glargine-subcutaneous/details"}
					],
	'pharmacy': {'queueno': 2604},
	'pop': False
}

@app.route("/")
@app.route("/index")
def home(ali=ali):
	# if not login yet
	if not session.get('logged_in'):
		return render_template('login.html', ali=ali)
	else:
		return render_template('index.html', ali=ali)

		
@app.route("/map")
def map():
	return render_template('map.html')
	

@app.route("/appointment")
def appointment(ali=ali):
	return render_template('appointment.html', ali=ali)

@app.route("/bill/<id>")
def bill(ali=ali, id=id):
	id = int(id)
	return render_template('bill.html', ali=ali, id=id)

@app.route("/education")
def edu(ali=ali):
	return render_template('education.html', ali=ali)

@app.route("/lie/<command>", methods=['POST'])
def lie(command, pop=pop):
	if(command=="show"):
		ali['pop'] = True
		print("Fuck it true")
	elif(command=="hide"):
		ali['pop'] = False
		print("Fuck it false")
	render_template('medication.html', ali=ali, pop=pop)
	#return medication()
	return doctor()

@app.route("/ischeckedin")
def ischeckedin():
	return render_template('ischeckedin.html', ali=ali)
	
@app.route("/diabetes")
def diabetes():
	return render_template('diabetes.html', ali=ali)

@app.route("/signup", methods=['POST','GET'])
def signup():
	if request.method =='POST':
		return home();
	else:
		return render_template('signup.html', ali=ali)
	
@app.route("/medication")
def medication(ali=ali, pop=pop):
	return render_template('medication.html', ali=ali, pop=pop)
	
@app.route("/diagnosis")
def diagnosis(ali=ali):
	return render_template('diagnosis.html', ali=ali)
	
@app.route("/makeappointment", methods=['POST','GET'])
def makeappointment(ali=ali):
	if request.method =='GET':
		return render_template('makeappointment.html', ali=ali)
	elif request.method =='POST':
		ali['appointment'].append(dict({'department': request.form['department'], 'time' : request.form['time'], 'date' : request.form['date'], 'id': len(ali['appointment'])}))
		return appointment(ali=ali)

@app.route('/login', methods=['POST','GET'])
def do_admin_login():
	if request.method =='POST':
		if request.form['password'] == 'ali' and request.form['username'] == 'ali':
			session['logged_in'] = True
		else:
			flash('Wrong password!')
		return home()
	else:
		return render_template('login.html')
	
if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run(host='0.0.0.0', port=5000)
