import Arms

class ConcreteArms(Arms):
    # Creates the properties of a weapon. Used to create any new weapon object.
    # Type may seem like it is missing, but do remember this is an interface. Type is
    # Dictated by the class. This allows for new types of weapons to be created.
    def __init__(self, rank, mt, hit, crit, range, effective, uses, worth, name, type, iconID):
        Arms.__init__(self, uses, worth, name, iconID)
        self.rank = rank
        self.mt = mt
        self.hit = hit
        self.crit = crit
        self.range = range
        self.effective = effective
        self.type = type

        # Instructions to be run when a weapon is set to a unit's equipped slot.

    def onEquip(self, unit):
        pass

    def onCombatUse(self, stack):
        self.uses -= 1

    def offEquip(self, unit):
        pass

        # Returns the stat (magic or strength) to be used in the combat calculator when attacking
        # with this weapon. Allows for modularity and follows the logic of a sword knowing it's a sword.

    def getCombatStat(self):
        return 'str'

    def triangleBonus(self, arms):
        list = ['Axe', 'Lance', 'Sword']
        this = list.index(self.type)
        that = list.index(arms.type)
        if this+1 == that or (this == 2 and that == 0): return 1
        elif this-1 == that or (this == 0 and that == 2): return 0
        else: return -1
