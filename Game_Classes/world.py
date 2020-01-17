import random
import enemies
import npc


class MapTile:
    """The Base Class For Map Tiles"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create A Subclass Instead")

    def modify_player(self, player):
        pass


class StartTile(MapTile):
    def intro_text(self):
        return """
        You find yourself in a cave with a flickering torch on the wall. 
        You can make out four paths, each equally as dark and foreboding."""


class BoringTile(MapTile):
    def intro_text(self):
        return """This is a very boring part of the cave."""


class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.50:
            self.enemy = enemies.GiantSpider()
            self.alive_text = "A giant spider jumps down from its web in front of you!"
            self.dead_text = "The corpse of a dead spider rots on the ground."
        elif r < 0.80:
            self.enemy = enemies.Ogre()
            self.alive_text = "An ogre is blocking your path!"
            self.dead_text = "A dead ogre reminds you of you triumph."
        elif r < 0.90:
            self.enemy = enemies.BatColony()
            self.alive_text = "You hear a squeaking noise growing louder ...suddenly you are lost in a swarm of bats!"
            self.dead_text = "Dozens of dead bats are scattered on the ground."
        else:
            self.enemy = enemies.RockMonster()
            self.alive_text = "You've disturbed a rock monster from his slumber!"
            self.dead_text = "Defeated, the monster has reverted into an ordinary rock."

        super(EnemyTile, self).__init__(x, y)

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.health = player.health - self.enemy.max_damage
            print("{} does {} damage. You have {} HP remaining".format(self.enemy.name, self.enemy.max_damage,
                                                                       player.health))

    def intro_text(self):
        if self.enemy.is_alive():
            return self.alive_text
        else:
            return self.dead_text


class TraderTile(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.trader = npc.Trader()

    def intro_text(self):
        return """
        A frail not-quite-human, not-quite-creature squats in 
        the corner clinking his gold coins together. 
        He looks willing to trade.
        """

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Gold".format(i, item.name, item.value))
        while True:
            user_input = input("Choose an item or press Q to exit: ")
            if user_input.lower() in ['q']:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)
                except ValueError:
                    print("Invalid choice")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("That's too expensive")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("Trade complete")

    def check_if_trade(self, player):
        while True:
            print("Would you like to (B)uy, (S)ell, or (Q)uit?")
            user_input = input().lower()
            if user_input in ['q']:
                return
            elif user_input in ['b']:
                print("Here's whats available to buy: ")
                self.trade(buyer=player, seller=self.trader)
            elif user_input in ['s']:
                print("Here's whats available to sell: ")
                self.trade(buyer=self.trader, seller=player)
            else:
                print("Invalid choice!")


class FindGoldTile(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.gold = random.randint(1, 50)
        self.gold_claimed = False

    def intro_text(self):
        if self.gold_claimed:
            return """
               Another unremarkable part of the cave. 
               You must forge onwards.
               """
        else:
            return """
               Someone dropped some gold. You pick it up.
               """

    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            print("+{} gold added.".format(self.gold))


class VictoryTile(MapTile):
    def modify_player(self, player):
        player.victory = True

    def intro_text(self):
        return """You see a bright light in the distance...\n... it grows as you get closer! It's sunlight!
        \n\nVictory is yours!"""


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None


def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|VT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False

    return True


world_dsl = """
|ET|ET|VT|ET|ET|
|ET|  |  |  |BT|
|BT|ET|FG|  |TT|
|TT|  |ST|FG|ET|
|FG|  |BT|  |FG|
"""

world_map = []

tile_type_dict = {"ST": StartTile,
                  "VT": VictoryTile,
                  "ET": EnemyTile,
                  "BT": BoringTile,
                  "FG": FindGoldTile,
                  "TT": TraderTile,
                  "  ": None}

start_tile_location = None


def parse_world_dsl():
    # Validating DSL
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid")

    """Splitting the DSL into lines and removing the empty lines created by the triple-quote syntax."""
    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    """Iterate over each line in the DSL. Instead of i, the variable y is used because we're working with an X-Y 
    grid. """
    for y, dsl_row in enumerate(dsl_lines):
        # Create an object to store the tiles
        row = []
        # Splitting the line into abbreviations using the "split" method
        dsl_cells = dsl_row.split("|")
        # The split method includes the beginning and end of the line so we remove those nonexistent cells
        dsl_cells = [c for c in dsl_cells if c]
        # Iterating over each cell in the DSL line
        for x, dsl_cell in enumerate(dsl_cells):
            # Looking up the abbreviation in the dictionary
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            """Looking up the abbreviation in the dictionary tile_type = tile_type_dict[dsl_cell] If the dictionary 
            returned a valid type, create a new tile object, pass it the X-Y coordinates as required by the 
            tiles __init__(), and add it to the row object. If None was found in the dictionary, we just add None. """
            row.append(tile_type(x, y) if tile_type else None)
        # Adding the whole row to the world_map
        world_map.append(row)
