class Enemy:
    """The Base Class For All Enemies"""

    def __init__(self, name, health, max_damage):
        self.name = name
        self.health = health
        self.max_damage = max_damage

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.health > 0


class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", health=10, max_damage=2)


class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", health=30, max_damage=15)


class BatColony(Enemy):
    def __init__(self):
        super(BatColony, self).__init__(name="Colony of Bats", health=100, max_damage=4)


class RockMonster(Enemy):
    def __init__(self):
        super(RockMonster, self).__init__(name="Rock Monster", health=80, max_damage=15)
