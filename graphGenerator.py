import urllib
import os
import time
import datetime

workspaceFolder = 'workspace/'
tempFileName    = 'ingestion.log'
errorKey        = 'HTTP Error'


def downloadFile(fileName):
	global workspaceFolder
	global tempFileName

	# download the file locally for processing
	urllib.urlretrieve ("http://u1819.uolsite.univision.com/applogs/" + fileName, workspaceFolder + tempFileName)


def deleteFile():
	os.remove(workspaceFolder + tempFileName)


def checkLastHour():

	logCheckDate = time.strftime("%Y-%m-%d")

	today   = datetime.datetime.now();
	oneHour = datetime.timedelta(hours=3)
	lastHour = today - oneHour
	logCheckHour = lastHour.strftime("%m-%d-%Y @ %H")

	checkByDateAndByHour(logCheckDate, logCheckHour)


def checkByDateAndByHour(dateString, hourString):
	global workspaceFolder
	global tempFileName
	global errorKey

	count = 0

	downloadFile("mylog_" + dateString)

	logfile = open(workspaceFolder + tempFileName, "r")
	for line in logfile:
	    if line.find(errorKey) > -1:
	        if line.find(hourString) > -1:
	            count = count + 1

	print hourString + " : " + str(count)
	deleteFile()


def checkToday():
	logCheckDate = time.strftime("%Y-%m-%d")
	checkForDate(logCheckDate)


def checkYesterday():
	today   = datetime.datetime.now();
	oneHour = datetime.timedelta(days=1)
	lastHour = today - oneHour
	logCheckYest = lastHour.strftime("%Y-%m-%d")

	checkForDate(logCheckYest)


def checkForDate(dateValue):
	global workspaceFolder
	global tempFileName
	global errorKey

	count = 0

	# download the file locally for processing
	downloadFile("mylog_" + dateValue)

	logfile = open(workspaceFolder + tempFileName, "r")
	for line in logfile:
	    if line.find(errorKey) > -1:
	        count = count + 1

	print dateValue + " : " + str(count)

	deleteFile()


def checkCurrentMonth():
	currentDay = time.strftime("%d")
	currentDate = int(currentDay)

	while (currentDate > 0):
		currentDate = currentDate - 1
		today  = datetime.datetime.now();
		differ = datetime.timedelta(days=currentDate)
		datekey = today - differ
		logFile = datekey.strftime("%Y-%m-%d")
		checkForDate(logFile)


def checkDateByHour(dateString, logLookUp):
	global workspaceFolder
	global tempFileName
	global errorKey

	count = 0
	timeString = 23

	today  = datetime.datetime.now();
	todayString = today.strftime("%Y-%m-%d")

	if (todayString == dateString):
		currentDay = time.strftime("%d")
		currentDate = int(currentDay)
		timeString = currentDate - 1

	# download the file locally for processing
	downloadFile("mylog_" + dateString)

	while (timeString > -1):
		logfile = open(workspaceFolder + tempFileName, "r")
		count = 0
		hours = str(timeString)

		if timeString < 10:
			hours = '0' + str(timeString)

		logCheckHour = logLookUp + " @ " + hours

		for line in logfile:
		    if line.find(errorKey) > -1:
		        if line.find(logCheckHour) > -1:
		            count = count + 1

		timeString = timeString - 1

		print logCheckHour + " : " + str(count)

	deleteFile()


def checkTodayByHour():
	datekey  = datetime.datetime.now();
	#differ = datetime.timedelta(days=2)
	#datekey = today - differ
	dateString = datekey.strftime("%Y-%m-%d")
	logLookUp  = datekey.strftime("%m-%d-%Y")
	checkDateByHour(dateString, logLookUp)


checkTodayByHour()