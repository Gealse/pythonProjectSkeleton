from dataclasses import dataclass

class TransformController(object):

    itemFactory : None
    
    def __init__(self):
        itemFactory = ItemFactory()

class ItemFactory(object):

    itemsList : list

    def __init__(self):
        self.itemsList.append(Item(name = 'hello'))
        input(itemsList)
        input(itemsList[0])

@dataclass
class Item(object):

    name : str
    
    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name