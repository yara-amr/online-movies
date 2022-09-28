import db
import sqlite3
from msilib.schema import tables
from db import get_db, close_db 

def create_users_tables():
    connect_db = get_db()

    try: 
        #Create Table
        connect_db.execute("""CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
            );""")
    except Exception as err:
        print("Table is Created Before", str(err))

    connect_db.commit()
    close_db(connect_db) 
create_users_tables()           


def create_movies_table():
    connect_db = get_db()

    try: 
        cursor = connect_db.cursor()

        #Create Table
        cursor.execute("""CREATE TABLE movies_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            release_year TEXT NOT NULL,
            details TEXT,
            photo BLOB NOT NULL);""")

    except Exception as err:
        print("Table is Created Before", str(err))

    connect_db.commit()
    close_db(connect_db) 
create_movies_table() 


def convertToBinaryData(filename):
	
	# Convert binary format to images or files data
	with open(filename, 'rb') as file:
		blobData = file.read()
	return blobData


def insertIntoDB(name, release_year, details, photo):
    connect_db = get_db()

    try: 
        #Create Table
        cursor =  connect_db.cursor()
        sqlite_insert_blob_query = """ INSERT INTO movies_data
                                  (name, release_year, details, photo) VALUES (?, ?, ?, ?)"""
        empPhoto = convertToBinaryData(photo)
        data_tuple = (name, release_year, details, empPhoto)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        connect_db.commit()
        print("Image and file inserted successfully as a BLOB into a table")

        close_db(cursor) 

    except Exception as err:
        print("Failed to insert blob data into sqlite table", str(err))
    

def create_comment_tables():
    connect_db = get_db()

    try: 
        #Create Table
        connect_db.execute("""CREATE TABLE comment (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            movie_name TEXT NOT NULL,
            user_email TEXT NOT NULL,
            comment_text TEXT 
            );""")
    except Exception as err:
        print("Table is Created Before", str(err))

    connect_db.commit()
    close_db(connect_db) 
create_comment_tables()   


def create_favorite_tables():
    connect_db = get_db()

    try: 
        #Create Table
        connect_db.execute("""CREATE TABLE favorite (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            movie_name TEXT NOT NULL,
            user_email TEXT NOT NULL);""")
    except Exception as err:
        print("Table is Created Before", str(err))

    connect_db.commit()
    close_db(connect_db) 
create_favorite_tables()

#### Adding Data In movies_data #####

insertIntoDB("Coco", "2021", "Family Movie", "E:\\MoviesWebsite\\task4\\task4\\static\\images\\Coco.jpg")
insertIntoDB("Harry Potter And The Sorcerer's Stone", "2001", "Family Movie", "E:\\MoviesWebsite\\task4\\task4\\static\\images\\Harry Potter And The Sorcerer's Stone.jpg")
insertIntoDB("Spider-Man No Way Home", "2021", "Action Movie", "E:\\MoviesWebsite\\task4\\task4\\static\\images\\Spider-Man No Way Home.jpg")
insertIntoDB("The Hunger Games", "2016", "Action Movie", "E:\\MoviesWebsite\\task4\\task4\\static\\images\\The Hunger Games.jpg")
insertIntoDB("Jumanji", "2021", "Action Movie", "E:\\MoviesWebsite\\task4\\task4\\static\\images\\Jumanji.jpg")
insertIntoDB("The Maze Runner", "2011", "Action Movie", "E:\\MoviesWebsite\\task4\\task4\\static\\images\\The Maze Runner.jpg")
insertIntoDB("Lightning Ship", "2021", "Action Movie", "E:\\MoviesWebsite\\task4\\task4\\static\\images\\Lightning Ship.jpg")
insertIntoDB("The Pirates The Last Royal Treasure", "2022", "Action Movie", "E:\\MoviesWebsite\\task4\\task4\\static\\images\\The Pirates The Last Royal Treasure.jpg")
insertIntoDB("Pipeline", "2021", "Action Movie", "E:\\MoviesWebsite\\task4\\task4\\static\\images\\Pipeline.jpg")
insertIntoDB("Shark The Beginning", "2021", "Action Movie", "E:\\MoviesWebsite\\task4\\task4\\static\\images\\Shark The Beginning.jpg")
insertIntoDB("Happy New Year", "2016", "Comedian Movie", "E:\\MoviesWebsite\\task4\\task4\\static\\images\\Happy New Year.jpg")
insertIntoDB("Soul", "2021", "Family Movie", "E:\\MoviesWebsite\\task4\\task4\\static\\images\\Soul.jpg")
insertIntoDB("Turning Red", "2021", "Family Movie", "E:\\MoviesWebsite\\task4\\task4\\static\\images\\Turning Red.jpg")
insertIntoDB("Sing 2", "2022", "Family Movie", "E:\\MoviesWebsite\\task4\\task4\\static\\images\\Sing 2.jpg")
insertIntoDB("Cars", "2012", "Family Movie", "E:\\MoviesWebsite\\task4\\task4\\static\\images\\Cars.jpg")
insertIntoDB("Encanto", "2022", "Family Movie", "E:\\MoviesWebsite\\task4\\task4\\static\\images\\Encanto.jpg")
insertIntoDB("Train To Busan", "2020", "Horror Movie", "E:\\MoviesWebsite\\task4\\task4\\static\\images\\Train To Busan.jpg")
insertIntoDB("Parasite", "2021", "Horror Movie", "E:\\MoviesWebsite\\task4\\task4\\static\\images\\Parasite.jpg")
insertIntoDB("The Cursed The Dead Man's Prey", "2019", "Horror Movie", "E:\\MoviesWebsite\\task4\\task4\\static\\images\\The Cursed The Dead Man's Prey.jpg")
insertIntoDB("Five Feet Apart", "2018", "Romantic Movie", "E:\\MoviesWebsite\\task4\\task4\\static\\images\\Five Feet Apart.jpg")
insertIntoDB("The Greatest Showman", "2010", "Romantic Movie", "E:\\MoviesWebsite\\task4\\task4\\static\\images\\The Greatest Showman.jpg")
insertIntoDB("The Theory Of Everything", "2017", "Romantic Movie", "E:\\MoviesWebsite\\task4\\task4\\static\\images\\The Theory Of Everything.jpg")
insertIntoDB("Bajirao Mastani", "2015", "Romantic Movie", "E:\\MoviesWebsite\\task4\\task4\\static\\images\\Bajirao Mastani.jpg")
insertIntoDB("Rab Ne Bana Di Jodi", "2018", "Romantic Movie", "E:\\MoviesWebsite\\task4\\task4\\static\\images\\Rab Ne Bana Di Jodi.jpg")
insertIntoDB("Me Before You", "2016", "Romantic Movie", "E:\\MoviesWebsite\\task4\\task4\\static\\images\\Me Before You.jpg")
insertIntoDB("Interstellar", "2001", "Action Movie", "E:\\MoviesWebsite\\task4\\task4\\static\\images\\Interstellar.jpg")
insertIntoDB("Bring The Soul", "2019", "Romantic Movie", "E:\\MoviesWebsite\\task4\\task4\\static\\images\\Bring The Soul.jpg")
insertIntoDB("Onward", "2021", "Family Movie", "E:\\MoviesWebsite\\task4\\task4\\static\\images\\Onward.jpg")
