import ConcreteArms

class OnlyXArms(ConcreteArms):
    # Creates the properties of a weapon. Used to create any new weapon object.
    # Type may seem like it is missing, but do remember this is an interface. Type is
    # Dictated by the class. This allows for new types of weapons to be created.
    def __init__(self, rank, mt, hit, crit, range, effective, uses, worth, name, type, validClasses, validNames, iconID):
        ConcreteArms.__init__(self, uses, worth, name, iconID)
        self.rank = rank
        self.mt = mt
        self.hit = hit
        self.crit = crit
        self.range = range
        self.effective = effective
        self.type = type
        self.validNames = validNames
        self.validClasses = validClasses

        # Instructions to be run when a weapon is set to a unit's equipped slot.

    def onEquip(self, unit):
        if unit.getName not in self.validNames:
            pass
        elif unit.getClassName not in self.validClasses:
            pass
        else:
            #equip
            pass
