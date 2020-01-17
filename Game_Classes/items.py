# class Item:
#     """The Base Class For All Items"""
#
#     def __init__(self, name, description, value):
#         self.name = name
#         self.description = description
#         self.value = value
#
#     def __str__(self):
#         return "{}{}".format(self.value, self.name)
#
#     def item_info(self):
#         return "{}\n{}\n{}\nValue: ${}\n".format(self.name, '=' * len(self.name), self.description, self.value)


class Consumable:
    def __init__(self):
        self.name = None
        self.healing_value = None
        self.value = None
        raise NotImplementedError("Do Not Create Raw Consumable Objects.")

    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)


class CrustyBread(Consumable):
    def __init__(self):
        # super().__init__()
        self.name = "Crusty Bread"
        self.healing_value = 10
        self.value = 12


class HealingPotion(Consumable):
    def __init__(self):
        # super().__init__()
        self.name = "Healing Potion"
        self.healing_value = 50
        self.value = 60


# class Gold(Item):
#     """A Subclass For The Gold Item(s)"""
#
#     def __init__(self, amt):
#         self.amt = amt
#         super(Gold, self).__init__(name="Gold Pieces",
#                                    description="A round coin with {} stamped on the front.".format(str(self.amt)),
#                                    value=self.amt)
