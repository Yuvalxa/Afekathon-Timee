from __future__ import print_function

import datetime
import os.path
import datetime

import google
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import google.protobuf
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file Yuval.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def get_DailyEvent(date, id):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file Yuval.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(id + '.json'):
        creds = Credentials.from_authorized_user_file(id + '.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(id + '.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=1000, singleEvents=True,
                                              orderBy='startTime').execute()
        print(events_result)
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return
        return events
        dailyEvent = []
        # Prints the start and name of the next 10 events
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            end = event['end'].get('dateTime', event['start'].get('date'))
            print(start)
            if start.split('T')[0] == date:
                dailyEvent.append(event)
        print(dailyEvent)
        return dailyEvent
    except HttpError as error:
        print('An error occurred: %s' % error)
    return None


def dayInCurrentWeek(date, start):
    start = start.split('T')[0]
    u = datetime.datetime.strptime(date, "%Y-%m-%d")
    s = datetime.datetime.strptime(start, "%Y-%m-%d")
    d = datetime.timedelta(days=7)
    check = u + d
    if u <= s <= check:
        return True
    else:
        return False


def get_WeekEvent(date, id):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file Token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(id + '.json'):
        creds = Credentials.from_authorized_user_file(id + '.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(id + '.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=100, singleEvents=True,
                                              orderBy='startTime').execute()
        print(events_result)
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return
        weekEvent = []
        # Prints the start and name of the next 10 events
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            end = event['end'].get('dateTime', event['start'].get('date'))
            print(start)
            day = start.split('T')[0].split('-')[2]
            if dayInCurrentWeek(date, start):
                weekEvent.append(event)
            # if type(int(day)) <= date:
        print(weekEvent)
        return weekEvent
    except HttpError as error:
        print('An error occurred: %s' % error)
        return None


def create_event(id, start, end, summary, description):
    creds = None
    # The file Token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(id + '.json'):
        creds = Credentials.from_authorized_user_file(id + '.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(id + '.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
        #
        # # Call the Calendar API
        # now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        # print('Getting the upcoming 10 events')
        # events_result = service.events().list(calendarId='primary', timeMin=now,
        #                                       maxResults=100, singleEvents=True,
        #                                       orderBy='startTime').execute()
        # print(events_result)
        # events = events_result.get('items', [])

        # if not events:
        #     print('No upcoming events found.')
        #     return
        event = {
            'summary': summary,
            'location': 'Central,Israel',
            'description': description,
            'start': {
                'dateTime': start,
                'timeZone': 'Asia/Jerusalem',
            },
            'end': {
                'dateTime': end,
                'timeZone': 'Asia/Jerusalem',
            },
            'recurrence': [
                'RRULE:FREQ=DAILY;COUNT=2'
            ],
            'attendees': [
                {'email': id},
            ],
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
        return event
    except HttpError as error:
        print('An error occurred: %s' % error)


# def main():
#     # get_DailyEvent('2022-05-12', 'Yuval')
#     # get_WeekEvent('2022-05-12', 'Yuval')
#     ##create_event('2022-05-12', 'asdf12@gmail.com', '2022-05-12T12:36:19', '2022-05-12T17:36:19', 'FirstTry', 'YESSSS')
#    # get_DailyEvent('2022-05-12', 'Yuval')
#
#
# if __name__ == '__main__':
#     main()