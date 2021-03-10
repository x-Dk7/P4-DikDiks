import os
from flask import Flask, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import AddForm
######################################
#### SET UP OUR SQLite DATABASE #####
####################################
app = Flask(__name__)
# This grabs our directory
app.config['SECRET_KEY'] = 'mysecretkey'

############################################

# SQL DATABASE AND MODELS

##########################################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                                        os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


class Character(db.Model):

    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    p_name = db.Column(db.Text)
    p_date = db.Column(db.Text)

    def __init__(self, p_name, p_date):
        self.p_name = p_name
        self.p_date = p_date

    def __repr__(self):
        return f"{self.p_name} {self.p_date}"


@app.route('/characters')
def characters():

    mar_char = Character.query.all()
    return render_template('list.html', mar_char=mar_char)


@app.route('/add-character', methods=['GET', 'POST'])
def add_character():

    form = AddForm()
    if form.validate_on_submit():
        name = form.p_name.data
        date = form.p_date.data
        new_char = Character(name, date)
        db.session.add(new_char)
        db.session.commit()

        return redirect(url_for('characters'))

    return render_template('add-character.html', form=form)


#debug = True so we can send and see messages to the terminal window so we can see what our code is doing!
if __name__ == '__main__':
    app.run(debug=True)#host and port can be added into parameters
