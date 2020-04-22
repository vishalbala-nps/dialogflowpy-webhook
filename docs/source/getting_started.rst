************************
Getting Started
************************
This Page gives instructions to create a basic bot

Installation
#############
.. code-block:: shell

   pip3 install dialogflowpy flask

.. note:: For this example, we are using Flask. You can use any python web framework (like Django, Bottle etc). Installing Flask is not a must for dialogflowpy to work

Server Setup
#############
Dialogflow has a few requirements for the webhook service. Your Webhook must have a public URL and must have an SSL certificate. There are many options for this. You can use services like Heroku, NGROK, Pythonanywhere etc. Your webhook code must be hosted on such sites and you should note the URL

Basic Fulfillment code
#######################
Create a new file (bot.py and paste the code into it)

.. code-block:: python

   from flask import Flask,request
   import dialogflowpy
   app = Flask(__name__)

   app.route("/fulfillment")
   def fulfillment():
      response_handler = dialogflowpy.response_handler()
      response_handler.generic_response("Hello from Python!")
      return response_handler.create_final_response()

    if __name__ == "__main__":
      app.run()

This code handles our webhook. This file should be hosted on the services listed above

Dialogflow Setup
#################
* Sign in to `Dialogflow <https://console.dialogflow.com/>`_
* Create a new `agent <https://console.dialogflow.com/api-client/#/newAgent>`_ with any name of your choice and set the timezone to your home timezone and click on "Save"
* After creating the agent, go to fulfillment and enter the URL where your app is located and click on "Save"

Testing
#######
For this example, we will be testing using Actions on Google. 

* In the Console, click on "Intergrations" and click on Google Assistant -> Test. This will take you to Actions on Google Console. There, in the simulator, type "Talk to my Test App" and Google should say "Hello from Python!"