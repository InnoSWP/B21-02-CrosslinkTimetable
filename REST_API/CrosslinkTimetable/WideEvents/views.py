from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from WideEvents.models import Event
from exchangelib import Credentials
from exchangelib import Mailbox
from exchangelib import DELEGATE, Account
import datetime
from exchangelib import Account, CalendarItem, Attendee, Mailbox

try:
    import zoneinfo
except ImportError:
    from backports import zoneinfo

def parse_date(date_str:str):
    current_date = date_str.split('T')[0]
    current_time = date_str.split('T')[1][:-1]
    
    year = int(current_date.split('-')[0])
    month = int(current_date.split('-')[1])
    day = int(current_date.split('-')[2])

    hour = int(current_time.split(':')[0])
    minute = int(current_time.split(':')[1])
    second = int(current_time.split(':')[2])

    return (year, month, day, hour, minute, second)


class EventAPIView(APIView):
    def get(self, request):
        university_events = list(Event.objects.all().values())
        return Response({'posts': university_events})
    
    def post(self, request):
        post_new = Event.objects.create(
            name=request.data['name'],
            content=request.data['content'],
            remind_before=request.data['remind_before'],
            place=request.data['place'],
            time_from=request.data['time_from'],
            time_to=request.data['time_to'],
            group_of_recipients=request.data['group_of_recipients']
        )

        subject = request.data['name']
        body = request.data['content']
        location = request.data['place']
        time_from=request.data['time_from']
        time_to=request.data['time_to']
        group_of_recipients=request.data['group_of_recipients']

        begin_year, begin_month, begin_day, begin_hour, begin_minute, begin_second = parse_date(time_from)
        end_year, end_month, end_day, end_hour, end_minute, end_second = parse_date(time_to)

        creds = Credentials(username='', password='')
        my_account = Account(
        primary_smtp_address='', credentials=creds,
        autodiscover=True, access_type=DELEGATE
        )

        a = my_account
        tz = zoneinfo.ZoneInfo('Europe/Moscow')
        calendar_items = []
        calendar_items.append(CalendarItem(
            start=datetime.datetime(begin_year, begin_month, begin_day, begin_hour, begin_minute, tzinfo=tz),
            end=datetime.datetime(end_year, end_month, end_day, end_hour, end_minute, tzinfo=tz),
            subject=subject,
            body=body,
            location=location,
            categories=['Wide Events'],
            required_attendees = [Attendee(
                mailbox=Mailbox(email_address=group_of_recipients),
                response_type='Accept'
            )]
        ))

        a.bulk_create(folder=a.calendar, items=calendar_items)

        return Response({'post': model_to_dict(post_new)})


def test_base_page(request):
    return render(request, "base.html")

def events(request):
    return render(request, "WideEvents/events.html")

def create_event(request):
    return render(request, "WideEvents/create-event.html")

def profile(request):
    return render(request, "WideEvents/profile.html")

def signin(request):
    return render(request, "WideEvents/signin.html")