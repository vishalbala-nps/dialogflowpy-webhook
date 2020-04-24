************************
Welcome to dialogflowpy
************************
dialogflowpy is a Python module for parsing and creating `Dialogflow <http://www.dialogflow.com/>`_ Webhook Requests and Responses. dialogflowpy serves as an 
SDK for creating Dialogflow bots which can be used with platforms like Actions on Google, Telegram etc.

Features
#########
* Parsing Dialogflow requests and get details like Intent, Slot Values, Contexts and more!
* Supports creation of Responses like: Text Responses, Cards, Quick Replies and Images 
* Supports creation of all `Google Assistant Rich Responses <https://cloud.google.com/dialogflow/docs/intents-rich-messages>`_

A simple Bot with dialogflowpy and Flask
########################################
.. code-block:: python

   from flask import Flask,request
   import dialogflowpy
   app = Flask(__name__)

   app.route("/fulfillment")
   def fulfillment():
      response_handler = dialogflowpy.response_handler()
      response_handler.generic_response("Hello from Python!")
      return response_handler.create_final_response()

The snippet above will make a dialogflow bot reply "Hello from Python!" whenever invoked.

Resources
##########

* Head over to the Getting Started section to create a Dialogflow bot with dialogflowpy
* Take a look at the Module Reference which contains all the modules available in dialogflowpy

Table of Contents
##################

.. toctree::
   :maxdepth: 2

   getting_started
   module_reference
