import random 
import math 

choices = ["1", "2", "3", "4"]
yes_no = ["y", "n", "Y", "N"]

class Item:
    def __init__ (self, name, item_type, coins):
        self.name = name
        self.type = item_type
        self.cost = coins

class Weapon(Item):
    def __init__ (self, name, coins, damage, speed):
        super().__init__(name, "weapon", coins)
        self.damage = damage
        self.speed = speed

class Armor(Item):
    def __init__ (self, name, coins, resistance):
        super().__init__(name, "armor", coins)
        self.resistance = resistance

class Food(Item):
    def __init__ (self, name, coins, rations):
        super().__init__(name, "food", coins)
        self.rations = rations

class Potion(Item):
    def __init__ (self, name, coins, health):
        super().__init__(name, "potion", coins)
        self.health = health

class Player:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats
        self.weapon = fist
        self.coins = 5
        self.armor = cloth
        self.spell = spells[0]

    def addItem(self, item):
        item_type = item.type
        if(item_type == "weapon"):
            self.weapon = item
        elif(item_type == "armor"):
            self.armor = item
        elif(item_type == "food"):
            self.food += item.rations
        elif(item_type == "health"):
            self.addHealth(item.health)

class Enemy:
    def __init__(self, name, stats, coins):
        self.name = name
        self.stats = stats
        self.anger = 0
        self.coins = coins

class Stats:
    def __init__(self, strength, dexterity, intelligence, health, mana):
        self.str = strength
        self.dex = dexterity
        self.int = intelligence
        self.totalHP = health
        self.hp = health
        self.mana = mana
        self.food = 30
        self.foodCap = 50
    
    def addHealth(self, amount):
        self.hp += amount
        if(self.hp > self.totalHP):
            self.hp = self.totalHP

    def addMana(self, amount):
        self.mana += amount
        if(self.mana > self.int):
            self.mana = self.int
    
    def toFullHealth():
        self.hp = self.totalHP

    def toFullMana():
        self.mana = self.int
    
    def toFullHunger():
        self.food = self.foodCap

    def addHunger(self, amount):
        self.food += amount
        if(self.food > self.foodCap):
            self.food = self.foodCap

class Spell():
    def __init__ (self, name, description, mana, power):
        self.name = name
        self.desc = description
        self.mana = mana
        self.power = power

# Spells

lightning = Spell("Lightning bolt", "lightning strikes upon enemy", 3, .75)
firebolt = Spell("Firebolt", "Throws flames at enemy", 4, .78)
iceshard = Spell("Ice shard", "Powerful ice strike", 5, .82)
earthquake = Spell("Earth shatter", "Earthquake rumbles enemy", 6, .87)
tornado = Spell("Tornado", "Tornado hits enemy", 7, .93)
plasma = Spell("Plasma ray", "Pelts enemy with pure plasma", 8, 1)
sunstrike = Spell("Sun strike", "Sunrays beam down the enemy", 9, 1.1)
meteor = Spell("Meteor shower", "Crushes enemy from above", 10, 1.25)
snap = Spell("Thanos snap", "I am inevitable", 20, 2)

spells = [lightning, firebolt, iceshard, earthquake, tornado, plasma, sunstrike, meteor, snap]

# Potions:

small_hp = Potion("Small HP potion", 15, 15)
medium_hp = Potion("Medium HP potion", 35, 40)
large_hp = Potion("Large HP potion", 75, 100)
full_hp = Potion("Full HP potion", 100, 10000)

potions = [small_hp, small_hp, medium_hp, medium_hp, small_hp, large_hp, full_hp, medium_hp, small_hp, large_hp, full_hp]

# Food:

banana = Food("banana", 15, 15)
muffin = Food("muffin", 15, 15)
pancake = Food("pancake", 15, 15)
soup = Food("soup", 15, 15)
lasagne = Food("lasagne", 15, 15)
wontons = Food("wontons", 15, 15)
icecream = Food("icecream", 15, 15)
pizza = Food("pizza", 15, 15)
hamburger = Food("hamburger", 15, 15)
cereal = Food("cereal", 15, 15)

food = [banana, muffin, pancake, soup, lasagne, wontons, icecream, pizza, hamburger]

# Weapons:

fist = Weapon("fist", 0, 0, 0)
stick = Weapon("stick", 5, 2, 1)
shortsword = Weapon("shortsword", 15 , 4, 2)
knife = Weapon("knife", 30, 2, 14)
axe = Weapon("axe", 65, 6, 7)
spear = Weapon("spear", 105, 8, 4)
sword = Weapon("sword", 135, 16, 8)
machete = Weapon("machete", 175, 20, 16)
war_scythe = Weapon("war scythe",275 , 32, 6)
battle_axe = Weapon("battle axe", 445 , 48, -5)
war_hammer = Weapon("war hammer", 650, 75, -10)
zeus = Weapon("Zeus's Bolt", 999 ,125, 50)

weapons = [stick, shortsword, knife, axe, spear, sword, machete, war_scythe, battle_axe, war_hammer, zeus]

# Armor:

cloth = Armor("cloth armor", 0, 1)
silk = Armor("silk armor", 5, 2)
leather = Armor("leather armor", 10, 4)
chainmail = Armor("chainmail armor", 35, 9)
copper = Armor("copper armor", 75, 16)
iron = Armor("iron armor", 125, 25)
steele = Armor("steele armor", 165, 36)
chromium = Armor("chromium armor", 240, 49)
celestial = Armor("celestial armor", 350, 64)
dimensional = Armor("dimensional armor", 490, 81)
vibranium = Armor("vibranium armor", 666, 100)

