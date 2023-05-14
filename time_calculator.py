def add_time(start, duration, day=None):
    startTime = sortStart(start)
    durTime = sortDuration(duration)
    #Calculate total minutes after first day
    TotalMins = startTime['minTot'] + durTime['minTot']
    #Convert to days then mins (1440 mins in day)
    minsOver = TotalMins % 1440
    daysOver = int((TotalMins-minsOver)/1440)
    #Calculate return value
    time = returnTime(minsOver)
    if daysOver==1:
        dayText = "(next day)"
    elif daysOver>1:
        dayText = "("+str(daysOver)+" days later)"
    else:
        dayText = ""
    
    #If day is given...
    if day!=None:
        dow = getDay(day, daysOver)
    else:
        dow=""
    new_time = time+dow+" "+dayText
    new_time = new_time.strip()
    return new_time

def sortStart(time):
    time1 = time.split(' ')
    time2 = time1[0].split(':')
    #calculate minutes after midnight
    if time1[1]=="PM":
        h = int(time2[0])+12
    elif time1[1]=="AM":
        h = int(time2[0])
    mins = (h*60)+int(time2[1])
    retval = {"h": time2[0], "m": time2[1], "ampm": time1[1], "minTot": mins}
    return retval

def sortDuration(time):
    time1 = time.split(':')
    mins = int(time1[0])*60+int(time1[1])
    retval = {"h": time1[0], "m": time1[1], "minTot": mins}
    return retval

def returnTime(minsIn):
    mins = minsIn % 60
    hours = int((minsIn - mins)/60)
    if hours>11:
        hours = hours - 12
        ampm = "PM"
    else:
        ampm = "AM"
    if hours == 0:
        hours = 12
    strMin = str(mins)
    if len(strMin)==1:
        strMin = "0"+strMin
    retval = str(hours)+":"+strMin+" "+ampm
    return retval

def getDay(day, daysOver):
    lower = day.lower()
    dow = {"monday":1, "tuesday":2, "wednesday":3, "thursday":4, "friday":5, "saturday":6, "sunday":7}
    dow2 = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 0:"Sunday"}

    #oldDay = dow[lower]
    oldDay = dow.get(lower)
    if oldDay==None:
        return ""
    newDay = oldDay + daysOver
    newDay = newDay % 7
    dayText = ", "+dow2[newDay]
    return dayText