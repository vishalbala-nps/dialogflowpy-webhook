"""
This is a Simple Demo to demonstrate handling multiple intents. Depending on the intent, the response
is different. 
"""
from flask import *
import dialogflowpy_webhook
app = Flask(__name__)

app.route("/")
def main():
    intent_handler = dialogflowpy_webhook.request_handler(request.get_json())
    response_handler = dialogflowpy_webhook.response_handler()

    intent = intent_handler.get_intent_displayName()
    if intent == "intent1":
        response_handler.generic_response("You have triggered intent1")
    elif intent == "intent2":
        response_handler.generic_response("You have triggered intent2")
    return jsonify(response_handler.create_final_response())