from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fronthend'


class InfoForm(FlaskForm):
	bread = StringField('What type of bread are you??')
	submit =SubmitField('Submit')

@app.route('/', methods=['GET','POST'])
def index():
	bread = False

	form =InfoForm()
	if form.validate_on_submit():
		bread = form.bread.data
		form.bread.data=''

	return render_template('base.html', form=form, bread=bread)

if __name__ == '__main__':
		app.run(debug=True)