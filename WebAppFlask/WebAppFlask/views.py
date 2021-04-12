"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template,request
from WebAppFlask import app
import pypyodbc


DATABASE_CONFIG ={
    'Driver': 'SQL Server',
    'Server': 'LAPTOP-JRMJFTHU\SQLEXPRESS',
    'Database':'CompanyDB',
    'UID': 'api',
    'Password': 'admin'
    }

connection = pypyodbc.connect("Driver= {"+DATABASE_CONFIG["Driver"]+"};Server=" + DATABASE_CONFIG["Server"] + "; Database=" + DATABASE_CONFIG["Database"] + ";uid=" + DATABASE_CONFIG["UID"] + ";pwd=" + DATABASE_CONFIG["Password"])


cursor=connection.cursor()
query=('SELECT * FROM login')
cursor.execute(query)
for row in cursor:
    uname=row[0]
    passw=row[1]


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )


@app.route('/contact',methods=['Post'])
def contact():
    username=request.form['username']
    password=request.form['password']
    data='%s %s' %(username,password)
    if(username==uname and password==passw):

        return render_template('contact.html',message='Congratulations! You Successfully logged in!',value=data)
    else:
        return render_template('index.html',message='You have entered wrong set of credentials')


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
