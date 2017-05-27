from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def sigin_form():
	return '''<form action="/signin" method="post">
			<p><input type="text" name="username"/></p>
			<p><input type="text" name="password"/></p>
			<p><input type="submit" value="Sign In" /></p>
			</form>'''

@app.route('/signin', methods=['POST'])
def signin():
	# need from request object read form content
	if request.form['username'] == 'zlxs' and request.form['password'] == 'pass':
		return '<h3>Hello %s</h3>' % 'zlxs'
	return '<h3>Bad!!!</h3>'

print(Flask.__name__)
# print(Flask.__file__)
# print(Flask.__doc__)
# print(Flask.__dict__)

if __name__ == '__main__':
	app.run()