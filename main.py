# We import all necessary libraries for the REST API
from flask import Flask
from flask_restful import Api, Resource, reqparse

# We are setting the keys for parsing the requests about wide events
task_post_args_wide_events = reqparse.RequestParser()
task_post_args_wide_events.add_argument("name", type=str, help="Name is required", required=True)
task_post_args_wide_events.add_argument("description", type=str)
task_post_args_wide_events.add_argument("time_from", type=str, help="Beginning time is required", required=True)
task_post_args_wide_events.add_argument("time_to", type=str, help="Ending time is required", required=True)
task_post_args_wide_events.add_argument("remind_before", type=str, help="Time for reminding is required", required=True)
task_post_args_wide_events.add_argument("group_of_recipients", type=str, help="Group of recipients is required",
                                        required=True)
task_post_args_wide_events.add_argument("special_notes", type=str)

# We keep our events in this dictionary (then we will keep all data in database)
events = {
    1: {
        "name": "Spring Ball 2022",
        "description": "The best and the most lovely event in Spring semester",
        "time_from": "May 26",
        "time_to": "May 27",
        "remind_before": "3 days",
        "group_of_recipients": "Students",
        "special_notes": "Bring a lot of food"
    }
}


# We handle our requests about wide events in this class
class WideEvents(Resource):
    # This function handles the GET requests about wide events
    def get(self, event_id):
        # If there is no such event that was added before, then we return the 404 code (Not found)
        if event_id not in events:
            return "This event is not planned yet", 404

        # Otherwise, we return this record and 200 code (OK)
        return events[event_id], 200

    # This function handles the POST requests about wide events
    def post(self, event_id):
        # We parse the parameters from the request
        args = task_post_args_wide_events.parse_args()

        # If there is such event that was added before, then we return the 409 code (Conflict)
        if event_id in events:
            return "This event is already planned", 409

        # Otherwise, we make the new record in our dictionary and return the 201 code (Created)
        events[event_id] = args
        return events[event_id], 201

    # This function handles the PUT requests about wide events
    def put(self, event_id):
        # We parse the parameters from the request
        args = task_post_args_wide_events.parse_args()

        # If there is no such event that was added before, then we return the 404 code (Not found)
        if event_id not in events:
            return "This event is not planned yet", 404

        # Otherwise, we update the record in our dictionary and return the 202 code (Accepted)
        events[event_id] = args
        return events[event_id], 202

    # This function handles the DELETE requests about wide events
    def delete(self, event_id):
        # If there is no such event that was added before, then we return the 404 code (Not found)
        if event_id not in events:
            return "This event is not planned yet", 404

        # Otherwise, we delete the record in our dictionary and return the 202 code (Accepted)
        del events[event_id]
        return "Successfully deleted the event", 202


# We are setting the keys for parsing the requests about emails
task_post_args_emails = reqparse.RequestParser()
task_post_args_emails.add_argument("group_of_recipients", type=str, help="Group of recipients is required",
                                   required=True)
task_post_args_emails.add_argument("copy", type=str)
task_post_args_emails.add_argument("theme", type=str, help="Theme is required", required=True)
task_post_args_emails.add_argument("content", type=str, help="Content is required", required=True)
task_post_args_emails.add_argument("files", type=str)

# We keep our mails in this dictionary (then we will keep all data in database)
mails = {
    1: {
        "group_of_recipients": "Students",
        "copy": "Employees",
        "theme": "New cost for dormitory",
        "content": "Students",
        "files": "Schedule",
    }
}


# We handle our requests about DoE emails in this class
class DoeEmails(Resource):
    # This function handles the GET requests about DoE emails
    def get(self, mail_id):
        # If there is no such mail that was sent before, then we return the 404 code (Not found)
        if mail_id not in mails:
            return "This mail is not sent yet", 404

        # Otherwise, we return this record and 200 code (OK)
        return mails[mail_id], 200

    # This function handles the POST requests about DoE emails
    def post(self, mail_id):
        # We parse the parameters from the request
        args = task_post_args_emails.parse_args()

        # If there is such mail that was sent before, then we return the 409 code (Conflict)
        if mail_id in mails:
            return "This mail is already sent", 409

        # Otherwise, we return this record and 202 code (Accepted)
        mails[mail_id] = args
        return mails[mail_id], 202


# We declare the instance of our app and set up the API
app = Flask(__name__)
api = Api(app)

# We set up the links to the classes
api.add_resource(WideEvents, "/wide-events/<int:event_id>")
api.add_resource(DoeEmails, "/doe-emails/<int:mail_id>")

if __name__ == '__main__':
    app.run(debug=True)
