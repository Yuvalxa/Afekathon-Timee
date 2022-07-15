import datetime
from event import Event
import Day


def update_activity(activity: Event, current_activity_time: int, current_finish_time: int) -> None:
    activity.startTime = current_activity_time
    activity.endTime = current_finish_time


def __sortEventList__(event_list: list) -> list:
    event_list.sort(key=lambda x: x.priority)


def activity_inserter(activities: list, dayTime: int, startTime: int) -> list:
    """
    the function schedule activites for single day.
    returns the schedule for the day and the remaining activites that could'nt be scheduled.
    """
    new_schedule = []
    current_finish_time = 0  # keeps track of the lastest activity finish time
    current_activity_time = startTime

    for activity in activities:
        # check if current day have more study time left
        if dayTime <= 0:
            break
        if activity.duration <= dayTime:
            activities.remove(activity)
            current_finish_time = current_activity_time + activity.duration
            update_activity(activity, current_activity_time, current_finish_time)
            new_schedule.append(activity)
            dayTime -= activity.duration
            current_activity_time += activity.duration

    return (new_schedule, activities)


def schedule_day(day: Day, event_list: list) -> list:
    for event in event_list:
        event.startDate=day.date
        event.endDate=day.date
    # for event in day.allEvents:
    #     print("b1")
    #     print(type(day.starthour), type(event.endTime), event.endTime, day.starthour)
    #     if event.endTime > str(day.starthour)+":00:00":
    #         day.starthour = int(event.endTime.split(":")[0])
    #         print("b2")
    tup = activity_inserter(event_list, day.duration, day.starthour)
    day.allEvents = tup[0]
    day.addAllEvents()
    return tup[1]


def schedule(event_list: list, days: list) -> list:
    """
    goes through the event list and schedules task for each day by the availabe study time and priority
    """
    if event_list == None:
        return
    __sortEventList__(event_list)
    for day in days:
        if len(event_list) == 0:
            break
        print(str(day.date), "pp")
        date = datetime.datetime.strptime(str(day.date), "%Y-%m-%d")
        deadline = datetime.datetime.strptime(str(event_list[0].deadline), "%Y-%m-%d")
        if date > deadline:
            raise Exception("Not enough time to complete all activities")
        event_list= schedule_day(day, event_list)
        print(str(day.date), "end")
    if len(event_list) > 0:
        raise Exception("Not enough time to complete all activities")

    return days
