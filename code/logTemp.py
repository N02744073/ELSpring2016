#!usr/bin/python
import os
import time
import sqlite3
"""Log Current time, Temperature in Celcius and Farenheit
   Return a list[time, tempC, tempF]"""
createdb = sqlite3.connect('/home/pi/ELSpring2016/code/testTemp.db')
curs = createdb.cursor()
def logTemp():
	tempfile = open("/sys/bus/w1/devices/28-00000698107d/w1_slave")
	tempfile_text = tempfile.read()
	currentTime = time.strftime('%x %X %Z')
	tempfile.close()
	tempC = float(tempfile_text.split("\n")[1].split("t=")[1])/1000
	tempF = tempC*9.0/5.0+32.0
	return[currentTime, tempC, tempF]
def addData(currentTime, tempC, tempF):
	curs.execute('''create table if not exists table1(date TEXT, time TEXT, tempC REAL, tempf REAL);''')
	curs.execute('''INSERT INTO table1(date, time, tempC, tempF)VALUES(?,?,?,?)''',(currentTime[1:8], currentTime[10:17], tempC, tempF))
	createdb.commit()
	createdb.close()
def main():
	data, tempC, tempF = logTemp()
	print data
	print tempC
	print tempF
	addData(data, tempC, tempF)
#print logTemp()
main()
