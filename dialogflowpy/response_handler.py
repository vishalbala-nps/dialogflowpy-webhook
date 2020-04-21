class response_handler():
    def __init__(self):
        self.cardbtnlist = []
        self.gsuglist = []
        self.googleijson = []
        self.gcarouselindex = 0
        self.gtableindex = 0
        self.gpermissionavail = False
        self.fulfiltextavail = False
        self.gencardavail = False
        self.eventavail = False
    #Event Triggers
    def trigger_event(self,event,params,langcode="en-US"):
        self.trigeventname = event
        self.trigeventparams = params
        self.triglangcode = langcode
        self.eventavail = True
    #Generic Responses
    def generic_response(self,speech):
        self.ftext = speech
        self.fulfiltextavail = True
    def generic_card(self,title,subtitle):
        self.cardtitle = title
        self.cardsubtitle = subtitle
        self.gencardavail = True
    def generic_card_add_button(self,btntitle,btnlink):
        self.cardbtnlist.append({"text":btntitle,"postback":btnlink})
    #Google Assistant Responses
    def google_assistant_speech(self,speech, **kwargs):
        gstts = speech
        gsdisplay = kwargs.get("displayText", "")
        self.gendcon = kwargs.get("endConversation",False)
        if gsdisplay != "":
            self.googleijson.append({"simpleResponse": {"textToSpeech":gstts,"displayText":gsdisplay}})
        else:
            self.googleijson.append({"simpleResponse": {"textToSpeech":gstts}})
    def google_assistant_card(self,title,subtitle,**kwargs):
        gcardtitle = title
        gcardftext = subtitle
        gcardbtn = kwargs.get("btnName","")
        gcardurl = kwargs.get("btnLink","")
        if gcardbtn == "":
            self.googleijson.append({"basicCard":{"title":gcardtitle,"formatted_text":gcardftext}})
        else:
            self.googleijson.append({"basicCard":{"title":gcardtitle,"formatted_text":gcardftext,"buttons":[{"title":gcardbtn,"openUrlAction":{"url":gcardurl}}]}})
    def google_assistant_new_carousel(self):
        self.googleijson.append({"carouselBrowse":{"items":[]}})
        self.gcarouselindex = self.googleijson.index({"carouselBrowse":{"items":[]}})
    def google_assistant_carousel_new_item(self,title,url,description,footer,imgurl,imgalt):
        try:
            self.googleijson[self.gcarouselindex]["carouselBrowse"]["items"].append({"title":title,"openUrlAction": {"url":url},"description":description,"footer":footer,"image":{"url":imgurl,"accessibilityText":imgalt}})
        except:
            raise AttributeError("google_assistant_new_carousel is not created")
    def google_assistant_new_suggestion(self,text):
        try:
            self.gsuglist.append({"title":text})
        except:
            self.gsuglist = []
            self.gsuglist.append({"title":text})
    def google_assistant_new_table(self):
        self.googleijson.append({"tableCard": {"rows":[],"columnProperties": []}})
        self.gtableindex = self.googleijson.index(({"tableCard": {"rows":[],"columnProperties": []}}))
    def google_assistant_table_add_header(self,headerName):
        try:
            self.googleijson[self.gtableindex]["tableCard"]["columnProperties"].append({"header":headerName})
        except:
            raise AttributeError("google_assistant_new_table is not created")
    def google_assistant_table_add_cell(self,cellList,addDivider):
        try:
            tablelist = []
            for i in cellList:
                tablelist.append({"text":i})
            self.googleijson[self.gtableindex]["tableCard"]["rows"].append({"cells":tablelist,"dividerAfter":addDivider})
        except:
            raise AttributeError("google_assistant_new_table is not created")
    def google_assistant_media_response(self,mediaURL,description,imgURL,imgDesc,displayName,speech):
        self.googleijson.append({"mediaResponse":{"mediaType": "AUDIO","mediaObjects":[{"contentUrl":mediaURL,"description":description,"icon":{"url":imgURL,"accessibilityText":imgDesc},"name":displayName}]}})
    def google_assistant_ask_permisson(self,speech,permissions):
        self.gpermissionjson = {"intent":"actions.intent.PERMISSION","data":{"@type":"type.googleapis.com/google.actions.v2.PermissionValueSpec","optContext":speech,"permissions":permissions}}
        self.gpermissionavail = True
    def create_final_response(self):
        try:
            if self.gendcon == False:
                expectres = True
            else:
                expectres = False
        except:
            expectres = True
        #Event Trigger
        if self.eventavail1:
            self.fulfiljson = {"followupEventInput":{"name":self.trigeventname,"parameters":self.trigeventparams,"languageCode":self.triglangcode}}
            return self.fulfiljson
        #Generic Reponses
        if self.fulfiltextavail:
            self.fulfiljson = {"fulfillmentText":self.ftext}
        else:
            self.fulfiljson = {}
        if self.gencardavail:
            if self.cardbtnlist != []:
                self.cardjson = {"title":self.cardtitle,"subtitle":self.cardsubtitle,"buttons":self.cardbtnlist}
            else:
                self.cardjson = {"title":self.cardtitle,"subtitle":self.cardsubtitle}
            self.fulfiljson["fulfillmentMessages"] = []
            self.fulfiljson["fulfillmentMessages"].append({"card":self.cardjson})
        #Google Assistant Responses
        if self.googleijson != []:
            self.fulfiljson["payload"] = {"google":{"expectUserResponse": expectres,"richResponse":{"items":self.googleijson}}}
        if self.gsuglist != []:
            try:
                self.fulfiljson["payload"]["google"]["richResponse"]["suggestions"] = self.gsuglist
            except:
                raise AttributeError("You are trying to insert suggestions into a Google Assistant Rich Response with no items. This will lead to an error in Actions on Google")
        if self.gpermissionavail:
            if self.googleijson != []:
                self.fulfiljson["payload"]["google"]["systemIntent"] = self.gpermissionjson
            else:
                self.fulfiljson["payload"] = {"google":{"expectUserResponse": expectres,"systemIntent":self.gpermissionjson}}
        return self.fulfiljson