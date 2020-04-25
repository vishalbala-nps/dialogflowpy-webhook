"""
This is a Simple Demo to demonstrate Saving and retriving data from a Context
"""
from flask import *
import dialogflowpy_webhook
app = Flask(__name__)

app.route("/")
def main():
    request_handler = dialogflowpy_webhook.request_handler(request.get_json())
    response_handler = dialogflowpy_webhook.response_handler()
    intent = request_handler.get_intent_displayName()
    sesid = request_handler.get_session_id() #Session ID is required for saving data to a context

    if intent == "askcontext":
        response_handler.generic_response("Hello. I am saving data to a contect")
        response_handler.add_context(sesid,"mycontext",lifespan=5,params={"param1":"value1"})
    elif intent == "getcontext":
        cntxt = request_handler.get_context_by_name("mycontext")
        response_handler.generic_response("Here is the data from the context "+cntxt["parameters"]["param1"])
