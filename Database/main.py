import os
from flask import Flask, render_template, flash, redirect, url_for, session, logging
from flask import request
import requests
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc


######################################
#### SET UP OUR SQLite DATABASE #####
####################################

# This grabs our directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#OMG SO IMPORTANT TO INCLUDE THIS ABOVE! Warnings up the wazoo if not here on a develoment server.

db = SQLAlchemy(app)

#we're adding to table dates
class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    #not planning to delete dates, but still a good practice
    p_name = db.Column(db.String(20), unique=False, nullable=False)
    p_date = db.Column(db.String, unique=False, nullable=False)

    #want score as int so we can sort by it easily. #Since we r trying without score I will change Lname to string

    def __init__(self, p_name, p_date):
        self.p_name = p_name
        self.p_date = p_date

    def __repr__(self):
        return f"{self.p_name}, {self.p_date}"

#db.create_all(); #to initialize the tables in the db. Do not need after first initilization


@app.route('/characters')
def characters():
    #go to the score table and query it, order it by the score value descending, limit 5 and serve up all of those items I asked for as a list.
    results = Characters.query.order_by(desc('p_date')).all()
    dates = []

    for result in results:
        date_dict = {'name':result.p_name, 'score':result.p_score}
        dates.append(date_dict)

    return render_template('index.html', dates = dates)


@app.route('/add-character', methods=['GET', 'POST'])
def add_character():

    if request.method == 'POST':
        name = request.form['name']
        date_created = request.form['date_created']
        #the code below confirmed I had the proper data. Now to add it to the db.
        #print(name)
        #print(score)

        new_character = Characters(name, date_created)
        db.session.add(new_character)
        db.session.commit()

        #here for now, should go to dates eventually.
        return redirect(url_for('characters', username=name))

    return render_template('add_character.html')


#debug = True so we can send and see messages to the terminal window so we can see what our code is doing!
if __name__ == '__main__':
    app.run(debug=True)  #host and port can be added into parameters
