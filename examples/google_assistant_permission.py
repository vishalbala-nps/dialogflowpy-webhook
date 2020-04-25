"""
This is a Simple Demo to demonstrate requesting the User's Name and Location in Google Assistant
"""
from flask import *
import dialogflowpy_webhook
app = Flask(__name__)

app.route("/")
def main():
    request_handler = dialogflowpy_webhook.request_handler(request.get_json())
    response_handler = dialogflowpy_webhook.response_handler()
    intent = request_handler.get_intent_displayName()
    payload = request_handler.get_payload()

    if intent == "googperm":
        response_handler.google_assistant_ask_permisson("For Testing",["NAME", "DEVICE_PRECISE_LOCATION"])
    elif intent == "googafterperm":
        response_handler.google_assistant_response("I got the Permissions")
        response_handler.google_assistant_response("Your Name is "+payload["user"]["profile"]["displayName"])
        response_handler.google_assistant_response("Your Address is "+payload["device"]["location"]["formattedAddress"])
