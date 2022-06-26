from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from exchangelib import Message, Mailbox, Credentials, Account, DELEGATE
from credentials import login, password

class DoEEmailsAPIView(APIView):
    def post(self, request):
        group_of_recipients = request.data['group_of_recipients']
        group_of_recipients_cc = request.data['group_of_recipients_cc']

        attendees_students = ['i.orekhov@innopolis.university', 'd.alekhin@innopolis.university',
                     'i.ezhova@innopolis.university']
        if group_of_recipients == 'Students':
            group_of_recipients = list(map(lambda x: Mailbox(email_address=x), attendees_students))

        subject = request.data['subject']
        content = request.data['content']

        creds = Credentials(username=login, password=password)
        my_account = Account(
            primary_smtp_address=login, credentials=creds,
            autodiscover=True, access_type=DELEGATE
        )

        m = Message(
            account=my_account,
            subject=subject,
            body=content,
            to_recipients=group_of_recipients,
            cc_recipients=['carl@example.com', 'denice@example.com'],
        )
        m.send()

        return Response({"resp": 200})
