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
    query=('SELECT * FROM login where username=? and pass=?')
    cursor.execute(query,[username,password])
    data=cursor.fetchone()

    if(data!=None):

        return render_template('contact.html',message='Login Successful'
            )
    else:
        return render_template('index.html',
            message='Login unsuccessful! Incorrect Username or Password')


@app.route('/reg')
def regis():
    """Renders the home page."""
    return render_template(
        'register.html',
        title='Register Page',
        year=datetime.now().year,
    )


@app.route('/log')
def logs():
    """Renders the home page."""
    return render_template(
        'index.html', year=datetime.now().year,
    )


@app.route('/register',methods=['POST'])
def register():
    username=request.form['username']
    password=request.form['password']

    cursor.execute("Insert Into login(username, pass) Values(?,?)" ,[username,password])
    cursor.commit() 
    
    msg = 'You have successfully registered !'
    return render_template('contact.html',message='Congratulations! You have Successfully Created A New Account!')

@app.route('/delete',methods=['POST'])
def delete():
    username=request.form['username']

    cursor.execute("Delete from login where username=?" ,[username])
    cursor.commit() 
    
    msg = 'You have successfully deleted your account!'
    return render_template('delete.html',message='You have successfully deleted your account!')


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
