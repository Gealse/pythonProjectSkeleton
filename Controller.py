from RawDataController import RawDataController
from TransformController import TransformController
from ProcessController import ProcessController
from OutputController import OutputController

class Controller(object):

    rawDataController = None
    transformController = None
    processController = None
    outputController = None

    def __init__(self):
        self.rawDataController = RawDataController()
        self.transformController = TransformController()
        self.processController = ProcessController()
        self.outputController = OutputController()

    def setCredentials(self):
        pass

    def getCredential(self):
        pass

    def mainController(self):
        pass