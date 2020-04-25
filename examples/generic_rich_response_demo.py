"""
This is a Simple Demo to demonstrate Generic Rich Responses. The Response is Trigered by the intents.
"""
from flask import *
import dialogflowpy_webhook
app = Flask(__name__)

app.route("/")
def main():
    intent_handler = dialogflowpy_webhook.request_handler(request.get_json())
    response_handler = dialogflowpy_webhook.response_handler()

    intent = intent_handler.get_intent_displayName()
    if intent == "gentextresponse":
        #Note: Unlike generic_response, you can have multiple generic_rich_text_response
        response_handler.generic_rich_text_response("Hello! Here is a text Response")
        response_handler.generic_rich_text_response("Here is another one!")
    elif intent == "gencardresponse":
        #A Generic Card with Some text and an image
        response_handler.generic_card(title="Hello world!",subtitle="Here is a Card from Python!",imageURL="https://storage.googleapis.com/automotive-media/album_art.jpg")
    elif intent == "gencardwbtnresponse":
        response_handler.generic_card(title="Hello world!",subtitle="Here is a Card with buttons from Python!",imageURL="https://storage.googleapis.com/automotive-media/album_art.jpg")
        response_handler.generic_card_add_button("A link to Google","http://google.com")
    elif intent == "gensuggestions":
        response_handler.generic_add_suggestions(["Hello world!","Abc","Def"],title="Here are some suggestions")
    elif intent == "genimage":
        response_handler.generic_image("https://storage.googleapis.com/automotive-media/album_art.jpg","An Image")
        
    return jsonify(response_handler.create_final_response())