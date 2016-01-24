import json
import Item
import ConcreteArms
import LegendaryArms
import OnlyXArms


class LoadingFactory(object):

    def __init__(self, source):
        self.source = source

    def createConcreteArms(self, name):
        file = json.load(open(self.source, 'r'))
        ret = ConcreteArms(*[name])
        file.close()
        return ret

    def createLegendaryArms(self, name):
        file = json.load(open(self.source, 'r'))
        ret = LegendaryArms(*[name])
        file.close()
        return ret

    def createOnlyXArms(self, name):
        file = json.load(open(self.source, 'r'))
        ret = OnlyXArms(*[name])
        file.close()
        return ret

    def createItem(self, name):
        file = json.load(open(self.source, 'r'))
        ret = Item(*[name])
        file.close()
        return ret