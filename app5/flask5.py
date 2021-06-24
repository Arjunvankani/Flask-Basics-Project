from flask import Flask, render_template, flash, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fronthend'



@app.route('/', methods=['GET', 'POST'])
def alert():
	form = SimpleForm(FlaskForm)

	if form.validate_on_submit():
		flash("You just Clicked the button !!")

		return redirect(url_for('alert'))
	return render_template('alert.html', form=form)

if __name__ == '__main__':
		app.run(debug=True)	