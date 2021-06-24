from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
db = SQLAlchemy(app)
db.init_app(app)
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/databasename'




posts = [
{
	'author': 'Arjun Vankani',
	'title': 'Blog Post 1',
	'content': 'First Post Content',
	'date_posted': 'March 1, 2020'
},
{
	'author': 'Jay Gundigara',
	'title': 'Blog Post 2',
	'content': 'Second Post Content',
	'date_posted': 'Feb 21, 2020'
}


]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'your Account has been created ! You are now able to  log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)