from flask import Flask
import time
from easygopigo3 import EasyGoPiGo3
gpg = EasyGoPiGo3()

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello world'

@app.route('/forward')
def forward():
	print("Forward!")
	gpg.forward()	# Send the GoPiGo Forward
	time.sleep(1)	# for 1 second.
	gpg.stop()	# the stop the GoPiGo
	return 'Alexabot moved forward!'

@app.route('/backward')
def backward():
	print("Backward!")
	gpg.backward()	# Send the GoPiGo Backward
	time.sleep(1)	# for 1 second
	gpg.stop()	# and then stop the GoPiGo.
	return 'Backward!'

@app.route('/left')
def left():
	print("Left!")
	gpg.left()
	time.sleep(1)
	gpg.stop()
	return 'Left!'

@app.route('/right')
def right():
	print("Right!")
	gpg.right()
	time.sleep(1)
	gpg.stop()
	return 'Right!'

@app.route('/dance')
def dance():
	print("Dance!")
	for each in range(0,5):
		gopigo.right()
		time.sleep(0.25)
		gopigo.left()
		time.sleep(0.25)
		gopigo.bwd()
		time.sleep(0.25)
	gopigo.stop()
	return 'Dance!'

@app.route('/coffee')
def coffee():
	print("Coffee!")
	return 'coffee!'
	
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
