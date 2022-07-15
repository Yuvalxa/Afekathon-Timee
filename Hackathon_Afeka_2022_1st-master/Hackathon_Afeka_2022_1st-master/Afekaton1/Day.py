from event import Event
import GoogleCalanderAPI
import datetime


class Day:
    def __init__(self, date, id, starthour, endhour):
        self.date = date
        self.allEvents = []
        self.id = id
        self.starthour = starthour
        # time_1 = datetime.datetime.strptime(starthour, '%H:%M:%S')
        # time_2 = datetime.datetime.strptime(endhour, '%H:%M:%S')
        # print(time_1, time_2)
        self.duration = endhour - starthour
        self.push= True

    # def getEvents(self):
    #     events = GoogleCalanderAPI.get_DailyEvent(self.date, self.id)
    #     for event in events:
    #         #    def __init__(self, id, event,priority,deadline,category,isTest,isStudy):
    #         ev = Event(self.id, event, '1','deadline','Mathmathics',True,False,True)
    #         self.allEvents.append(ev)

    def addAllEvents(self):
        for event in self.allEvents:
            self.addEvent(event.id,event.startDate, event.startTime, event.endDate, event.endTime, event.summery,
                          event.description, event.priority, event.deadline, event.category, event.isTest,
                          event.isStudy, event.isDone)

    def addEvent(self,id, startDate, startTime, endDate, endTime, summery, description, priority, deadline, category,
                 isTest, isStudy, isDone):
        ev = Event(id,mail=self.id, startDate=startDate, endDate=endDate, startTime=startTime, endTime=endTime,
                   summery=summery, description=description, priority=priority, deadline=deadline, category=category,
                   isTest=isTest, isStudy=isStudy, isDone=isDone)
        if isinstance(startTime,str):
            GoogleCalanderAPI.create_event(self.id, startDate + "T" + startTime, endDate + "T"
                                           + endTime, summery, description)
        else:
            GoogleCalanderAPI.create_event(self.id, str(startDate) + "T" + str(startTime)+":00:00", str(endDate) + "T"
                                       + str(endTime)+":00:00", summery, description)
        print("a")
        # 2015-05-28T09:00:00-07:00

    def findEvent(self, id):
        for event in self.allEvents:
            if event.id == id:
                return event
        return None

    def updateEvent(self, id, StartTime, endTime):
        event: Event = self.findEvent(id)
        if event is not None:
            event.StartTime = StartTime
            event.endTime = endTime
            event.isDone = True
            return True
        return False


# a = Day('2022-05-13', 'asfd12@gmail.com', '08:00:00', '22:00:00')

# a.addEvent('2022-05-13', '09:00:00', '2022-05-13', '21:00:00', 'TestTESTETETETETETES', 'MOSHE', '5', 'dealine', 'Math',
#            True, True, True)
# print(a.allEvents)
