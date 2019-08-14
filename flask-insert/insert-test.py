from flask import Flask, flash, render_template, redirect, request, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "b1234567"

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_amalProject'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/insert', methods=["POST"])
def method_name():
    district = request.form.get("txt_district")
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO tbl_district(district_name) VALUES(%s)", (district,))
    mysql.connection.commit()
    return redirect(url_for("index"))