class response_handler():
    def __init__(self):
        self.cardbtnlist = []
        self.gsuglist = []
        self.googleijson = []
        self.genericmessages = []
        self.contextlist = []
        self.gencardindex = 0
        self.gcarouselindex = 0
        self.gtableindex = 0
        self.gpermissionavail = False
        self.fulfiltextavail = False
        self.eventavail = False
        self.contextavail = False
    #Event Triggers
    def trigger_event(self,event,params,langcode="en-US"):
        self.trigeventname = event
        self.trigeventparams = params
        self.triglangcode = langcode
        self.eventavail = True
    def add_context(self,sessionID,contextName,lifespan,params):
        self.contextlist.append({"name":sessionID+"/contexts/"+contextName,"lifespanCount":lifespan,"parameters":params})
        self.contextavail = True
    #Generic Responses
    def generic_response(self,speech):
        self.ftext = speech
        self.fulfiltextavail = True
    def generic_card(self,title,subtitle,**kwargs):
        imgurl = kwargs.get("imageURL","")
        fjson = {}
        if imgurl == "":
            fjson = {"card":{"title":title,"subtitle":subtitle}}
        else:
            fjson = {"card":{"title":title,"subtitle":subtitle,"imageUri":imgurl}}
        self.genericmessages.append(fjson)
        self.gencardindex = self.genericmessages.index(fjson)
    def generic_card_add_button(self,btntitle,btnlink):
        try:
            self.genericmessages[self.gencardindex]["card"]["buttons"].append({"text":btntitle,"postback":btnlink})
        except:
            self.genericmessages[self.gencardindex]["card"]["buttons"] = []
            self.genericmessages[self.gencardindex]["card"]["buttons"].append({"text":btntitle,"postback":btnlink})
    def generic_quick_reply(self,title,replies):
        self.genericmessages.append({"quick_replies":{"title":title,"replies":replies}})
    def generic_image(self,imgURL,imgalt):
        self.genericmessages.append({"image":{"image_uri":imgURL,"accessibility_text":imgalt}})
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
        imgurl = kwargs.get("imageURL","")
        imgalt = kwargs.get("imageAlt","")
        toappend = {}
        if gcardbtn == "":
            toappend = {"basicCard":{"title":gcardtitle,"formatted_text":gcardftext}}
        else:
            toappend = {"basicCard":{"title":gcardtitle,"formatted_text":gcardftext,"buttons":[{"title":gcardbtn,"openUrlAction":{"url":gcardurl}}]}}
        if imgurl != "":
            toappend["basicCard"]["image"] = {"url":imgurl,"accessibilityText":imgalt}
        self.googleijson.append(toappend)
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
    def google_assistant_new_table(self,**kwargs):
        imgurl = kwargs.get("imageURL","")
        imgalt = kwargs.get("imageAlt","")
        tabtitle = kwargs.get("title","")
        tabsub = kwargs.get("subtitle","")
        fjson = {}
        fjson = {"tableCard": {"rows":[],"columnProperties": []}}
        if imgurl != "":
            fjson["tableCard"]["image"] = {"url":imgurl,"accessibilityText":imgalt}
        if tabtitle != "":
            fjson["tableCard"]["title"] = tabtitle
        if tabsub != "":
            fjson["tableCard"]["subtitle"] = tabsub
        self.googleijson.append(fjson)
        self.gtableindex = self.googleijson.index(fjson)
    def google_assistant_table_add_header(self,headerName,**kwargs):
        alignment = kwargs.get("horizontalAlignment","")
        fjson = {}
        try:
            if alignment != "":
                fjson = {"header":headerName,"horizontalAlignment":alignment}
            else:
                fjson = {"header":headerName}
            self.googleijson[self.gtableindex]["tableCard"]["columnProperties"].append(fjson)

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
        if self.eventavail:
            self.fulfiljson = {"followupEventInput":{"name":self.trigeventname,"parameters":self.trigeventparams,"languageCode":self.triglangcode}}
            return self.fulfiljson
        #Generic Reponses
        if self.fulfiltextavail:
            self.fulfiljson = {"fulfillmentText":self.ftext}
        else:
            self.fulfiljson = {}
        if self.genericmessages != []:
            self.fulfiljson["fulfillmentMessages"] = self.genericmessages
        #Contexts
        if self.contextavail == True:
            self.fulfiljson["outputContexts"] = self.contextlist
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