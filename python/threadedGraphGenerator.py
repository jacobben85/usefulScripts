import calendar
import datetime
import os
import urllib
import webbrowser
import multiprocessing

import pygal


# the workspace folder
# and temporary file used
# source path
workspaceFolder = '/tmp/'
tempFileName = 'ingestion.log'
sourcePath = 'http://u1819.uolsite.univision.com/applogs/'

# The Error look up key
errorKey = 'HTTP Error'


# method for downloading the file
def downloadFile(fileName, dateValue):
	global workspaceFolder
	global tempFileName

	# download the file locally for processing
	urllib.urlretrieve (sourcePath + fileName, workspaceFolder + dateValue + tempFileName)
	print "downloaded ", fileName


# delete the downloaded temp file, after processing
def deleteFile(dateValue):
	os.remove(workspaceFolder + dateValue + tempFileName)
	print "deleted ", dateValue


# method to check by date
def checkForDate(dateValue):
	global workspaceFolder
	global tempFileName
	global errorKey

	count = 0

	# download the file locally for processing
	downloadFile("mylog_" + dateValue, dateValue)
	
	print "processing ", dateValue

	logfile = open(workspaceFolder + dateValue + tempFileName, "r")
	for line in logfile:
		if line.find(errorKey) > -1:
			count = count + 1

	deleteFile(dateValue)
	
	return count


def checkForMonthYear(lookupYear, lookupMonth):
	
	errorList = []

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

	x_max = numberOfDays + 1

	processing = 0

	while (processing < numberOfDays):
		processing = processing + 1
		dateForLookup = lookupYear + '-' + lookupMonth + '-' + str(processing)

		if processing < 10:
			dateForLookup = lookupYear + '-' + lookupMonth + '-0' + str(processing)

		errorList.append(checkForDate(dateForLookup))
		
	generateChart(lookupMonth, x_max, errorList)
		
		
def logProesser(yearStr, monthStr):
	print "thread started for ", yearStr, monthStr
	checkForMonthYear(yearStr, monthStr)
	print "thread ended for ", yearStr, monthStr


def spawnThread(yearStr, monthStr):
	p = multiprocessing.Process(target=logProesser, args=(yearStr, monthStr, ))
	p.start()


def checkForTheYear():
	global errorList

	months = 12
	while (months > 0):
		months = months
		monthStr = str(months)
		if months < 10:
			monthStr = '0' + str(months)

		spawnThread('2014', monthStr)
		months = months - 1


def generateChart(fileName, x_max, dataForChart):
	global errorKey
	
	print "Generating chart for ", fileName

	bar_chart = pygal.Bar()
	bar_chart.title = fileName
	bar_chart.x_labels = map(str, range(1, x_max))
	bar_chart.add('Errors', dataForChart)
	bar_chart.render_to_file('graph/' + fileName + '.svg')


if __name__ == "__main__":
	
	checkForTheYear()
	
	currentDir = os.path.dirname(os.path.realpath(__file__))
	
	new = 2  # open in a new tab, if possible
	# open a public URL, in this case, the webbrowser docs
	url = "file://" + currentDir + "/errorGraph.html"
	webbrowser.open(url, new=new)
