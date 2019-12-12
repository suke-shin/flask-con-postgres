from flask import Flask, render_template, request
from database import db_session
from models import User

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/prereg', methods=['POST'])
def prereg():
	email = None
	if request.method == 'POST':
		name = request.form.get('name')
		email = request.form.get('email')
		if not db_session.query(User).filter(User.email == email).count(): # error
			reg = User(name=name, email=email)
			db_session.add(reg)
			db_session.commit()
			return render_template('success.html')
	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True)