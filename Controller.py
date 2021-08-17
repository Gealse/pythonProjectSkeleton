from WebController import WebController


class Controller(object):

    webController = None

    def __init__(self):
        self.webController = WebController()

    def setCredentials(self):
        pass

    def getCredential(self):
        pass

    def mainController(self):
        pass