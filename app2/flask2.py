from flask import Flask, escape, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/signup')
def signup():
	return render_template('signup.html')


@app.route('/thankyou')
def thankyou():
	first = request.args.get('first')
	last =  request.args.get('last')
	return render_template('thankyou.html', first=first, last=last)



@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404




if __name__ == '__main__':
	app.run(debug=True)