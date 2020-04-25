class response_handler():
    """
    The Class handles the creation of Dialogflow Responses

    .. note:: There are 2 types of Rich Responses which can be created using this class. They are: Generic Rich Responses and Google Assistant Rich Responses. Generic Responses work on all platforms except Google Assistant. Functions that create generic responses start with 'generic'. For Google Assistant, you should use Google Assistant Rich Responses. These functions start with 'google_assistant'
    """
    def __init__(self):
        """
        Constructor
        """
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
        self.gcardadded = False
    #Context
    def add_context(self,sessionID,contextName,lifespan=0,params={}):
        """
        Adds/Changes a Dialogflow Context

        :param sessionID: The Session ID
        :type sessionID: str
        :param contextName: The name of the Context to add/edit
        :type contextName: str
        :param lifespan: The  number of conversational turns for which the context remains active, defaults to 0
        :type lifespan: int, optional
        :param params: The Dictionary of Data to store in the context, defaults to {}
        :type params: dict, optional
        """
        self.contextlist.append({"name":sessionID+"/contexts/"+contextName,"lifespanCount":lifespan,"parameters":params})
        self.contextavail = True
    #Event Triggers
    def trigger_event(self,event,params,langcode="en-US"):
        """
        Triggers a Dialogflow Event

        :param event: The Name of the Event to Trigger
        :type event: str
        :param params: The Dictionary of Parameters
        :type params: dict
        :param langcode: The Language Code of the Agent, defaults to "en-US"
        :type langcode: str, optional

        .. note:: When the response contains event, other things are ignored (except Contexts)
        """
        self.trigeventname = event
        self.trigeventparams = params
        self.triglangcode = langcode
        self.eventavail = True
    #Generic Responses
    def generic_response(self,speech):
        """
        A Generic Text to be displayed or told to the user.

        :param speech: The Text to be displayed or said to the user
        :type speech: str

        .. note:: ``generic_response`` works on all platforms including Google Assistant. However, it is recommended to use ``google_assistant_response`` for Google Assistant and ``generic_rich_text_response`` for text responses on other platforms.
        """
        self.ftext = speech
        self.fulfiltextavail = True
    #Generic Rich Responses
    def generic_rich_text_response(self,text):
        """
        A Generic Rich Text Response to display to the user. Unlike ``generic_response``, you can have multiple ``generic_rich_text_response``

        :param text: The Text to be displayed to the user
        :type text: str
        """
        self.genericmessages.append({"text":{"text":[text]}})
    def generic_card(self,title,**kwargs):
        """
        A Generic Card to be displayed to the user

        :param title: The Title of the Card
        :type title: str
        :param subtitle: The Subitle of the Card
        :type subtitle: str, optional
        :param imageURL: The Link of the Image to be displayed on the card
        :type imageURL: str, optional
        """
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
        """
        Adds a button to a Generic Card. When clicked, directs to a website

        :param btntitle: The button's title
        :type btntitle: str
        :param btnlink: The link to redirect to on click
        :type btnlink: str
        :raises AttributeError: This Error is Raised if a new button is added before calling ``generic_card``
        """
        if self.gencardindex == -1:
            raise AttributeError("generic_card is not created")
        else:
            try:
                self.genericmessages[self.gencardindex]["card"]["buttons"].append({"text":btntitle,"postback":btnlink})
            except:
                self.genericmessages[self.gencardindex]["card"]["buttons"] = []
                self.genericmessages[self.gencardindex]["card"]["buttons"].append({"text":btntitle,"postback":btnlink})
    def generic_add_suggestions(self,suggestionList,**kwargs):
        """
        Adds Suggestion Chips/Quick Replies to be displayed. 

        :param suggestionList: The List of Suggestions/Quick Replies
        :type suggestionList: list
        :param title: The title of the Suggestions
        :type suggestionList: str, optional
        """
        title = kwargs.get("title","")
        self.genericmessages.append({"quick_replies":{"title":title,"quickReplies":suggestionList}})
    def generic_image(self,imageURL,imgalt):
        """
        Sends an Image to the User

        :param imageURL: The URL of the Image
        :type imageURL: str
        :param imgalt: The Alt Text for the Image
        :type imgalt: str
        """
        self.genericmessages.append({"image":{"image_uri":imageURL,"accessibility_text":imgalt}})
    #Google Assistant Rich Responses
    def google_assistant_response(self,speech, **kwargs):
        """
        A Google Assistant speech to be said (and displayed) to the user

        :param speech: The Text to be said to the user
        :type speech: str
        :param displayText: The text to be displayed in the chat bubble while telling the speech
        :type displayText: str, optional
        :param endConversation: Specifies wheather this response should end the conversation or not
        :type endConversation: bool

        .. note:: This MUST Before any Google Assistant Rich Response. Failing to do so will result in an error in Google Assistant
        """
        gstts = speech
        gsdisplay = kwargs.get("displayText", "")
        self.gendcon = kwargs.get("endConversation",False)
        if gsdisplay != "":
            self.googleijson.append({"simpleResponse": {"textToSpeech":gstts,"displayText":gsdisplay}})
        else:
            self.googleijson.append({"simpleResponse": {"textToSpeech":gstts}})
    def google_assistant_card(self,title,**kwargs):
        """
        A Google Assistant Card to be displayed to the user

        :param title: The Title of the Card
        :type title: str

        :param subtitle: The subtitle of the Card
        :type subtitle: str, optional

        :param formatted_text: The text to be displayed along with the card
        :type formatted_text: str, optional

        :param btnName: The Name of the button to be displayed on the card
        :type btnName: str, optional

        :param btnLink: The link to redirect on button click
        :type btnLink: str, optional

        :param imageURL: The URL of the image to be displayed on the card
        :type imageURL: str, optional

        :param imageAlt: The Alt Text of the image to be displayed on the card
        :type imageAlt: str, optional
    
        :param imageDisplayOption: The Display options for the image (`Click here For a list of image display options <https://developers.google.com/assistant/conversational/webhook/reference/rest/Shared.Types/ImageDisplayOptions>`_)
        :type imageDisplayOption: str, optional

        :raises AttributeError: This error is raised if more than one card is added
        """
        if self.gcardadded == True:
            raise AttributeError("You can have only one Google Assistant Card. More than one cards will lead to an error in Google Assistant")
        self.gcardadded = True
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
        """
        Creates a New Google Assistant Carousel

        :raises AttributeError: This error is raised if more than one Carousel is added
        """
        if self.gcarouselindex != -1:
            raise AttributeError("You can have only one Google Assistant Carousel. More than one Carousels will lead to an error in Google Assistant")
        self.googleijson.append({"carouselBrowse":{"items":[]}})
        self.gcarouselindex = len(self.googleijson)-1
    def google_assistant_carousel_add_item(self,title,url,imageURL,imgalt,description="",footer=""):
        """
        Adds a new item to a Google Assistant Carousel

        :param title: The title of the carousel item
        :type title: str
        :param url: The URL to redirect to when the Carousel item is clicked
        :type url: str
        :param imageURL: The URL of the image to be displayed on the caarousel item
        :type imageURL: str
        :param imgalt: The Alt text of the image to be displayed on the caarousel item
        :type imgalt: str
        :param description: The description to be displayed on the carousel item, defaults to ""
        :type description: str, optional
        :param footer: The footer to be displayed on the carousel item, defaults to ""
        :type footer: str, optional
        :raises AttributeError: This Error is raised if a new item is added before calling ``google_assistant_new_carousel``
        """
        try:
            self.googleijson[self.gcarouselindex]["carouselBrowse"]["items"].append({"title":title,"openUrlAction": {"url":url},"description":description,"footer":footer,"image":{"url":imageURL,"accessibilityText":imgalt}})
        except:
            raise AttributeError("google_assistant_new_carousel is not created")
    def google_assistant_add_suggestions(self,suggestionList):
        """
        Adds Google Assistant Suggestion Chips to be displayed

        :param suggestionList: The list containing the suggestions to be displayed
        :type suggestionList: list
        """
        for i in suggestionList:
            self.gsuglist.append({"title":i})
    def google_assistant_new_table(self,**kwargs):
        """
        Creates a new Google Assistant Table Card

        :param title: The title of the Table Card
        :type title: str, optional

        :param subtitle: The subtitle of the Table Card
        :type subtitle: str, optional

        :param imageURL: The URL of the image to be displayed on the table card
        :type imageURL: str, optional

        :param imageAlt: The Alt text of the image to be displayed on the table card
        :type imageAlt: str, optional

        :raises AttributeError: This error is raised if more than one Table is added
        """
        if self.gtableindex != -1:
            raise AttributeError("You can have only one Google Assistant Table. More than one Tables will lead to an error in Google Assistant")
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
        """
        Adds a Header row to a Google Assistant Table Card

        :param headerList: The list containing the header rows to be added
        :type headerList: list
        :raises AttributeError: This Error is raised if a header row is added before calling ``google_assistant_new_table``
        """
        try:
            for i in headerList:
                self.googleijson[self.gtableindex]["tableCard"]["columnProperties"].append({"header":i})
        except:
            raise AttributeError("google_assistant_new_table is not created")
    def google_assistant_table_add_row(self,cellList,addDivider):
        """
        Adds a new row to a Google Assistant Table Card

        :param cellList: The list containing the rows to be added
        :type cellList: list
        :param addDivider: Specifies if a divider should be added after the row
        :type addDivider: bool
        :raises AttributeError: This Error is raised if a row is added before calling ``google_assistant_new_table``
        """
        try:
            tablelist = []
            for i in cellList:
                tablelist.append({"text":i})
            self.googleijson[self.gtableindex]["tableCard"]["rows"].append({"cells":tablelist,"dividerAfter":addDivider})
        except:
            raise AttributeError("google_assistant_new_table is not created")
    def google_assistant_media_response(self,mediaURL,description,displayName,**kwargs):
        """
        Creates a Google Assistant Media Response to play music

        :param mediaURL: The URL where the music is located
        :type mediaURL: str
        :param description: The description of the music
        :type description: str
        :param displayName: The name of the music to display
        :type displayName: str
        :param imageURL: The URL of the image to be displayed along with the media response
        :type imageURL: str,optional
        :param imgAlt: The Alt Text of the image to be displayed along with the media response
        :type imgAlt: str,optional
        """
        imgURL = kwargs.get("imageURL","")
        imgAlt = kwargs.get("imgAlt","")
        self.googleijson.append({"mediaResponse":{"mediaType": "AUDIO","mediaObjects":[{"contentUrl":mediaURL,"description":description,"icon":{"url":imgURL,"accessibilityText":imgAlt},"name":displayName}]}})
    def google_assistant_ask_permisson(self,speech,permissionList):
        """
        Asks for permission from user in Google Assistant to get details like User's real name and address

        :param speech: The reason for the Permisssion Request
        :type speech: str
        :param permissionList: The list of Permissions to get from the user 
        :type permissionList: list
        """
        self.gpermissionjson = {"intent":"actions.intent.PERMISSION","data":{"@type":"type.googleapis.com/google.actions.v2.PermissionValueSpec","optContext":speech,"permissions":permissionList}}
        self.gpermissionavail = True
    def create_final_response(self):
        """
        Creates the Final Response JSON to be sent back to Dialogflow

        :raises AttributeError: This error is raised if you try to insert Google Assistant Suggestions to a Google Assistant Rich Response with no items
        :return: The Response JSON
        :rtype: Dictionary
        """
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