class response_handler():
    def __init__(self):
        self.gcardbtnlist = []
        self.cardbtnlist = []
        self.gsuglist = []
        self.gmedialist = []
    def genericResponse(self,text):
        self.ftext = text
    def genericCard(self,title,subtitle):
        self.cardtitle = title
        self.cardsubtitle = subtitle
    def genericCardNewButton(self,btntitle,btnlink):
        self.cardbtnlist.append({"text":btntitle,"postback":btnlink})
    def googleAssistantCard(self,title,subtitle,text):
        self.gcardtitle = title
        self.gcardftext = subtitle
        self.gcardspeech = text
    def googleAssistantCardNewButton(self,btntitle,btnlink):
        self.gcardbtnlist.append({"title":btntitle,"openUrlAction":{"url":btnlink}})
    def googleAssistantNewCarousel(self,text):
        self.carousellist = []
        self.carousellist.append({"simpleResponse":{"textToSpeech":text}})
        self.carousellist.append({"carouselBrowse":{"items":[]}})
    def googleAssistantCarouselNewItem(self,title,url,description,footer,imgurl,imgalt):
        try:
            self.carousellist[1]["carouselBrowse"]["items"].append({"title":title,"openUrlAction": {"url":url},"description":description,"footer":footer,"image":{"url":imgurl,"accessibilityText":imgalt}})
        except:
            raise AttributeError("googleAssistantNewCarousel is not created")
    def googleAssistantNewSuggestion(self,text):
        try:
            self.gsuglist.append({"title":text})
        except:
            self.gsuglist = []
            self.gsuglist.append({"title":text})
    def googleAssistantMediaResponse(self,mediaURL,description,imgURL,imgDesc,displayName,speech):
        self.mediajson = ({"mediaResponse":{"mediaType": "AUDIO","mediaObjects":[{"contentUrl":mediaURL,"description":description,"icon":{"url":imgURL,"accessibilityText":imgDesc},"name":displayName}]}})
        self.mediatts = ({"simpleResponse":{"textToSpeech":speech}})
    def formResponse(self):
        import warnings
        ijson = []
        try:
            self.fulfiljson = {"fulfillmentText":self.ftext}
        except:
            self.fulfiljson = {}
            warnings.warn("genericResponse is not set. Your agent might not work on all platforms")
        try:
            ijson.append({"simpleResponse":{"textToSpeech":self.gcardspeech}})
            if self.gcardbtnlist == []:
                ijson.append({"basicCard":{"title":self.gcardtitle,"formatted_text":self.gcardftext}})
            else:
                ijson.append({"basicCard":{"title":self.gcardtitle,"formatted_text":self.gcardftext,"buttons":self.gcardbtnlist}})
        except:
            pass
        try:
            if self.cardbtnlist != []:
                self.cardjson = {"title":self.cardtitle,"subtitle":self.cardsubtitle,"buttons":self.cardbtnlist}
            else:
                self.cardjson = {"title":self.cardtitle,"subtitle":self.cardsubtitle}
            self.fulfiljson["fulfillmentMessages"] = []
            self.fulfiljson["fulfillmentMessages"].append({"card":self.cardjson})
        except:
            pass
        try:
            self.fulfiljson["outputContexts"] = self.contexts
        except:
            pass
        try:
            for i in self.carousellist:
                ijson.append(i)
        except:
            pass
        try:
            ijson.append(self.mediatts)
            ijson.append(self.mediajson)
        except:
            pass
        if ijson != []:
            try:
                self.fulfiljson["payload"].update({"google":{"expectUserResponse": True,"richResponse":{"items":ijson}}})
            except:
                self.fulfiljson["payload"] = {"google":{"expectUserResponse": True,"richResponse":{"items":ijson}}}
        if self.gsuglist != []:
            try:
                self.fulfiljson["payload"].update({"google":{"expectUserResponse": True,"richResponse":{"items":ijson,"suggestions":self.gsuglist}}})
            except:
                self.fulfiljson["payload"] = {"google":{"expectUserResponse": True,"richResponse":{"items":ijson,"suggestions":self.gsuglist}}}
        return self.fulfiljson