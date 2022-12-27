import requests as req
from flask import Flask, render_template, request
import psycopg2


app = Flask(__name__)

con = psycopg2.connect(
    database = 'app_db',
    user = 'postgres',
    password = 'psqlmtuci',
    host = 'localhost',
    port = '5432')
cur = con.cursor()


@app.route('/login/', methods = ['GET'])
def index():
    return render_template('login.html')

@app.route('/login/', methods = ['POST'])
def login():
    username = request .form.get('username')
    password = request .form.get('passport')
    cur.execute("SELECT * FROM servise.users WHERE login=%s and password=%s", (str(username),str(password)))
    records = list(cur.fetchall())

    return render_template('account.html', full_name = records[0][1])