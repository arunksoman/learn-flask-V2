from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'bdbshuvffebnfb'

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_crud'

mysql = MySQL(app)

@app.route('/') 
def sql_database():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM tbl_userInfo")
    results = cur.fetchall()
    cur.close()
    msg = 'SELECT * FROM tbl_userInfo'
    return render_template('sqldatabase.html', results=results, msg=msg)   
@app.route('/insert',methods = ['POST', 'GET']) #this is when user submits an insert
def sql_datainsert():
    if request.method == 'POST':
        last_name = request.form['last_name']
        first_name = request.form['first_name']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        zip = request.form['zip']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tbl_userInfo (first_name,last_name,address,city,state,zip) VALUES (%s,%s,%s,%s,%s,%s)", (first_name,last_name,address,city,state,zip) )
        mysql.connection.commit()
    curc = mysql.connection.cursor()
    curc.execute("SELECT * FROM tbl_userInfo")
    results = curc.fetchall()
    mysql.connection.commit()
    msg = 'INSERT INTO tbl_userInfo (first_name,last_name,address,city,state,zip) VALUES ('+first_name+','+last_name+','+address+','+city+','+state+','+zip+')'
    return render_template('sqldatabase.html', results=results, msg=msg) 
@app.route('/delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def sql_datadelete():
    if request.method == 'GET':
        dprimary = request.args.get('dprimary')
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM tbl_userInfo where id = %s", (dprimary,) )
        mysql.connection.cursor()
    curc = mysql.connection.cursor()
    curc.execute("SELECT * FROM tbl_userInfo")
    results = curc.fetchall()
    mysql.connection.commit()
    msg = 'DELETE FROM tbl_userInfo WHERE id = ' + dprimary
    return render_template('sqldatabase.html', results=results, msg=msg)
@app.route('/query_edit',methods = ['POST', 'GET']) #this is when user clicks edit link
def sql_editlink():
    if request.method == 'GET':
        eprimary = request.args.get('eprimary')
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM tbl_userInfo where id = %s", (eprimary, ))
        eresults = cur.fetchall()
        mysql.connection.commit()
    curc = mysql.connection.cursor()
    curc.execute("SELECT * FROM tbl_userInfo")
    results = curc.fetchall()
    mysql.connection.commit()
    return render_template('sqldatabase.html', eresults=eresults, results=results)
@app.route('/edit',methods = ['POST', 'GET']) #this is when user submits an edit
def sql_dataedit():
    if request.method == 'POST':
        old_primary_key = request.form['old_primary_key']
        last_name = request.form['last_name']
        first_name = request.form['first_name']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        zip = request.form['zip']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE tbl_userInfo set first_name=%s,last_name=%s,address=%s,city=%s,state=%s,zip=%s WHERE id=%s", (first_name,last_name,address,city,state,zip,old_primary_key) )
        mysql.connection.commit()
    curc = mysql.connection.cursor()
    curc.execute("SELECT * FROM tbl_userInfo")
    results = curc.fetchall()
    mysql.connection.commit()
    msg = 'UPDATE tbl_userInfo set first_name = ' + first_name + ', last_name = ' + last_name + ', address = ' + address + ', city = ' + city + ', state = ' + state + ', zip = ' + zip + ' WHERE id = ' + old_primary_key
    return render_template('sqldatabase.html', results=results, msg=msg)

if __name__ == "__main__":
    app.run(debug=True)

