from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
   return 'Hello, World !'

@app.route('/info')
def info():
	return '<h1> Arjun Vankani</h1>'


@app.route('/friend/<name>')
# def friend(name):
#	return '10th char of a name {}</h1>'.format(name[10])


def friend(name):
	return render_template('front2.html',name=name)



@app.route('/html')
def index():
	name = "Arjun"

	list1 = list(name)

	return render_template('front1.html', name=name, list1=list1)
	


@app.route('/index')
def index1():
	return render_template('front1.html')


if __name__ == '__main__':
	app.run(debug=True)