armor = [silk, leather, chainmail, copper, iron, steele, chromium, celestial, dimensional, vibranium]

# Generates Random Numbers
def randomish_num(integer):
    return random.randint(math.floor(integer/2),integer)

def random_num(integer):
    return random.randint(integer)

# Prints out the skills of a player
def print_skills():
    print("Strength = " + str(p.stats.str))
    print("Dexterity = " + str(p.stats.dex))
    print("Intelligence = " + str(p.stats.int))
    print("Health = " + str(p.stats.hp))
    print("Mana = " + str(p.stats.mana) + "\n")

# Function to determine the spacing added to a string
def stringBuilder(string, totalLength):
    if(type(string) != str):
        string = str(string)
    strLength = len(string)
    blankSpaces = ""
    for i in range(totalLength - strLength):
        blankSpaces += " "
    string += blankSpaces
    return string

# Prints out the store
def print_store():
    print("********************************")
    print("      item          |   Cost  ")
    print("1. " + stringBuilder(potions[0].name, 17) + "| " + stringBuilder(potions[0].cost, 4) + " coins")
    print("2. " + stringBuilder(weapons[0].name, 17) + "| " + stringBuilder(weapons[0].cost, 4) + " coins")
    print("3. " + stringBuilder(food[0].name, 17) + "| " + stringBuilder(food[0].cost, 4) + " coins")
    print("4. " +  stringBuilder(armor[0].name, 17) + "| " + stringBuilder(armor[0].cost, 4) + " coins")
    print("********************************\n")

# Prints out a want to shop message
def store_msg():
    print("Would you like to buy something before going on the journey? " + "You have " + str(p.coins) + " coins to spend (Y/N)\n")

# Allows user to buy an item
def store_buy(item, itemArray):
    if(p.coins >= item.cost):
        response = ""
        while response not in yes_no:
            response = input("Are you sure you want to purchase: " + item.name + "? (Y/N) \n")
            if(response.lower() == "y"):
                p.coins -= item.cost
                p.addItem(item)
                itemArray.remove(item)
                print("Thanks for purchasing: " + item.name + "! You have " + str(p.coins) + " coins remaining! \n")
    else:
        print("Sorry you don't have enough coins to buy this item!")
        
def store(enemy):
    response = ""
    while response not in yes_no:
        print_store()
        store_msg()
        response = input()
        if (response.lower() == "y"):
            response = ""
            if(p.coins < 3):
                response = input("Shopkeeper: You don't have enough money to buy anything here! Do you want to earn some money? (Y/N)\n")
                if(response.lower() == "y"):
                    print("Alright you are going to have to battle the " + enemy.name + " on my brother's farm")
                    # Start a fight with wolves
            else:
                while response not in choices:
                    response = ""
                    response = input("What would you like to purchase? (Type <1, 2, 3, 4> based on the corresponding items)\n")
                    if(response == "1"):
                        store_buy(potions[0], potions)
                    elif(response == "2"):
                        store_buy(weapons[0], weapons)
                    elif(response == "3"):
                        store_buy(food[0], food)
                    elif(response == "4"):
                        store_buy(armor[0], armor)
                    else:
                        print("Please respond with 1, 2, 3, or 4!")

def battle(player, enemy):
    turn = ""
    if(player.stats.dex > enemy.stats.dex):
        turn = player.name
    else:
        turn = enemy.name
    while(player.stats.hp > 0 and enemy.stats.hp > 0):
        turn = fight(player, enemy, turn)
    if(player.stats.hp < 0):
        print("You lose! Should've trained harder! THE END! \n")
    else:
        print("Congrats, you defeated the " + enemy.name)

def fightMenu():
    print("******************************************************")
    print("      options          |          Description         ")
    print("1. Melee Attack        | " + shopStringBuilder(potions[0].cost, 4) + " coins")
    print("2. Cast "  + stringBuilder(player.spells[0].name, 20) + "| " + stringBuilder(player.spells[0].desc, 29) + " coins")
    print("3. Rest                | Gain back health and mana    ")
    print("4. Run                 | Evade fight                  ")
    print("******************************************************\n")
    

def fight(player, enemy, turn):
    if(turn == player.name):
        while response not in choices:
            response = ""
            fightMenu()
            response = input("What would you like to purchase? (Type <1, 2, 3, 4> based on the corresponding items)\n")
            if(response == "1"):
                attack()
            elif(response == "2"):
                castSpell()
            elif(response == "3"):
                heal()
            elif(response == "4"):
                retreat()
            else:
                print("Please respond with 1, 2, 3, or 4!")
        return enemy.name
    elif(turn == enemy.name):
        return player.name

def getStats(strength, dexterity, intelligence, health, mana):
    return Stats(randomish_num(strength), randomish_num(dexterity), randomish_num(intelligence), randomish_num(health), randomish_num(mana))

name = input("Hello! What is your name, soldier\n")
playerStats = getStats(10, 25, 20, 50, 30)
p = Player(name, playerStats)
print("Hello, " + p.name + ". You are chosen to go on this quest to slay the fire dragon!\n")
print("Throughout all your training, you gained these skills:\n")
print_skills()
print("These skills are going to play a roll in whether you defeat the dragon or not\n")

# Begin Game!
print("You leave early morning, and come across to a nearby village for food and supplies")
wolfStats = getStats(3, 15, 0, 20, 0)
wolf = Enemy("Wolf", wolfStats, 7)
store(wolf)

                
