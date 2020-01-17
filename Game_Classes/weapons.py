class Weapon:
    """The Base Class For All Weapons"""

    def __init__(self, name, description, max_damage, value):
        self.name = name
        self.description = description
        self.max_damage = max_damage
        self.value = value

    def __str__(self):
        return self.name


class Rock(Weapon):
    def __init__(self):
        super(Rock, self).__init__(name='Rock', description='A fist-sized rock, suitable for bludgeoning.',
                                   max_damage=5, value=1)


class Dagger(Weapon):
    def __init__(self):
        super(Dagger, self).__init__(name='Dagger',
                                     description='A small dagger with some rust. Somewhat more dangerous than a rock.',
                                     max_damage=10, value=20)


class RustySword(Weapon):
    def __init__(self):
        super(RustySword, self).__init__(name='Rusty Sword',
                                         description='This sword is showing its age, but still has some fight in it.',
                                         max_damage=20, value=100)


class Crossbow(Weapon):
    def __init__(self):
        super(Crossbow, self).__init__(name='Crossbow', description='A ranged weapon in similar principle to a bow '
                                                                    'that shoots arrows.',
                                       max_damage='20', value=120)


class Axe(Weapon):
    def __init__(self):
        super(Axe, self).__init__(name='Axe',
                                  description='Upon a handle of aged old oak sits a blade of sharpest steel.',
                                  max_damage=40, value=200)
