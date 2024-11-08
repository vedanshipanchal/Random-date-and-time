import random
import time


def getRandomdate(startDate,endDate):
    print("To print a ramdom date betweeen start date and end date")
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'
    startTime = time.mktime(time.strptime(startDate,dateFormat))
    endtime = time.mktime(time.strptime(startDate,dateFormat))
    randomTime = startTime + randomGenerator * (endtime-startTime)
    randomDate = time.strftime(dateFormat,time.localtime(randomTime))
    return randomDate

print("Random date:",getRandomdate("1/4/2012","6/12/2028"))