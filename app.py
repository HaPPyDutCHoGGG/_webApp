from flask import Flask, render_template, request;
import psycopg2;


app = Flask(__name__);

con = psycopg2.connect(
    database = 'app_db',
    user = 'postgres',
    password = 'psqlmtuci',
    host = 'localhost',
    port = '5432');
cur = con.cursor();

print('connected');

@app.route('/login/', methods = ['GET'])
def index():
    return render_template('login.html');

@app.route('/login/', methods = ['POST'])
def login():
    username = request.form.get('username');
    password = request.form.get('password');
    cur.execute("SELECT EXISTS(SELECT * FROM service.users WHERE login=%s and password=%s)", (str(username),str(password)));
    check = str(cur.fetchone());print(check); #return render_template('account.html', full_name = check);
    if (check == '(False,)'):
        return render_template('account.html', full_name = 'unknown user');
    else:
        if (username == '') or (password == ''):
            return render_template('account.html', full_name = 'input error');

        cur.execute("SELECT * FROM service.users WHERE login=%s and password=%s", (str(username),str(password)));
        records = list(cur.fetchall());

        return render_template('account.html', full_name = records[0][1]);
#select exists(select * from service.users where login='admin' and password='admin');
#select exists(select * from service.users where login='adвквn' and password='aвкквn');
con.close();