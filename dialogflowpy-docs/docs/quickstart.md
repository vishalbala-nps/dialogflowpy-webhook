# Quickstart
This is a quickstart guide for creating a Dialogflow fulfillment using dialogflowpy and Flask
## Requirements

- Your program must be hosted in the cloud (eg. Heroku) and Must support SSL
- A Google Account to Login to Dialogflow

## Dialogflow Setup

- Go to the [Dialogflow](https://www.dialogflow.com) website and click on "Go To Console". If this is the first time you are using Dialogflow, you will need to Sign in with Google
- After signing in, click on Create Agent. You will just need to fill in the agent name, timezone and language and click on Create Agent
- After creating the agent, you will be in the intents page. Click on "Default Welcome Intent" and under fulfillment, click on "Enable Webhook Call for this Intent" and "Enable Webhook Call for Slot Filling". You will need to this for all intents which you want to come to your Web server. Click on the trash button over "Text Response" to delete all the responses. After that, click on Save

## Fulfillment Setup
### Deployment
Now that you have setup in Dialogflow, we need to manage the fulfillment. Create a folder and create the following files

- Python Program (app.py)
```
import dialogflowpy
from flask import *

app = Flask(__name__)

app.route("/",methods=["POST"])
def main():
    intent_handler = dialogflowpy.intent_handler(request.get_json())
    response_handler = dialogflowpy.response_handler()
    intent = intent_handler.get_intent()
    if intent == "Default Welcome Intent":
        response_handler.genericResponse("Hello From Python!")
```
- requirements.txt
```
flask
dialogflowpy
gunicorn
```
After creating these files, deploy them to the cloud service and make a note of the URL. As these steps change from provider to provider, I can't list them out here. The command to run the server is `gunicorn app:app` and the command to run before this is `pip3 install -r requirements.txt` to install all the required modules
### Dialogflow Fulfillment cofiguration
After deploying to your cloud service, we need to configure in Dialogflow. Go to Fulfillment (located in the sidebar) and enable Webhook. Paste the URL of the cloud service copied earlier under URL and click on Save
### Testing
After entering the webhook URL, click on Integrations (located in the sidebar) and click on Google Assistant and click on Test. This will take you to the Google Assistant emulator. Type "Talk to my Test App" and you should get "Hello from Python!" back
## Next Steps
Now that you have created a basic App, you may want to look at the [Module Reference](/module_reference) for more features of this module