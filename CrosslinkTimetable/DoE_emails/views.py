from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from exchangelib import Message, Mailbox, Credentials, Account, DELEGATE
from credentials import login, password

from sqlite3 import connect


class DoEEmailsAPIView(APIView):
    def post(self, request):
        group_of_recipients = request.data['group_of_recipients']
        group_of_recipients_cc = request.data['group_of_recipients_cc']

        conn = connect('../CrosslinkTimetable/db.sqlite3')
        cursor = conn.cursor()

        if group_of_recipients == 'Students':
            receiver = list(map(lambda x: x[0], cursor.execute("SELECT * FROM Students").fetchall()))
            group_of_recipients = list(map(lambda x: Mailbox(email_address=x), receiver))
        elif group_of_recipients == 'Teachers':
            receiver = list(map(lambda x: x[0], cursor.execute("SELECT * FROM Teachers").fetchall()))
            group_of_recipients = list(map(lambda x: Mailbox(email_address=x), receiver))

        print(group_of_recipients)

        conn.close()

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
            # cc_recipients=['carl@example.com', 'denice@example.com'],
        )
        m.send()

        return Response({"resp": 200})
