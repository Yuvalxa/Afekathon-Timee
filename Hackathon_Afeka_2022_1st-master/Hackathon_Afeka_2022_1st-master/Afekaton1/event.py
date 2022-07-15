class Event:
    def __init__(self, id,mail=None, event=None,startDate=None,endDate=None,startTime=None,endTime=None,description=None,summery=None,priority=None,deadline=None,category=None,isTest=None,isStudy=None,isDone=False,duration=None):
        self.id = id
        self.mail=mail
        self.startTime = None
        self.startDate = None
        self.endTime = None
        self.endDate = None
        self.summery = None
        self.description = None
        if event is not None:
            self.gets_start(event)
            self.get_end(event)
            self.get_summary(event)
        else:
            self.startDate = startDate
            self.startTime = startTime
            self.endDate =endDate
            self.endTime=endTime
            self.description = description
            self.summery = summery
        self.priority = priority
        self.category = category
        self.deadline=deadline
        self.isTest =isTest
        self.isStudy = isStudy
        self.isDone = isDone
        self.duration = duration

    def gets_start(self, event):
        start = event['start'].get('dateTime', event['start'].get('date'))
        self.startTime = start.split('T')[1].split('.')[0]
        self.startDate = start.split('T')[0]
        return None

    def get_end(self, event):
        start = event['end'].get('dateTime', event['end'].get('date'))
        self.endTime = start.split('T')[1].split('.')[0]
        self.endDate = start.split('T')[0]
        return None

    def get_summary(self, event):
        self.summery = event['summary']
        self.description = event['description']
        return None

