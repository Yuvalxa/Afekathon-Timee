from event import Event
from sqlConnection import sql
from Day import Day
import scheduler
import datetime
import random


class controller:
    def __init__(self, view=None, model=None):
        self.view = view
        # self.model = model
        self.days = []
        self.mail = 'yuvalsmastey@gmail.com'
        self.sql = sql()
        self.fillDays(self.mail)
        self.loadExistingEvents(self.mail)

    def fillDays(self, mail: str = None):
        start_date = datetime.date(2022, 5, 13)
        end_date = datetime.date(2022, 5, 31)
        delta = datetime.timedelta(days=1)
        while start_date < end_date:
            curr = start_date
            start_time = 14
            end_time = start_time
            while end_time <= start_time:
                end_time = 22

            current_day = Day(curr, mail, start_time, end_time)
            if mail is not None:
                current_day.id = self.mail
            start_date += delta
            self.days.append(current_day)

    def loadExistingEvents(self, mail: str):
        all_events = self.sql.getAllEvents()
        # self.days = self.fillDays(mail)
        for idx, day in enumerate(self.days):
            for event in all_events:
                if self.mail == mail and event.startDate == str(day.date):
                    self.days[idx].allEvents.append(event)
            # if day.push:
            #     day.addAllEvents()
            #     day.push = False
            scheduler.__sortEventList__(day.allEvents)
        pass

    pass

    #### Event Model UI interaction ####
    def getEventsFromModelOnDate(self, date) -> list:
        for day in self.days:
            if str(day.date) == date:
                return day.allEvents

    def getEventFromId(self, id: str, mail=None):  # !!
        for day in self.days:
            event = day.findEvent(id)
            if event is not None:
                return event
        return None

    #### Event Primitives ####
    def getStartDateFromEvent(self, e: Event) -> str:
        return e.startDate

    def getEndDateFromEvent(self, e: Event) -> str:
        return e.endDate

    def getStartTimeFromEvent(self, e: Event) -> str:
        return e.startTime

    def getEndTimeFromEvent(self, e: Event) -> str:
        return e.endTime

    def getsummeryTimeFromEvent(self, e: Event) -> str:
        return e.summery

    def getIdFromEvent(self, e: Event) -> str:
        print("controller says id is: ", str(e.id))
        return str(e.id)

    def getDeadlineFromEvent(self, e: Event) -> str:
        return e.deadline

    def getPriorityFromEvent(self, e: Event) -> str:
        return e.priority

    def getIsTestFromEvent(self, e: Event) -> str:
        return e.isTest

    def getIsStudyFromEvent(self, e: Event) -> str:
        return e.isStudy

    def getCategoryFromEvent(self, e: Event) -> str:
        return e.category

    def getIsDoneFromEvent(self, e: Event) -> str:
        return e.category

    def getFormalsummeryFromEvent(self, e: Event):
        if e.isDone:
            return strike(e.summery + " " + e.startTime + " " + e.endTime)
        return e.summery + " " + e.startTime + " " + e.endTime

    def getIDFromEvent(self, e: Event):
        return e.id

    def getFormalEventssummerys(self, date: str) -> str:
        return [self.getFormalsummeryFromEvent(event) for event in self.getEventsFromModelOnDate(date)]

    def fireUpdate(self):
        self.days = []
        self.fillDays(self.mail)
        self.loadExistingEvents(self.mail)

    def dorGet(self, date: str):
        self.fireUpdate()
        if self.getEventsFromModelOnDate(date) == None:
            return
        lst = []
        for i in self.getEventsFromModelOnDate(date):
            lst.append((self.getFormalsummeryFromEvent(i), self.getIsDoneFromEvent(i), self.getIDFromEvent(i)))
        return lst

    def updateEvent(self, id: str, start: str, end: str):
        e: Event = None
        for day in self.days:
            for event in day.allEvents:
                print("hi in update event", type(id), type(event.id))
                if str(event.id) == id:
                    day.updateEvent(id, start, end)
                    print("aaaaaaaa")
                    e = event
                    break
        print("hi in update event out of for", e.id)
        self.sql.updateEvent(e)

    def dorCreateEvent(self, name: str, deadline: str, priority: str):
        print("a")
        dur = self.sql.getDuration("Calculus")
        print("b")
        id = self.sql.getNextId()
        e = Event(id, deadline=deadline, summery=name, priority=priority, duration=dur)
        print("c")
        self.days = scheduler.schedule([e], self.days)
        print("aaa")
        newE = self.getEventFromId(id, self.mail)

        self.sql.insertNewEvent(e.summery, str(newE.startDate) + " " + str(newE.startTime) + ":00:00",
                                str(newE.endDate) + " " + str(newE.endTime) + ":00:00", " ", self.mail, e.priority,
                                e.isDone)
        print(e.startTime + e.endTime)


def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result
