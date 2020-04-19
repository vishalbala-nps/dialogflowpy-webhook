class intent_handler():
    def __init__(self,dialogresjson):
        self.resjson = dialogresjson
    def get_intent(self):
        return self.resjson["queryResult"]["intent"]["displayName"]
    def get_params(self):
        return self.resjson["queryResult"]["parameters"]
    def get_capabilities(self):
        try:
            retjson = []
            for i in self.resjson["originalDetectIntentRequest"]["payload"]["surface"]["capabilities"]:
                retjson.append(i["name"])
            print(retjson)
            return retjson
        except:
            return []
    def get_source(self):
        try:
            return self.resjson["originalDetectIntentRequest"]["source"]
        except:
            return ""