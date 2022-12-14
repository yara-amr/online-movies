import db
from flask import Flask, render_template, request, redirect, url_for, session,flash
import sqlite3
import os

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")
    return filename


'''
def readBlobData(id):
    try:
        sqliteConnection = sqlite3.connect('new_employee.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sql_fetch_blob_query = """SELECT * from movies_data where id = ?"""
        cursor.execute(sql_fetch_blob_query, (id,))
        record = cursor.fetchall()
        name=""
        photo=""
        for row in record:
            print("Id = ", row[0], "Name = ", row[1])
            name = row[1]
            photo = row[4]
            print("Storing employee image and resume on disk \n")
            photoPath = "E:\\MoviesWebsite\\task4\\task4\\static\\images\\" + name + ".jpg"
            xx = writeTofile(photo, photoPath)
        cursor.close()
        return name
    except sqlite3.Error as error:
        print("Failed to read blob data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")
'''

@app.route('/')
def index_page():
    connect =db.get_db()
    cursor = connect.cursor()

    sql_fetch_blob_query = """SELECT id from movies_data"""
    cursor.execute(sql_fetch_blob_query)
    record = cursor.fetchall()
     
    connect.commit()
    cursor.close()

    con = db.get_db()
   
    cur = con.cursor()
    cur.execute("select * from movies_data")
   
    rows = cur.fetchall()
    '''sqliteConnection = sqlite3.connect('new_employee.db')
    cursor = sqliteConnection.cursor()
    print("Connected to SQLite")
    sql_fetch_blob_query = """SELECT id from movies_data"""
    cursor.execute(sql_fetch_blob_query)
    record = cursor.fetchall()
     
    sqliteConnection.commit()
    cursor.close()
    con = sqlite3.connect("new_employee.db")
    con.row_factory = sqlite3.Row
   
    cur = con.cursor()
    cur.execute("select * from movies_data")
   
    rows = cur.fetchall()'''
            
    return render_template("HomePage.html",rows = rows)


@app.route('/about')
def aboutPage():
    return render_template('about.html')


@app.route('/login', methods=['GET', 'POST'])
def LoginPage():
    
    r=""    
    if request.method == 'POST':
        if ( request.form['email'] != "" and request.form['password'] != ""):

            email = request.form['email']
            password = request.form['password']
            
            connect = db.get_db()
            c = connect.cursor()
        
            c.execute("SELECT * FROM users WHERE email = ? AND password = ?" ,(email, password))
            #connect.commit()
            r = c.fetchall()
            
            for i in r:
                if(email == i[2] and password ==i[3]):
                    session['logged_in'] = True
                    session['email'] = email
                    flash('Log In successfully')
                    return redirect(url_for("index_page"))
                else:                    
                    render_template('LoginPage.html')
            
            db.close_db(connect)    
        
        return render_template('LoginPage.html', msg = "*** Please Check Your Enter ***")

    return render_template('LoginPage.html')
    

@app.route('/signup', methods=['GET', 'POST'])
def SignupPage():
    if request.method == 'POST':
        if (request.form['name'] != "" and request.form['email'] != "" and request.form['password'] != ""):
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            
            connect = db.get_db()
            c = connect.cursor()
            c.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)" ,(name, email, password))
            print("Done")
            connect.commit()
            db.close_db(connect)
            return redirect(url_for("LoginPage"))
        
        return render_template('SignupPage.html', msg = "*** Please Full All Fields ***")
    return render_template('SignupPage.html')
        

@app.route('/search', methods=['GET','POST'])
def search():
    
    if request.method == 'POST':
        if (request.form['search'] != ""):

            search = request.form['search']
            
            connect = db.get_db()
            c = connect.cursor()
            c.execute("select * from movies_data where name = ?" ,(search,))
            result = c.fetchall()
            
            db.close_db(connect)
    return render_template("search.html", record = result)


@app.route('/Browse_movie/<string:name>', methods=['GET', 'POST'])
def Browse_movie(name = None):
    if request.method == 'POST':
        name = request.form['name'] 
    
    cur1 = db.get_db().cursor()
    cur1.execute(f"select * from comment where movie_name = ?", (name,))
    data = cur1.fetchall()

    cur = db.get_db().cursor()
    cur.execute(f"select * from movies_data where name = ?", (name,))
    row = cur.fetchone()

    return render_template('Browse_movie.html', row = row, data = data)    


@app.route('/Add_comment', methods=['GET', 'POST'])
def Add_comment():
    
    if request.method == 'POST':

        if (request.form['name'] != "" and request.form['email'] != "" and request.form['comment'] != "" and session['logged_in'] == True):
            name = request.form['name']
            email = request.form['email']
            comment = request.form['comment']
            connect = db.get_db()
            c = connect.cursor()

            c.execute("INSERT INTO comment (movie_name, user_email, comment_text) VALUES (?, ?, ?)" ,(name, email, comment))
            connect.commit()

            cur = db.get_db().cursor()
            cur.execute(f"select * from movies_data where name = ?", (name,))
            row = cur.fetchone()

            cur = db.get_db().cursor()
            cur.execute(f"select * from comment where movie_name = ?", (name,))
            data = cur.fetchall()

            db.close_db(connect)

            return render_template('Browse_movie.html', row = row, data = data)
        
        return render_template('Add_comment.html', msg = "*** Please Full All Fields ***")    

    return render_template('Add_comment.html')    


@app.route('/Add_favorite', methods=['GET', 'POST'])
def Add_favorite():
    if request.method == 'POST' and session['logged_in'] == True:

        if (request.form['favorite_movie'] != "" and request.form['user_email'] != ""):
            name = request.form['favorite_movie']
            email = request.form['user_email']
            
            connect = db.get_db()
            c = connect.cursor()

            c.execute("INSERT INTO favorite (movie_name, user_email) VALUES (?, ?)" ,(name, email))
            connect.commit()

            cur = db.get_db().cursor()
            cur.execute(f"select * from movies_data where name = ?", (name,))
            row = cur.fetchone()

            '''cur = db.get_db().cursor()
            cur.execute(f"select * from favorite where movie_name = ?", (name,))
            data = cur.fetchall()'''

            db.close_db(connect)

            return render_template('Browse_movie.html', row = row)

        return render_template('Add_favorite.html', msg = "*** Please Full All Fields ***")    


    return render_template('Add_favorite.html')    


@app.route('/favorite_list')
def favorite_list():
    if session['logged_in'] == True:
        con = db.get_db()
    
        cur = con.cursor()
        cur.execute("select * from favorite where user_email = ?", (session['email'], ))
    
        row = cur.fetchall()
                
        return render_template("favoriteList.html",row = row)


@app.route('/LogOut')
def LogOut():
    session.clear()
    return redirect(url_for("index_page"))
