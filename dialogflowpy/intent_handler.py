class intent_handler():
    def __init__(self,dialogresjson):
        self.resjson = dialogresjson
    def get_intent(self):
        try:
            return self.resjson["queryResult"]["intent"]
        except:
            raise TypeError("Malformed Request JSON: Failed to find Intent JSON")
    def get_intent_name(self):
        try:
            return self.resjson["queryResult"]["intent"]["name"]
        except:
            raise TypeError("Malformed Request JSON: Failed to find Intent Name")
    def get_intent_displayName(self):
        try:
            return self.resjson["queryResult"]["intent"]["displayName"]
        except:
            raise TypeError("Malformed Request JSON: Failed to find Intent Display Name")
    def get_parameters(self):
        try:
            return self.resjson["queryResult"]["parameters"]
        except:
            return {}
    def get_parameter(self,param):
        try:
            return self.resjson["queryResult"]["parameters"][param]
        except:
            raise KeyError("Parameter "+param+" not found")
    def get_action(self):
        try:
            return self.resjson["queryResult"]["action"]
        except:
            return ""
    def get_capabilities(self):
        try:
            retjson = []
            for i in self.resjson["originalDetectIntentRequest"]["payload"]["surface"]["capabilities"]:
                retjson.append(i["name"])
            return retjson
        except:
            return []
    def get_source_payload(self):
        try:
            return self.resjson["originalDetectIntentRequest"]["payload"]
        except:
            return {}
    def get_source(self):
        try:
            return self.resjson["originalDetectIntentRequest"]["source"]
        except:
            return ""
    