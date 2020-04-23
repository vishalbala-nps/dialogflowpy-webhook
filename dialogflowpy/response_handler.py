class response_handler():
    def __init__(self):
        self.cardbtnlist = []
        self.gsuglist = []
        self.googleijson = []
        self.genericmessages = []
        self.contextlist = []
        self.gencardindex = -1
        self.gcarouselindex = -1
        self.gtableindex = -1
        self.gpermissionavail = False
        self.fulfiltextavail = False
        self.eventavail = False
        self.contextavail = False
    #Context
    def add_context(self,sessionID,contextName,lifespan=0,params={}):
        self.contextlist.append({"name":sessionID+"/contexts/"+contextName,"lifespanCount":lifespan,"parameters":params})
        self.contextavail = True
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
    #Generic Rich Responses
    def generic_card(self,title,**kwargs):
        imgurl = kwargs.get("imageURL","")
        subtitle = kwargs.get("subtitle","")
        fjson = {}
        if imgurl == "":
            fjson = {"card":{"title":title,"subtitle":subtitle}}
        else:
            fjson = {"card":{"title":title,"subtitle":subtitle,"imageUri":imgurl}}
        self.genericmessages.append(fjson)
        self.gencardindex = len(self.genericmessages)-1
    def generic_card_add_button(self,btntitle,btnlink):
        try:
            self.genericmessages[self.gencardindex]["card"]["buttons"].append({"text":btntitle,"postback":btnlink})
        except:
            self.genericmessages[self.gencardindex]["card"]["buttons"] = []
            self.genericmessages[self.gencardindex]["card"]["buttons"].append({"text":btntitle,"postback":btnlink})
    def generic_add_suggestions(self,suggestionList,**kwargs):
        title = kwargs.get("title","")
        self.genericmessages.append({"quick_replies":{"title":title,"quickReplies":suggestionList}})
    def generic_image(self,imageURL,imgalt):
        self.genericmessages.append({"image":{"image_uri":imageURL,"accessibility_text":imgalt}})
    #Google Assistant Rich Responses
    def google_assistant_response(self,speech, **kwargs):
        gstts = speech
        gsdisplay = kwargs.get("displayText", "")
        self.gendcon = kwargs.get("endConversation",False)
        if gsdisplay != "":
            self.googleijson.append({"simpleResponse": {"textToSpeech":gstts,"displayText":gsdisplay}})
        else:
            self.googleijson.append({"simpleResponse": {"textToSpeech":gstts}})
    def google_assistant_card(self,title,**kwargs):
        gcardtitle = title
        gcardsub = kwargs.get("subtitle","")
        gcardftext = kwargs.get("formatted_text","")
        gcardbtn = kwargs.get("btnName","")
        gcardurl = kwargs.get("btnLink","")
        imgurl = kwargs.get("imageURL","")
        imgalt = kwargs.get("imageAlt","")
        imgdisopt = kwargs.get("imageDisplayOption","")
        toappend = {}
        if gcardbtn == "":
            toappend = {"basicCard":{"title":gcardtitle,"subtitle":gcardsub,"formatted_text":gcardftext}}
        else:
            toappend = {"basicCard":{"title":gcardtitle,"subtitle":gcardsub,"formatted_text":gcardftext,"buttons":[{"title":gcardbtn,"openUrlAction":{"url":gcardurl}}]}}
        if imgurl != "":
            toappend["basicCard"]["image"] = {"url":imgurl,"accessibilityText":imgalt}
        if imgdisopt != "":
            toappend["basicCard"]["imageDisplayOptions"] = imgdisopt
        self.googleijson.append(toappend)
    def google_assistant_new_carousel(self):
        self.googleijson.append({"carouselBrowse":{"items":[]}})
        self.gcarouselindex = len(self.googleijson)-1
    def google_assistant_carousel_add_item(self,title,url,imageURL,imgalt,description="",footer=""):
        try:
            self.googleijson[self.gcarouselindex]["carouselBrowse"]["items"].append({"title":title,"openUrlAction": {"url":url},"description":description,"footer":footer,"image":{"url":imageURL,"accessibilityText":imgalt}})
        except:
            raise AttributeError("google_assistant_new_carousel is not created")
    def google_assistant_add_suggestions(self,suggestionList):
        for i in suggestionList:
            self.gsuglist.append({"title":i})
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
    def google_assistant_table_add_header_row(self,headerList):
        try:
            for i in headerList:
                self.googleijson[self.gtableindex]["tableCard"]["columnProperties"].append({"header":i})
        except:
            raise AttributeError("google_assistant_new_table is not created")
    def google_assistant_table_add_row(self,cellList,addDivider):
        try:
            tablelist = []
            for i in cellList:
                tablelist.append({"text":i})
            self.googleijson[self.gtableindex]["tableCard"]["rows"].append({"cells":tablelist,"dividerAfter":addDivider})
        except:
            raise AttributeError("google_assistant_new_table is not created")
    def google_assistant_media_response(self,mediaURL,description,displayName,**kwargs):
        imgURL = kwargs.get("imageURL","")
        imgDesc = kwargs.get("imgDesc","")
        self.googleijson.append({"mediaResponse":{"mediaType": "AUDIO","mediaObjects":[{"contentUrl":mediaURL,"description":description,"icon":{"url":imgURL,"accessibilityText":imgDesc},"name":displayName}]}})
    def google_assistant_ask_permisson(self,speech,permissionList):
        self.gpermissionjson = {"intent":"actions.intent.PERMISSION","data":{"@type":"type.googleapis.com/google.actions.v2.PermissionValueSpec","optContext":speech,"permissions":permissionList}}
        self.gpermissionavail = True
    def create_final_response(self):
        self.fulfiljson = {}
        try:
            if self.gendcon == False:
                expectres = True
            else:
                expectres = False
        except:
            expectres = True
        #Contexts
        if self.contextavail == True:
            self.fulfiljson["outputContexts"] = self.contextlist
        #Event Trigger
        if self.eventavail:
            self.fulfiljson = {"followupEventInput":{"name":self.trigeventname,"parameters":self.trigeventparams,"languageCode":self.triglangcode}}
            return self.fulfiljson
        #Generic Reponses
        if self.fulfiltextavail:
            self.fulfiljson = {"fulfillmentText":self.ftext}
        if self.genericmessages != []:
            self.fulfiljson["fulfillmentMessages"] = self.genericmessages
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