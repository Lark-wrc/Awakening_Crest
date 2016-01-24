import Item

class Arms(Item):
    # Creates the properties of a weapon. Used to create any new weapon object.
    # Type may seem like it is missing, but do remember this is an interface. Type is
    # Dictated by the class. This allows for new types of weapons to be created.
    def __init__(self, rank, mt, hit, crit, range, effective, uses, worth, name, iconID):
        Item.__init__(self, uses, worth, name, iconID)
        self.rank = rank
        self.mt = mt
        self.hit = hit
        self.crit = crit
        self.range = range
        self.effective = effective


    def onEquip(self, unit):
        pass

        # If this weapon does anything special, such as allow an extra attack or grant
        # a combat skill to it's user, this method will apply it to the stack provided.

    def onCombatUse(self, stack):
        pass

        # The inverse of on_equip.

    def offEquip(self, unit):
        pass

        # Returns true or false if a unit can equip this weapon. Will check itself against the
        # provided unit's class's equippible list.

    def equippible(self, unit):
        pass

        # Returns the stat (magic or strength) to be used in the combat calculator when attacking
        # with this weapon. Allows for modularity and follows the logic of a sword knowing it's a sword.

    def getCombatStat(self):
        pass

    def triangleBonus(Arms):
        pass


