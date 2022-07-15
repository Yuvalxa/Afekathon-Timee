import mysql.connector
from event import Event
from data import *

parameterTypeDict = {"hw": 1, "test": 2}


def addDay(day):
    splited = day.split(" ")
    splited1 = splited[0].split("-")
    splited1[2] = int(splited1[2]) + 1
    newDate = (str(splited1[0]) + "-" + str(splited1[1]) + "-" + str(splited1[2]) + " " + str(splited[1]))
    print(newDate)
    return newDate


def addWeek(day):
    splited = day.split(" ")
    splited1 = splited[0].split("-")
    splited1[2] = int(splited1[2]) + 7
    newDate = (str(splited1[0]) + "-" + str(splited1[1]) + "-" + str(splited1[2]) + " " + str(splited[1]))
    print(newDate)
    return newDate


class sql():
    rows = None

    def __init__(self):
        self.con = mysql.connector.connect(host=host,
                                           user=user,
                                           password=password,
                                           database=database,
                                           port=port,
                                           auth_plugin=auth_plugin)
        self.cur = self.con.cursor()

    # Event Funcs
    def getEventsById(self, id):
        self.rows = self.cur.execute(
            "select * from events where eventId = " + str(id))
        self.rows = self.cur.fetchall()
        for r in self.rows:
            return (Event(r[0], startDate=str(r[2]).split(" ")[0], endDate=str(r[3]).split(" ")[0],
                          startTime=str(r[2]).split(" ")[1],
                          endTime=str(r[3]).split(" ")[1], description=r[4], summery=r[1], priority=r[6],
                          category="basic", isDone=bool(r[7]), mail=r[5]))

    def getAllDayEvents(self, day, userEmail):
        dayEvents = []
        nextday = addDay(day)
        self.rows = self.cur.execute(
            "select * from events where userEmail = '" + userEmail + "'" + " and startTime between '" + day + "' and '" + nextday + "' and isDone = 0")
        self.rows = self.cur.fetchall()
        for r in self.rows:
            dayEvents.append(Event(r[0], startDate=str(r[2]).split(" ")[0], endDate=str(r[3]).split(" ")[0],
                                   startTime=str(r[2]).split(" ")[1],
                                   endTime=str(r[3]).split(" ")[1], description=r[4], summery=r[1], priority=r[6],
                                   category="basic", isDone=bool(r[7]), mail=r[5]))
            return dayEvents

    def getAllUserEvents(self, userEmail):
        alluserEvents = []
        self.rows = self.cur.execute(
            "select * from events where userEmail = '" + userEmail)
        self.rows = self.cur.fetchall()
        for r in self.rows:
            alluserEvents.append(Event(r[0], startDate=str(r[2]).split(" ")[0], endDate=str(r[3]).split(" ")[0],
                                       startTime=str(r[2]).split(" ")[1],
                                       endTime=str(r[3]).split(" ")[1], description=r[4], summery=r[1], priority=r[6],
                                       category="basic", isDone=bool(r[7]), mail=r[5]))
            return alluserEvents

    def getAllEvents(self):
        allEvents = []
        self.rows = self.cur.execute("select * from events ")
        self.rows = self.cur.fetchall()
        for r in self.rows:
            allEvents.append(Event(r[0], startDate=str(r[2]).split(" ")[0], endDate=str(r[3]).split(" ")[0],
                                   startTime=str(r[2]).split(" ")[1],
                                   endTime=str(r[3]).split(" ")[1], description=r[4], summery=r[1], priority=r[6],
                                   category="basic", isDone=bool(r[7]), mail=r[5]))
        return allEvents

    def getAllweekEvents(self, day, userEmail):
        weekEvents = []
        nextday = addWeek(day)
        self.rows = self.cur.execute(
            "select * from events where userEmail = '" + userEmail + "'" + " and startTime between '" + day + "' and '" + nextday + "' and isDone = 0")
        self.rows = self.cur.fetchall()
        for r in self.rows:
            weekEvents.append(
                Event(r[0], startDate=r[2].split(" ")[0], endDate=r[3].split(" ")[0], startTime=r[2].split(" ")[1],
                      endTime=r[3].split(" ")[1], description=r[4], summery=r[1], priority=r[6], category="basic",
                      isDone=bool(r[7]), mail=r[5]))
        return weekEvents

    def insertNewEvent(self, name, startTime, endTime, eventDescription, userEmail, eventPriority, isDone):
        print(name, startTime, endTime, eventDescription, userEmail, eventPriority, isDone)
        mySql_insert_query = "insert into events (eventName, startTime, endTime, eventDescription, userEmail, " + \
                             "eventPriority, isDone) " + \
                             "values ('" + str(name) + "','" + str(startTime) + "','" + str(endTime) + "','" + \
                             str(eventDescription) + "','" + str(userEmail) + "'," + str(eventPriority) + "," + str(int(isDone)) + ")"
        print("hi0")
        self.rows = self.cur.execute("insert into events (eventName, startTime, endTime, eventDescription, userEmail,eventPriority, isDone) values ('" + str(name) + "','" + str(startTime) + "','" + str(endTime) + "','" + str(eventDescription) + "','" + str(userEmail) + "'," + str(eventPriority) + "," + str(int(isDone)) + ")")
        print("hi")
        self.con.commit()

    def updateEvent(self, event):
        print("hi")
        startdateTime = str(event.startDate) + " " + str(event.startTime)
        endDateTime = str(event.endDate) + " " + str(event.endTime)
        mySql_update_query = "update events set eventName= '" + event.summery + "', startTime= '" + str(startdateTime) + "', endTime='" + str(endDateTime) + "', eventDescription='" + str(event.description) + "', eventPriority=" + str(event.priority) + ", isDone = " + str(1) + " where eventId = " + str(event.id)
        print("hi1")
        self.rows = self.cur.execute(mySql_update_query)
        print("hi2")

        self.con.commit()

    # Statistics Funcs
    def getAllCategory(self):
        self.cur.execute("select distinct parameterName from statistics")
        rows = self.cur.fetchall()
        for r in rows:
            print(str(r[0]))

    def getCategoryAvg(self, category, type):
        self.cur.execute(
            "select parameterEvg from statistics where parameterName = '" + category + "' and parameterType = " + str(
                parameterTypeDict[type]))
        rows = self.cur.fetchall()
        for r in rows:
            print(str(r[0]))

    def getNextId(self):
        self.cur.execute("select eventId from events order by eventId desc limit 1")
        rows = self.cur.fetchall()
        for r in rows:
            return r[0] + 1

    def updateAvg(self, categoryName, newTime):
        self.cur.execute("select * from statistics where parameterName = '" + categoryName + "'")
        rows = self.cur.fetchall()
        oldAvg = rows[0][2]
        oldnums = rows[0][3]
        newAvg = (oldAvg * oldnums + newTime) / (oldnums + 1)
        mySql_update_query = "update statistics set parameterEvg= '" + str(newAvg) + "', numOfStats= '" + str(
            oldnums + 1) + " " + " where parameterName = " + categoryName + "'"
        self.rows = self.cur.execute(mySql_update_query);
        self.con.commit()

    def getDuration(self, categoryName):
        self.cur.execute("select parameterEvg from statistics where parameterName = '" + categoryName + "'")
        rows = self.cur.fetchall()
        for r in rows:
            return r[0]


myDB = sql()
