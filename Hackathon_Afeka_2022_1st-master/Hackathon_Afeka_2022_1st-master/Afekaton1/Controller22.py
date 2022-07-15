from event import Event

e1 = Event("123", "2222")
e1.startTime = "5:00:00"
e1.endTime = "8:00:00"
e2 = Event("124", "2222")
e2.startTime = "8:00:00"
e2.endTime = "12:00:00"
e3 = Event("125", "2222")
e3.startTime = "12:00:00"
e3.endTime = "16:00:00"
thisEvents = {"123" : e1, "124": e2, "125": e3}

class controller:
    def __init__(self, view=None, model=None):
        self.view = view
        self.model = model

    #### Event Model UI interaction ####
    def getEventsFromModelOnDate(self, date) -> list: # same day
        print("in contrtoller: ", date)
        tasks = [("Calcules 1", False, "123"), ("Liiner Algebra HW2", False, "124"),
                 ("Intro To Java HW1", False, "125"), ("Descrete Mathematics HW3", False, "127"),
                 ("Watch Video", False, "128")]

        return tasks

    def getEventsFromModelWeek(self, date): # model returns list of all week's events from date
        pass

    def CreateEventToModel(self, e: Event):
        pass

    def UpdateEventToModel(self, before: Event, after: Event):
        pass

    def getEventFromId(self, id: str, mail: str):
        print("hi", thisEvents[id])
        return thisEvents[id]

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
        return e.id

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

    def getFormalEventsSummery(self, date: str) -> str:
        return [self.getFormalsummeryFromEvent(event) for event in self.getEventsFromModelOnDate(date)]

    def dorGet(self, date: str):
        return [(self.getFormalsummeryFromEvent(i), self.getIsDoneFromEvent(i), self.getIDFromEvent(i))
                for i in self.getEventsFromModelOnDate(date)]


def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result