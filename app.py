from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, TextAreaField, SelectField, PasswordField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissecret!'

class MyForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    text_area = TextAreaField('Text Area')
    radio_area = RadioField('Radio Area', default='Option1', choices=[('Option1', 'Option one is this'), ('Option2', 'Bracia Pierdolec'), ('Option3', 'Gorace mamuski w twojej okolicy')])
    select_area = SelectField('Select Area', choices=[('1','1'), ('2', '2'), ('3', '3')])

@app.route('/', methods = ['POST', 'GET'])
def form():
    form = MyForm()
    

    if form.validate_on_submit():
        return render_template('results.html', email=form.email.data, password=form.password.data, textarea=form.text_area.data, radioarea=form.radio_area.data, selectarea=form.radio_area.data)
    
    return render_template('form.html', form=form)
if __name__ == '__main__':
    app.run(debug=True)