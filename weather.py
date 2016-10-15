'''
    Author: Sneha Bhalodia
    Python Version: 2.7
'''
import urllib2
import csv
import datetime
import threading

def getData(year):
    print year
    file1 = open(year+'.csv', 'wb');
    writer = csv.writer(file1)
    
    d = datetime.datetime(int(year), 1, 1, 0, 0)
    d2 = datetime.datetime(int(year), 12, 31, 0, 0)
    today = datetime.datetime.today()
    
    # loop through each day of the year
    while (d <= d2) and (d < today):
        print str(d.month) + " " + str(d.day)

        f = urllib2.urlopen('https://www.wunderground.com/history/airport/KBKL/'+ str(d.year)+'/' + str(d.month)+'/' + str(d.day) +'/DailyHistory.html?&format=1')
        dataString = f.read()
    
        # entireDay contains string for entire day
        entireDay = dataString.rstrip().split('\n')
        day = []
        
        # loops through each hour of the day
        for i in range (2, len(entireDay)):
            #text for 1 hour
            hour = entireDay[i].split(',')
            
            hourData = [d.strftime('%m/%d/%Y'), hour[0], hour[1]]
            day.append(hourData)
        
        writer.writerows(day)
        d += datetime.timedelta(days=1)
    file1.close()
    
t1 = threading.Thread(target=getData, args=("2012",))
t2 = threading.Thread(target=getData, args=("2013",))
t3 = threading.Thread(target=getData, args=("2014",))
t4 = threading.Thread(target=getData, args=("2015",))
t5 = threading.Thread(target=getData, args=("2016",))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
