********************************
Welcome to dialogflowpy-webhook
********************************

.. image:: https://readthedocs.org/projects/dialogflowpy-webhook/badge/?version=latest
   :target: https://dialogflowpy-webhook.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://img.shields.io/pypi/v/dialogflowpy-webhook
   :target: https://pypi.org/project/dialogflow-fulfillment/
   :alt: Pypi Badge

.. image:: https://img.shields.io/github/issues/vishalbala-nps/dialogflowpy-webhook
   :target: https://github.com/vishalbala-nps/dialogflowpy-webhook/issues
   :alt: Github issues

.. image:: https://img.shields.io/pypi/pyversions/dialogflowpy-webhook
   :alt: Python version

.. image:: https://img.shields.io/github/license/vishalbala-nps/dialogflowpy-webhook
   :target: https://github.com/vishalbala-nps/dialogflowpy-webhook/
   :alt: license

.. image:: https://img.shields.io/pypi/dd/dialogflowpy-webhook
   :alt: PyPI - Downloads

A Python module for parsing and creating Requests and Responses of Dialogflow Fulfillment Library. The `Dialogflow Fulfillment Library <https://cloud.google.com/dialogflow/docs/fulfillment-overview>`_ allows you to connect natural language understanding and processing to your own system. Using Fulfillment, you can surface commands and information from your services to your users through a natural conversational interface.

This dialogflowpy-webhook module is intended to help build Python Dialogflow Fulfillment for multiple `integrations <https://cloud.google.com/dialogflow/docs/integrations/>`_ including Google Assistant, Facebook and Telegram. It is expected to work for Slack and Line as well.

Features
#########
* Parsing Dialogflow requests and get details like Intent, Slot Values, Contexts and more!
* Supports creation of Responses like: Text Responses, Cards, Quick Replies/Suggestions and Images 
* Supports creation of all `Google Assistant Rich Responses <https://cloud.google.com/dialogflow/docs/intents-rich-messages>`_

A simple Bot with dialogflowpy-webhook and Flask
#################################################
.. code-block:: python

   from flask import Flask,request
   import dialogflowpy_webhook as dfw
   app = Flask(__name__)

   app.route("/fulfillment")
   def fulfillment():
      response_handler = dfw.response_handler()
      response_handler.generic_response("Hello from Python!")
      return response_handler.create_final_response()

The snippet above will make a dialogflow bot reply "Hello from Python!" whenever invoked.

Resources
##########

* Head over to the Getting Started section to create a Dialogflow bot with dialogflowpy_webhook
* Take a look at the Module Reference which contains all the modules available in dialogflowpy_webhook
* Take a look at the examples `here <https://github.com/vishalbala-nps/dialogflowpy-webhook/tree/master/examples>`_ which contain some use cases for many functions

Reporting Bugs
###############
In case of any problems or suggestions with this module, feel free to open a `Github Issue <https://github.com/vishalbala-nps/dialogflowpy-webhook/issues>`_

Table of Contents
##################

.. toctree::
   :maxdepth: 2

   getting_started
   module_reference
