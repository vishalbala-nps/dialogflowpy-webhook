class request_handler():
    """
    This Class Handles the Parsing of Dialogflow Requests and get details like Intent, Parameters, Session ID etc

    :param dialogflowRequestJson: The Dialogflow Request JSON
    """
    def __init__(self,dialogflowRequestJson):
        self.resjson = dialogflowRequestJson
    def get_intent(self):
        """
        Returns the Intent JSON which triggered the Webhook

        :raises TypeError: This Error is Raised if the Intent JSON can't be retived if the Request JSON is Malformed
        :return: Intent Object
        :rtype: JSON
        """
        try:
            return self.resjson["queryResult"]["intent"]
        except:
            raise TypeError("Malformed Request JSON: Failed to find Intent JSON")
    def get_intent_name(self):
        """
        Returns the Intent Name which triggered the Webhook

        :raises TypeError: This Error is Raised if the Intent Name can't be retived if the Request JSON is Malformed
        :return: Intent Name
        :rtype: str
        """
        try:
            return self.resjson["queryResult"]["intent"]["name"]
        except:
            raise TypeError("Malformed Request JSON: Failed to find Intent Name")
    def get_intent_displayName(self):
        """
        Returns the Intent Display Name (this is the Intent Name which you would have specified in Dialogflow) which triggered the Webhook

        :raises TypeError: This Error is Raised if the Intent Display Name can't be retived if the Request JSON is Malformed
        :return: Intent Display Name
        :rtype: str
        """
        try:
            return self.resjson["queryResult"]["intent"]["displayName"]
        except:
            raise TypeError("Malformed Request JSON: Failed to find Intent Display Name")
    def get_parameters(self):
        """
        Returns a JSON of filled Parameter Values

        :return: Parameter Object
        :rtype: JSON
        """
        try:
            return self.resjson["queryResult"]["parameters"]
        except:
            return {}
    def get_parameter(self,param):
        """
        Returns a Parameter Value by Parameter Name

        :param param: The Parameter name to retrive the Value
        :raises KeyError: This Error is Rasied if the Parameter is not found
        :return: Parameter Value
        :rtype: str
        """
        try:
            return self.resjson["queryResult"]["parameters"][param]
        except:
            raise KeyError("Parameter "+param+" not found")
    def get_action(self):
        """
        Returns the Action Name Specified for the Intent
        """
        try:
            return self.resjson["queryResult"]["action"]
        except:
            return ""
    def get_session_id(self):
        """
        Returns the Session ID of the Dialogflow Session

        :raises TypeError: This Error is Raised if the Session ID can't be retived if the Request JSON is Malformed
        :return: Session ID
        :rtype: str
        """
        try:
            return self.resjson["session"]
        except:
            raise TypeError("Malformed Request JSON: Failed to find Session ID")
    def get_context_by_name(self,contextName):
        """
        Returns a Context JSON by Context Name

        :param contextName: The Context Name to retrive the Context JSON
        :type contextName: str
        :raises LookupError: This Error is Raised if The Context is not found
        :return: Context Object
        :rtype: JSON
        """
        fres = {}
        for i in self.resjson["queryResult"]["outputContexts"]:
            if i["name"].split("/")[len(i["name"].split("/"))-1] == contextName:
                fres = i
                break
        if fres == {}:
            raise LookupError("Context with name "+contextName+" not found!")
        else:
            return fres
    def get_capabilities(self):
        """
        Returns a list Google Assistant Capabilities for a particular surface (eg. Smart Display, Mobile Phone, Chromebook etc.) from where the bot is accessed.

        .. note:: This Feature is specific only for Google Assistant. This will return an empty list if the bot is accessed from platforms which are not Google Assistant
        
        :return: Capabilities List
        :rtype: list
        """
        try:
            retjson = []
            for i in self.resjson["originalDetectIntentRequest"]["payload"]["surface"]["capabilities"]:
                retjson.append(i["name"])
            return retjson
        except:
            return []
    def get_payload(self):
        """
        Returns the Platform Specific Payload from where the request originated

        :return: Payload Object
        :rtype: JSON
        """
        try:
            return self.resjson["originalDetectIntentRequest"]["payload"]
        except:
            return {}
    def get_source(self):
        """
        Returns the source where the request originated

        :return: Source where the request originated
        :rtype: str
        """
        try:
            return self.resjson["originalDetectIntentRequest"]["source"]
        except:
            return ""