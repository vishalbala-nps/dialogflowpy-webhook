class response_handler():
    def __init__(self):
        self.gcardbtnlist = []
        self.cardbtnlist = []
        self.gsuglist = []
        self.gmedialist = []
    def generic_response(self,speech):
        self.ftext = speech
    def generic_card(self,title,subtitle):
        self.cardtitle = title
        self.cardsubtitle = subtitle
    def generic_card_new_button(self,btntitle,btnlink):
        self.cardbtnlist.append({"text":btntitle,"postback":btnlink})
    def google_assistant_speech(self,speech, **kwargs):
        self.gstts = speech
        self.gsdisplay = kwargs.get("displayText", "")
        self.gendcon = kwargs.get("endConversation",False)
    def google_assistant_card(self,title,subtitle,speech):
        self.gcardtitle = title
        self.gcardftext = subtitle
        self.gcardspeech = speech
    def google_assistant_card_new_button(self,btntitle,btnlink):
        self.gcardbtnlist.append({"title":btntitle,"openUrlAction":{"url":btnlink}})
    def google_assistant_new_carousel(self,speech):
        self.carousellist = []
        self.carousellist.append({"simpleResponse":{"textToSpeech":speech}})
        self.carousellist.append({"carouselBrowse":{"items":[]}})
    def google_assistant_carousel_new_item(self,title,url,description,footer,imgurl,imgalt):
        try:
            self.carousellist[1]["carouselBrowse"]["items"].append({"title":title,"openUrlAction": {"url":url},"description":description,"footer":footer,"image":{"url":imgurl,"accessibilityText":imgalt}})
        except:
            raise AttributeError("googleAssistantNewCarousel is not created")
    def google_assistant_new_suggestion(self,text):
        try:
            self.gsuglist.append({"title":text})
        except:
            self.gsuglist = []
            self.gsuglist.append({"title":text})
    def google_assistant_new_table(self,speech):
        self.gtablejson = {"tableCard": {"rows":[],"columnProperties": []}}
        self.gtablespeech = speech
    def google_assistant_table_add_header(self,headerName):
        try:
            self.gtablejson["tableCard"]["columnProperties"].append({"header":headerName})
        except:
            raise AttributeError("googleAssistantNewTable is not created")
    def google_assistant_table_add_cell(self,cellList,addDivider):
        try:
            tablelist = []
            for i in cellList:
                tablelist.append({"text":i})
            self.gtablejson["tableCard"]["rows"].append({"cells":tablelist,"dividerAfter":addDivider})
        except:
            raise AttributeError("googleAssistantNewTable is not created")
    def google_assistant_media_response(self,mediaURL,description,imgURL,imgDesc,displayName,speech):
        self.mediajson = ({"mediaResponse":{"mediaType": "AUDIO","mediaObjects":[{"contentUrl":mediaURL,"description":description,"icon":{"url":imgURL,"accessibilityText":imgDesc},"name":displayName}]}})
        self.mediatts = ({"simpleResponse":{"textToSpeech":speech}})
    def google_assistant_ask_permisson(self,speech,permissions):
        self.gpermissionjson = {"intent":"actions.intent.PERMISSION","data":{"@type":"type.googleapis.com/google.actions.v2.PermissionValueSpec","optContext":speech,"permissions":permissions}}
    def form_response(self):
        import warnings
        ijson = []
        try:
            if self.gendcon == False:
                expectres = True
            else:
                expectres = False
        except:
            expectres = False
        #Generic Reponses
        try:
            self.fulfiljson = {"fulfillmentText":self.ftext}
        except:
            self.fulfiljson = {}
            warnings.warn("genericResponse is not set. Your agent might not work on all platforms")
        try:
            if self.cardbtnlist != []:
                self.cardjson = {"title":self.cardtitle,"subtitle":self.cardsubtitle,"buttons":self.cardbtnlist}
            else:
                self.cardjson = {"title":self.cardtitle,"subtitle":self.cardsubtitle}
            self.fulfiljson["fulfillmentMessages"] = []
            self.fulfiljson["fulfillmentMessages"].append({"card":self.cardjson})
        except:
            pass
        #Google Assistant Responses
        try:
            if self.gsdisplay != "":
                ijson.append({"simpleResponse": {"textToSpeech":self.gstts,"displayText":self.gsdisplay}})
            else:
                ijson.append({"simpleResponse": {"textToSpeech":self.gstts}})
        except:
            pass
        try:
            ijson.append({"simpleResponse":{"textToSpeech":self.gcardspeech}})
            if self.gcardbtnlist == []:
                ijson.append({"basicCard":{"title":self.gcardtitle,"formatted_text":self.gcardftext}})
            else:
                ijson.append({"basicCard":{"title":self.gcardtitle,"formatted_text":self.gcardftext,"buttons":self.gcardbtnlist}})
        except:
            pass
        try:
            for i in self.carousellist:
                ijson.append(i)
        except:
            pass
        try:
            ijson.append({"simpleResponse":{"textToSpeech":self.gtablespeech}})
            ijson.append(self.gtablejson)
        except:
            pass
        try:
            ijson.append(self.mediatts)
            ijson.append(self.mediajson)
        except:
            pass
        if ijson != []:
            try:
                self.fulfiljson["payload"].update({"google":{"expectUserResponse": expectres,"richResponse":{"items":ijson}}})
            except:
                self.fulfiljson["payload"] = {"google":{"expectUserResponse": expectres,"richResponse":{"items":ijson}}}
        if self.gsuglist != []:
            try:
                self.fulfiljson["payload"].update({"google":{"expectUserResponse": expectres,"richResponse":{"items":ijson,"suggestions":self.gsuglist}}})
            except:
                self.fulfiljson["payload"] = {"google":{"expectUserResponse": expectres,"richResponse":{"items":ijson,"suggestions":self.gsuglist}}}
        try:
            if ijson != []:
                self.fulfiljson["payload"]["google"]["systemIntent"] = self.gpermissionjson
            else:
                try:
                    self.fulfiljson["payload"].update({"google":{"expectUserResponse": expectres,"systemIntent":self.gpermissionjson}}) 
                except:
                    self.fulfiljson["payload"] = {"google":{"expectUserResponse": expectres,"systemIntent":self.gpermissionjson}}
        except:
            pass
        return self.fulfiljson