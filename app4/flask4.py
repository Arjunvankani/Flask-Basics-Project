from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField, DateTimeField, RadioField, SelectField, TextField, TextAreaField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fronthend'


class InfoForm(FlaskForm):
	bread = StringField('What type of bread are you? ', validators=[DataRequired()])
	mood = RadioField('Please select your choose :', choices=[('mood1','Happy'),('mood2', 'Exited'),('mood3', 'Sad')])
	food_choice = SelectField(u'Pick your choice :',choices=[('chi','Chiken'),('fish', 'Fish'),('veg', 'Grass')])

	feedback = TextAreaField()
	submit = SubmitField('Submit')




@app.route('/', methods=['GET','POST'])
def index():
	

	form =InfoForm()

	if form.validate_on_submit():

		session['bread'] = form.bread.data
		session['mood'] = form.mood.data
		session['food'] = form.food_choice.data
		session['feedback'] = form.feedback.data

		return redirect(url_for('thankyou'))
	return render_template('index.html', form=form)


@app.route('/thankyou')
def thankyou():

	return render_template('thankyou.html')
	





if __name__ == '__main__':
		app.run(debug=True)	