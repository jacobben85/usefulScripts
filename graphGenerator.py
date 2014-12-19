import urllib
import os
import time
import datetime
import pygal
import calendar


# the workspace folder
# and temporary file used
# source path
workspaceFolder = '/tmp/'
tempFileName    = 'ingestion.log'
sourcePath      = 'http://u1819.uolsite.univision.com/applogs/'

# The Error look up key
errorKey        = 'HTTP Error'

# List with the errors
errorList = []

x_min = 0
x_max = 30


# method for downloading the file
def downloadFile(fileName):
	global workspaceFolder
	global tempFileName

	# download the file locally for processing
	urllib.urlretrieve (sourcePath + fileName, workspaceFolder + tempFileName)


# delete the downloaded temp file, after processing
def deleteFile():
	os.remove(workspaceFolder + tempFileName)


# method to check the errors in last hour
def checkLastHour():

	logCheckDate = time.strftime("%Y-%m-%d")

	today   = datetime.datetime.now();
	oneHour = datetime.timedelta(hours=3)
	lastHour = today - oneHour
	logCheckHour = lastHour.strftime("%m-%d-%Y @ %H")

	checkByDateAndByHour(logCheckDate, logCheckHour)


# Check the errors for a date and for an particular hour
def checkByDateAndByHour(dateString, hourString):
	global workspaceFolder
	global tempFileName
	global errorKey
	global errorList

	count = 0

	downloadFile("mylog_" + dateString)

	logfile = open(workspaceFolder + tempFileName, "r")
	for line in logfile:
	    if line.find(errorKey) > -1:
	        if line.find(hourString) > -1:
	            count = count + 1

	#print hourString + " : " + str(count)
	errorList.append(count)

	deleteFile()


# check errors today
def checkToday():
	logCheckDate = time.strftime("%Y-%m-%d")
	checkForDate(logCheckDate)


#check errors yesterday
def checkYesterday():
	global x_min
	global x_max

	x_min = 0
	x_max = 24

	today = datetime.datetime.now();
	diff  = datetime.timedelta(days=1)
	yest  = today - diff
	logCheckYest = yest.strftime("%Y-%m-%d")
	logLookUp    = yest.strftime("%m-%d-%Y")
	checkDateByHour(logCheckYest, logLookUp)


# method to check by date
def checkForDate(dateValue):
	global workspaceFolder
	global tempFileName
	global errorKey
	global errorList

	count = 0

	# download the file locally for processing
	downloadFile("mylog_" + dateValue)

	logfile = open(workspaceFolder + tempFileName, "r")
	for line in logfile:
	    if line.find(errorKey) > -1:
	        count = count + 1

	# print dateValue + " : " + str(count)
	errorList.append(count)

	deleteFile()


# check current month, per date
def checkCurrentMonth():
	global x_min
	global x_max
	
	currentDay = time.strftime("%d")
	currentDate = int(currentDay)

	x_min = 1
	x_max = currentDate + 1

	while (currentDate > 0):
		currentDate = currentDate - 1
		today  = datetime.datetime.now();
		differ = datetime.timedelta(days=currentDate)
		datekey = today - differ
		logFile = datekey.strftime("%Y-%m-%d")
		checkForDate(logFile)


# check by hour for a date
def checkDateByHour(dateString, logLookUp):
	global workspaceFolder
	global tempFileName
	global errorKey
	global errorList

	global x_min
	global x_max

	count = 0
	timeString = 23

	today  = datetime.datetime.now();
	todayString = today.strftime("%Y-%m-%d")

	if (todayString == dateString):
		currentTime = time.strftime("%H")
		currentTime = int(currentTime)
		timeString = currentTime - 1

	x_min = 1
	x_max = timeString + 1

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

		#print logCheckHour + " : " + str(count)
		errorList.append(count)

	deleteFile()


# check errors today
def checkTodayByHour():
	datekey  = datetime.datetime.now();
	dateString = datekey.strftime("%Y-%m-%d")
	logLookUp  = datekey.strftime("%m-%d-%Y")
	checkDateByHour(dateString, logLookUp)


# Last month errors
def checkLastMonth():

	today = datetime.datetime.now();
	diff  = datetime.timedelta(months=1)
	lastMonth = today - diff


# checkTodayByHour()
# checkYesterday()
# checkCurrentMonth()
checkLastMonth()


bar_chart = pygal.Bar()
bar_chart.title = 'Error count'
bar_chart.x_labels = map(str, range(x_min, x_max))
bar_chart.add('Errors', errorList)
bar_chart.render_to_file('chart.svg')