from dataclasses import dataclass,field

class TransformController(object):
    """ """
    itemFactory:None
    
    def __init__(self):
        self.itemFactory = ItemFactory()

    def createItems(self):
        self.itemFactory.createItemsA()
        self.itemFactory.createItemsB()

    def getItemsA(self):
        return self.itemFactory.getItemsA()
        
    def getItemsB(self):
        return self.itemFactory.getItemsB()

class ItemFactory(object):
    """ """
    itemAList:list
    itemBList:list

    def __init__(self):
        self.itemAList = []
        self.itemBList = []

    def createItemsA(self):
        self.itemAList.append(ItemA(fullName ='Genis Algans Segui'))

    def createItemsB(self):
        self.itemBList.append(ItemB(dividend=10,divisor=4))

    def getItemsA(self):
        return self.itemAList
        
    def getItemsB(self):
        return self.itemBList
@dataclass()
class ItemA(object):
    """ """
    fullName:str
    name:str = field(init=False)
    surname:str = field(init=False)
    surname2:str = field(init=False,default='')
    
    def __post_init__(self):
        self.name = self.fullName.split(' ')[0]
        self.surname = self.fullName.split(' ')[1]
        if (self.fullName.split(' ')[2]):
            self.surname2 = self.fullName.split(' ')[2]

    def getFullName(self):
        return self.fullName

    def getName(self):
        return self.name

    def getSurname(self):
        return self.surname

    def getSurname2(self):
        return self.surname2

@dataclass()
class ItemB(object):
    """ """
    dividend:int
    divisor:int
    quotient:int = field(init=False)
    remainder:float = field(init=False)
    
    def __post_init__(self):
        self.quotient = int(self.dividend / self.divisor)
        self.remainder = self.dividend % self.divisor

    def getDividend(self):
        return self.dividend

    def getDividend(self):
        return self.divisor

    def getQuotient(self):
        return self.quotient

    def getRemainder(self):
        return self.remainder