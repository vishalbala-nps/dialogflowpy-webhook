"""
This is a Simple Demo to demonstrate Google Assistant Rich Responses. The Response is Trigered by the intents.
"""
from flask import *
import dialogflowpy_webhook
app = Flask(__name__)

app.route("/")
def main():
    request_handler = dialogflowpy_webhook.request_handler(request.get_json())
    response_handler = dialogflowpy_webhook.response_handler()
    intent = request_handler.get_intent_displayName()
    capabilities = request_handler.get_capabilities()
    if intent == "googresponse":
        response_handler.google_assistant_response("Hello World!")
    elif intent == "googcardresponse":
        response_handler.google_assistant_response("Here is a Card")
        response_handler.google_assistant_card(title="Hello world!",subtitle="Here is a Card from Python!",imageURL="https://storage.googleapis.com/automotive-media/album_art.jpg",imageAlt="An image")
    elif intent == "googcardwbuttonresponse":
        response_handler.google_assistant_response("Here is a Card with buttons")
        response_handler.google_assistant_card(title="Hello world!",subtitle="Here is a Card from Python!",imageURL="https://storage.googleapis.com/automotive-media/album_art.jpg",imageAlt="An image",btnName="This is a link to Google",btnLink="http://www.google.com")
    elif intent == "googsuggestions":
        response_handler.google_assistant_response("Here are some suggestions")
        response_handler.google_assistant_add_suggestions(["Hello World!","Abc"])
    elif intent == "googcarousel":
        if "actions.capability.WEB_BROWSER" in capabilities: #Checks if actions.capability.WEB_BROWSER is available. If not, returns a fallback error message
            response_handler.google_assistant_response("Here is a Carousel")
            response_handler.google_assistant_new_carousel()
            response_handler.google_assistant_carousel_add_item(title="Item 1", url="http://google.com", imageURL="https://storage.googleapis.com/automotive-media/album_art.jpg", imgalt="An Image")
            response_handler.google_assistant_carousel_add_item(title="Item 2", url="http://google.com", imageURL="https://storage.googleapis.com/automotive-media/album_art.jpg", imgalt="An Image")
        else:
            response_handler.google_assistant_response("Sorry, Carousels do not work on your device!")
    elif intent == "googtable":
        response_handler.google_assistant_response("Here is a Table")
        response_handler.google_assistant_new_table()
        response_handler.google_assistant_table_add_header_row(["header1","header2","header3"])
        response_handler.google_assistant_table_add_row(["item1","item2","item3"],True)
        response_handler.google_assistant_table_add_row(["item1","item2","item3"],False)
    elif intent == "googmedia":
        response_handler.google_assistant_response("Here is a Media Response")
        response_handler.google_assistant_media_response(mediaURL="https://storage.googleapis.com/automotive-media/Jazz_In_Paris.mp3",description="A Jass Song",displayName="A Jass in Paris")
    return jsonify(response_handler.create_final_response())