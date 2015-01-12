import calendar
import datetime
import os
import time
import urllib
import webbrowser

import pygal


# the workspace folder
# and temporary file used
# source path
workspaceFolder = '/tmp/'
tempFileName = 'ingestion.log'
sourcePath = 'http://u1819.uolsite.univision.com/applogs/'

# The Error look up key
errorKey = 'HTTP Error'

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

	today = datetime.datetime.now();
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

	# print hourString + " : " + str(count)
	errorList.append(count)

	deleteFile()


# check errors today
def checkToday():
	logCheckDate = time.strftime("%Y-%m-%d")
	checkForDate(logCheckDate)


# check errors yesterday
def checkYesterday():
	global x_min
	global x_max

	x_min = 0
	x_max = 24

	today = datetime.datetime.now();
	diff = datetime.timedelta(days=1)
	yest = today - diff
	logCheckYest = yest.strftime("%Y-%m-%d")
	logLookUp = yest.strftime("%m-%d-%Y")
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
		today = datetime.datetime.now();
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

	today = datetime.datetime.now();
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

		# print logCheckHour + " : " + str(count)
		errorList.append(count)

	deleteFile()


# check errors today
def checkTodayByHour():
	datekey = datetime.datetime.now();
	dateString = datekey.strftime("%Y-%m-%d")
	logLookUp = datekey.strftime("%m-%d-%Y")
	checkDateByHour(dateString, logLookUp)


# Last month errors
def checkLastMonth():

	today = datetime.datetime.now();
	currentDay = today.strftime("%d")
	currentDay = int(currentDay) + 1
	diff = datetime.timedelta(days=currentDay)
	lastMonth = today - diff

	lookupMonth = lastMonth.strftime("%m")
	lookupYear = lastMonth.strftime("%Y")

	checkForMonthYear(lookupYear, lookupMonth)


def checkForMonthYear(lookupYear, lookupMonth):
	global x_min
	global x_max

	lookupMonthInt = int(lookupMonth)
	lookupYearInt = int(lookupYear)

	monthRange = calendar.monthrange(lookupYearInt, lookupMonthInt)
	numberOfDays = monthRange[1]

	dateKey = datetime.datetime.now();
	currentYear = dateKey.strftime("%Y")
	currentMonth = dateKey.strftime("%m")
	currentDay = dateKey.strftime("%d")

	if lookupYearInt == int(currentYear):
		if lookupMonthInt > int(currentMonth):
			return
		elif lookupMonthInt == int(currentMonth):
			numberOfDays = int(currentDay)

	elif lookupYearInt > currentYear:
		return


	x_min = 1
	x_max = numberOfDays + 1

	processing = 0

	while (processing < numberOfDays):
		processing = processing + 1
		dateForLookup = lookupYear + '-' + lookupMonth + '-' + str(processing)

		if processing < 10:
			dateForLookup = lookupYear + '-' + lookupMonth + '-0' + str(processing)

		checkForDate(dateForLookup)


def checkForTheMonth():
	checkForMonthYear('2014', '08')

def checkForTheYear():
	global errorList

	months = 12
	while (months > 0):
		months = months
		monthStr = str(months)
		if months < 10:
			monthStr = '0' + str(months)

		errorList[:] = []
		checkForMonthYear('2014', monthStr)
		generateChart(monthStr)
		months = months - 1

def generateChart(fileName):
	global errorKey
	global x_min
	global x_max
	global errorList

	bar_chart = pygal.Bar()
	bar_chart.title = fileName
	bar_chart.x_labels = map(str, range(x_min, x_max))
	bar_chart.add('Errors', errorList)
	bar_chart.render_to_file('graph/' + fileName + '.svg')


# checkTodayByHour()
# checkYesterday()
checkCurrentMonth()
# checkLastMonth()
# checkForTheMonth()
# checkForTheYear()

# currentDir = os.path.dirname(os.path.realpath(__file__))

# new = 2  # open in a new tab, if possible
# open a public URL, in this case, the webbrowser docs
# url = "file://" + currentDir + "/errorGraph.html"
# webbrowser.open(url, new=new)
