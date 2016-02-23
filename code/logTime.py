#ELSpring2016/code
# created by Amitoz Deol
#Script to get today's date and time and store it into an SQL database file, testTime.db

import sqlite3
from time import strftime
def readTime():
    timeanddate = strftime('%Y-%m-%d, %H-%M-%S')
    print timeanddate
    return timeanddate
createdb = sqlite3.connect('testTime.db')
curs = createdb.cursor()
def logTime():
    curs.execute('''create table if not exists table1(date TEXT, time TEXT);''')
def addData(date , time):
    curs.execute('''INSERT INTO table1(date, time)VALUES (?,?);''',(date, time))
    createdb.commit()
    createdb.close()
def main():
    data = readTime()
    logTime()
    addData(data[0:9], data[12:19])
main()