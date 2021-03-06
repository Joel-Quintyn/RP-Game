import items
import weapons


class NonPlayableCharacter():
    def __init__(self):
        self.name = None
        raise NotImplementedError("Do not create raw NPC objects.")

    def __str__(self):
        return self.name


class Trader(NonPlayableCharacter):
    def __init__(self):
        # super().__init__()
        self.name = "Trader"
        self.gold = 100
        self.inventory = [items.CrustyBread(), items.CrustyBread(), items.CrustyBread(),
                          items.HealingPotion(), items.HealingPotion()]
