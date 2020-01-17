import items
import weapons
import world


class Player:
    def __init__(self):
        self.inventory = [weapons.Rock(), weapons.RustySword(), weapons.Dagger(), items.CrustyBread()]
        self.x = world.start_tile_location[0]
        self.y = world.start_tile_location[1]
        self.health = 100
        self.gold = 5
        self.victory = False

    def is_alive(self):
        return self.health > 0

    def print_inventory(self):
        print('Inventory:')
        for item in self.inventory:
            print('* ' + str(item))
        print("* Gold: {}".format(self.gold))

    def most_powerful_weapon(self):
        most_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.max_damage > most_damage:
                    best_weapon = item
                    most_damage = item.max_damage
            except AttributeError:
                pass
        return best_weapon

    def heal(self):
        consumables = [item for item in self.inventory if isinstance(item, items.Consumable)]
        if not consumables:
            print("You don't have any items to heal you!")
            return

        for i, item in enumerate(consumables, 1):
            print("Choose an item to use to heal: ")
            print("{}. {}".format(i, item))

        valid = False
        while not valid:
            choice = input("")
            try:
                to_eat = consumables[int(choice) - 1]
                self.health = min(100, self.health + to_eat.healing_value)
                self.inventory.remove(to_eat)
                print("Current HP: {}".format(self.health))
                valid = True
            except (ValueError, IndexError):
                print("Invalid Choice try again")

    def attack(self):
        best_weapon = self.most_powerful_weapon()
        room = world.tile_at(self.x, self.y)
        enemy = room.enemy
        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.health -= best_weapon.max_damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.health))

    def trade(self):
        room = world.tile_at(self.x, self.y)
        room.check_if_trade(self)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)
