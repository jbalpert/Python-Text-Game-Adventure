import random 
import math
import sys
import os

choices = ["1", "2", "3", "4"]
yes_no = ["y", "n", "Y", "N"]

# class Dungeon:
#     def __init__ (self, name, roomNum, monsters, level, boss, isGold = True, isTraps = True, isSkill = False, isShop = True):
#         self.structure = []
#         self.name = name
#         self.roomNum = roomNum
#         self.isGold = isGold
#         self.isTraps = isTraps
#         self.isShop = isShop
#         self.isSkill = isSkill
#         self.level = level
#         self.boss = boss
    
#     def create(self):
#         roomsLeft = self.roomNum
#          = proportionRooms(self)
#         while(total_rooms > 0)
#             room, roomsLeft = makeRoom(rooms)
#             self.structure.append(room)

#     def makeRoom(self, roomsLeft):
        

class Item:
    def __init__ (self, name, item_type, coins=0):
        self.name = name
        self.type = item_type
        self.cost = coins

class Spell(Item):
    def __init__ (self, name, description, mana, power):
        super().__init__(name, "spell")
        self.desc = description
        self.mana = mana
        self.power = power

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
        self.coins = 0
        self.armor = cloth
        self.spell = spells[0]

    def addItem(self, item):
        item_type = item.type
        if(item_type == "weapon"):
            currentWeapon = self.weapon
            self.weapon = item
            print("You upgraded your weapon from " + currentWeapon.name + " to " + self.weapon.name + "!\n")
        elif(item_type == "armor"):
            currentArmor = self.armor
            self.armor = item
            self.stats.totalHP += item.resistance
            print("You upgraded your armor from " + currentArmor.name + " to " + self.armor.name + "!\n")
        elif(item_type == "food"):
            print("YUM! Eating the " + item.name + " added " + str(item.rations) + " to your mana and saturation!\n")
            self.stats.addHunger(item.rations)
            self.stats.addMana(item.rations)
        elif(item_type == "health"):
            print("Drinking the " + item.name + " added " + str(item.rations) + " to your mana and saturation!\n")
            self.addHealth(item.health)
        elif(item_type == "spell"):
            self.spell = item

    def armorCheck(self):
        num = random_num(5)
        if(num == 1 or num == 2):
            return True
        else:
            return False

    def dexCheck(self):
        if(random_num(100) < math.floor((self.stats.dex + self.weapon.speed) * .1)):
            print("Congrats! Your incredible speed allows you to strike AGAIN \n")
            return True
        else:
            return False

    def attack(self, enemy):
        print("You chose to attack the enemy with your " + self.weapon.name + "!\n")
        hit = randomish_num(self.stats.str)
        if(hit == random.randint(math.floor(self.stats.str/2),self.stats.str)):
            print("You missed the " + enemy.name + " on your attack!\n")
        else:
            hit += self.weapon.damage
            print("You dealt " + str(hit) + " damage to the " + enemy.name + "\n")
            enemy.stats.hp -= hit
            if(self.dexCheck()):
                self.attack(enemy)

    def castSpell(self, enemy):
        print("You chose to attack the enemy with your " + self.spell.name + "!\n")
        hit = self.spell.power * self.stats.int
        self.stats.mana -= self.spell.mana
        print("You dealt " + str(hit) + " damage to the " + enemy.name + "\n")
        enemy.stats.hp -= hit
        if(self.dexCheck()):
            self.attack(enemy)

    def rest(self):
        print("You chose to rest give your body a rest!\n")
        healthGain = math.floor(random_numLow(self.stats.totalHP)*.33)
        manaGain = math.floor(random_numLow(self.stats.int)*.33)
        self.stats.addHealth(healthGain)
        self.stats.addMana(manaGain)
        print("You gained " + str(healthGain) + " hp and " + str(manaGain) + " mana from your short rest!\n")

    def retreat(self):
        run = random_num(100)
        print(run)
        print(self.stats.dex)
        if(run < self.stats.dex):
            print("You have successfully escaped!\n")
            return True
        else:
            print("You failed to escape\n")
            return False

    def addXP(self, xp):
        self.stats.xp += xp
        print("You have " + str(self.stats.xp) + " / " + str(self.stats.xpToLevelUp) + " experience points!\n")
        while(self.stats.xp >= self.stats.xpToLevelUp):
            self.stats.xp -= self.stats.xpToLevelUp
            self.levelUp()

    def levelUp(self):
        print("Well done " + self.name + " you leveled up!\n")
        self.stats.level += 1
        self.stats.xpToLevelUp = math.ceil(self.stats.xpToLevelUp * 1.1)
        if(self.stats.level % 5 == 0 and not spells == []):
            self.gainSpell()
        else:
            skillPoints = math.ceil(self.stats.level / 2)
            skillBonus = random_numLow(skillPoints)
            print("You gained " + str(skillBonus) + " skill points for leveling up!\n")
            self.stats.sp += skillBonus
            input(" ")
            clear()
            self.skillRaise()
        print("You have " + str(self.stats.xp) + " / " + str(self.stats.xpToLevelUp) + " experience points!\n")

    def gainSpell(self):
        spells.remove(spells[0])
        self.addItem(spells[0])
        print("You have found time to practice your wizardry and learned the " + self.spell.name + " spell!\n")

    def skillRaise(self):
        response = ""
        while response not in choices:
            print_skills()
            print("You have " + str(self.stats.sp) + " skill points to use to level up your stats!")
            response = input("What stats would you like to increase? (Type <1, 2, 3, 4> based on the corresponding items)\n")
            clear()
            if response in choices:
                response = self.skillup(response)
            else:
                print("Please respond with 1, 2, 3, or 4!\n")
    
    def skillup(self, response):
        if(response == "1"):
            self.stats.sp -= 1
            self.stats.str += 1
            print("You went to a weight room and leveled up your strength, you now have " + str(self.stats.str) + " strength! \n")
        elif(response == "2"):
            self.stats.sp -= 1
            self.stats.dex += 1
            print("You leveled up your dexterity, you now have " + str(self.stats.dex) + " dexterity \n")
        elif(response == "3"):
            self.stats.sp -= 1
            self.stats.int += 1
            print("You studied in your spare time and gained intelligence, you now have " + str(self.stats.int) + " intelligence \n")
        elif(response == "4"):
            self.stats.sp -= 1
            self.stats.totalHP += 2
            self.stats.hp += 2
            print("You leveled up your health, you now have " + str(self.stats.totalHP) + " health \n")
        if(self.stats.sp == 0):
            return response
        else:
            response = ""
            return response
class Enemy:
    def __init__(self, name, stats, coins, experience):
        self.name = name
        self.stats = stats
        self.anger = 0
        self.coins = coins
        self.xp = experience
    
    def dexCheck(self):
        if(random_num(100) < math.floor(self.stats.dex * .1)):
            print("The enemies incredible speed allows it to strike TWICE\n")
            return True
        else:
            return False

    def attack(self, player):
        hit = randomish_num(self.stats.str)
        if(hit == random.randint(math.floor(self.stats.str/2),self.stats.str)):
            print("Luckily, the " + self.name + " missed you!\n")
        elif(hit <= player.armor.resistance and player.armorCheck()):
            print("Your " + player.armor.name + " prevented you from taking damaged\n")
        else:
            print("The " + self.name + " dealt " + str(hit) + " damage to the " + player.name + "\n")
            player.stats.hp -= hit
            if(self.dexCheck()):
                self.attack(player)

class Stats:
    def __init__(self, strength, dexterity, intelligence, health):
        self.str = strength
        self.dex = dexterity
        self.int = intelligence
        self.totalHP = health
        self.hp = health
        self.mana = intelligence
        self.food = 30
        self.foodCap = 50
        self.xp = 0
        self.xpToLevelUp = 20
        self.level = 1
        self.sp = 0
    
    def addHealth(self, amount):
        self.hp += amount
        if(self.hp > self.totalHP):
            self.hp = self.totalHP

    def addMana(self, amount):
        self.mana += amount
        if(self.mana > self.int):
            self.mana = self.int
    
    def toFullHealth(self):
        self.hp = self.totalHP

    def toFullMana(self):
        self.mana = self.int
    
    def toFullHunger(self):
        self.food = self.foodCap

    def addHunger(self, amount):
        self.food += amount
        if(self.food > self.foodCap):
            self.food = self.foodCap

    def buffStats(self, percent, add=0):
        self.str = math.floor((self.str * percent) + add)
        self.dex = math.floor((self.dex * percent) + add)
        self.int = math.floor((self.int * percent) + add)
        self.totalHP = math.floor((self.totalHP * percent) + add)
        self.toFullHealth()
        self.toFullMana()

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
stick = Weapon("stick", 5, 1, 1)
butter_knife = Weapon("butter knife", 35, 2, 2)
shortsword = Weapon("shortsword", 95, 4, 2)
katana = Weapon("katana", 135, 6, 4)
axe = Weapon("axe", 170, 8, 5)
butcher_knife = Weapon("butcher's knife", 215, 13, 3)
spear = Weapon("spear", 270, 14, 5)
sword = Weapon("sword", 335, 21, 10)
machete = Weapon("machete", 420, 28, 18)
war_scythe = Weapon("war scythe", 525, 36, 20)
battle_axe = Weapon("battle axe", 670, 48, 3)
war_hammer = Weapon("war hammer", 1025, 72, 10)
lightsaber = Weapon("Lightsaber", 1650, 100, 75)
zeus = Weapon("Zeus's Bolt",2500 ,185, 100)

weapons = [stick, butter_knife, shortsword, katana, axe, butcher_knife, spear, sword, machete, war_scythe, battle_axe, war_hammer, lightsaber, zeus]

# Armor:

cloth = Armor("cloth armor", 0, 1)
silk = Armor("silk armor", 25, 2)
leather = Armor("leather armor", 80, 4)
chainmail = Armor("chainmail armor", 190, 9)
copper = Armor("copper armor", 280, 16)
iron = Armor("iron armor", 365, 25)
steele = Armor("steele armor", 460, 36)
chromium = Armor("chromium armor", 570, 49)
celestial = Armor("celestial armor", 715, 64)
dimensional = Armor("dimensional armor", 1120, 100)
vibranium = Armor("vibranium armor", 2000, 150)

armor = [silk, leather, chainmail, copper, iron, steele, chromium, celestial, dimensional, vibranium]

# Simple way to implement stats in an enemy or player 
def getStats(strength, dexterity, intelligence, health):
    return Stats(randomish_num(strength), randomish_num(dexterity), randomish_num(intelligence), randomish_num(health))

# Generates Random Numbers
def randomish_num(integer):
    return random.randint(math.floor(integer/2),integer)

def random_num(integer):
    return random.randint(1, integer)

def random_numLow(integer):
    if(math.floor(integer/2) < 1):
        return 1
    return random.randint(1, math.floor(integer/2))

# Prints out the skills of a player
def print_skills():
    print("***********************************************************************")
    print("1.) Strength     = " + stringBuilder(p.stats.str, 5) + "Affects how much damage you inflict on an enemy")
    print("2.) Dexterity    = " + stringBuilder(p.stats.dex, 5) + "Affects your speed and chance to combo")
    print("3.) Intelligence = " + stringBuilder(p.stats.int, 5) + "Affects your mana and spell strength")
    print("4.) Health       = " + stringBuilder(p.stats.hp, 5)  + "Affects your total amount of hp")
    print("***********************************************************************\n")
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

# Allows user to buy an item
def store_buy(item, itemArray):
    if(p.coins >= item.cost):
        response = ""
        while response not in yes_no:
            response = input("Are you sure you want to purchase the " + item.name + " that costs " + str(item.cost) + " coins? (Y/N) \n")
            if(response.lower() == "y"):
                p.coins -= item.cost
                p.addItem(item)
                itemArray.remove(item)
                print("Thanks for purchasing the " + item.name + "! You have " + str(p.coins) + " coins remaining! \n")
            elif(response.lower() == "n"):
                print("We will put this item back on the shelf!\n")
            else:
                yesnoInputFail()
    else:
        print("Sorry you don't have enough coins to buy this item!\n")

# Store Module    
def store(enemy, coinMin):
    response = ""
    while response not in yes_no:
        print_store()
        response = input("Would you like to buy something before going on the journey? " + "You have " + str(p.coins) + " coins to spend (Y/N)\n")
        clear()
        if (response.lower() == "y"):
            response = ""
            if(p.coins <= coinMin and p.coins < min(potions[0].cost ,weapons[0].cost, food[0].cost, armor[0].cost)):
                response = earnShopMoney(enemy, coinMin)
            elif(p.coins < min(potions[0].cost ,weapons[0].cost, food[0].cost, armor[0].cost)):
                print("Sorry you don't have enough coins to shop here!\n")
            else:
                while response not in choices:
                    print_store()
                    response = input("What would you like to purchase? (Type <1, 2, 3, 4> based on the corresponding items)\n")
                    clear()
                    if(response == "1"):
                        store_buy(potions[0], potions)
                    elif(response == "2"):
                        store_buy(weapons[0], weapons)
                    elif(response == "3"):
                        store_buy(food[0], food)
                    elif(response == "4"):
                        store_buy(armor[0], armor)
                    else:
                        print("Please respond with 1, 2, 3, or 4!\n")
        elif(response.lower() == "n"):
            response = ""
            if(p.coins <= coinMin):
                response = earnShopMoney(enemy, coinMin)
            else:
                response = "n"
                print("You decide to leave the shop to continue your quest!\n")
        else:
            yesnoInputFail()

def earnShopMoney(enemy, coinMin):
    response = ""
    while response not in yes_no:
        response = input("Shopkeeper: You are dirt poor! Do you want to earn some money? (Y/N)\n")
        clear()
        if(response.lower() == "y"):
            response = ""
            storeBattle(enemy)
            return response
        elif(response.lower() == "n"):
            print("That's fine! Come again soon!\n")
            return response
        else:
            yesnoInputFail()
        
def yesnoInputFail():
    print("Sorry I couldn't understand, (type: Y/N)\n")

def choiceInputFail():
    print("Please respond with 1, 2, 3, or 4!\n")

# Store Battle for coins
def storeBattle(enemy):
    print("Alright you are going to have to battle the " + enemy.name + " on my brother's farm\n")
    print("You travel a bit to the farm and see in the distance a menacing " + enemy.name + "!\n")
    input(" ")
    clear()
    battle(p, enemy)
    

# Battle Module
def battle(player, enemy):
    enemy_coins = enemy.coins
    enemy_xp = enemy.xp
    turn = ""
    if(player.stats.dex > enemy.stats.dex):
        print("Since your dexterity is higher than the enemy, you get to go first!\n")
        turn = player.name
    else:
        print("Since your dexterity is lower than the enemy, you get to go second.\n")
        turn = enemy.name
    while(player.stats.hp >= 0 and enemy.stats.hp >= 0):
        turn = fight(player, enemy, turn)
        printHealth(player, enemy)
        input(" ")
        clear()
    if(player.stats.hp <= 0):
        print("You lose! Should've trained harder! THE END! \n")
        sys.exit(":(")
    elif(enemy.stats.hp == -100000):
        print("You left quickly to saftey! Phew that was a close one!\n")
        enemy.stats.toFullHealth()
        enemy.coins = math.ceil(enemy_coin * .75)
        enemy.xp = math.ceil(enemy_xp * .75)
    else:
        coinReward = randomish_num(enemy.coins)
        xpReward = randomish_num(enemy.xp)
        enemy.stats.buffStats(1.25)
        print("Congrats, you defeated the " + enemy.name)
        print("You earned " + str(coinReward) + " coins and " + str(xpReward) + " experience from the fight!\n")
        player.addXP(xpReward)
        player.coins += coinReward
        player.stats.food -= random_num(3)
        if(player.stats.food > 5):
            player.stats.addHealth(random_numLow(player.stats.totalHP))
            player.stats.addMana(random_numLow(player.stats.int))

# Prints fight menu during a player's turn
def fightMenu():
    print("******************************************************")
    print("      options          |          Description         ")
    print("1. Melee Attack        | Strike with " + p.weapon.name  + "!")
    print("2. Cast "  + stringBuilder(p.spell.name, 15) + "| " + stringBuilder(p.spell.desc, 29))
    print("3. Rest                | Gain back health and mana    ")
    print("4. Run                 | Evade fight                  ")
    print("******************************************************\n")
    
# Runs the battle
def fight(player, enemy, turn):
    response = ""
    if(turn == player.name):
        while response not in choices:
            response = ""
            printHealth(player, enemy)
            fightMenu()
            response = input("It is your turn! (Type <1, 2, 3, or 4> based on the corresponding options to fight!)\n")
            clear()
            if(response == "1"):
                player.attack(enemy)
            elif(response == "2" and player.stats.mana >= player.spell.mana):
                player.castSpell(enemy)
            elif(response == "3"):
                player.rest()
            elif(response == "4"):
                if(player.retreat()):
                    enemy.stats.hp = -100000
                    enemy.xp = 0
                    enemy.coins = 0
                else:
                    pass
            else:
                print("You need to respond with 1, 2, 3, or you don't have enough mana to cast the spell!\n")
                fight(player, enemy, turn)
        return enemy.name
    elif(turn == enemy.name):
        enemy.attack(player)
        return player.name

def printHealth(player, enemy):
    print("********************************************")
    print(" " + stringBuilder(player.name, 12) + " hp: " + stringBuilder((str(player.stats.hp) + " / " + str(player.stats.totalHP)), 12) + "Mana: " + stringBuilder((str(player.stats.mana) + " / " + str(player.stats.int)), 12))
    print(" " + stringBuilder(enemy.name, 12) + " hp: " + stringBuilder((str(enemy.stats.hp) + " / " + str(enemy.stats.totalHP)), 12) + "Mana: " + stringBuilder((str(enemy.stats.mana) + " / " + str(enemy.stats.int)), 12))
    print("********************************************\n")

def clear():
    os.system('cls||clear')

def forest(p):
    response = ""
    print("You come across a dense forest with towering trees, you have a bad feeling about this.")
    print("Despite your concerns, you are a warrior and continue and enter the forest")
    print("Cutting through vines with your "  + p.weapon.name + " you see a path in the distance")
    while response not in yes_no:
        response = input("Do you want to investigate the path? (Y/N)\n").lower()
        clear()
        if(response == 'y'):
            response = investFpath(p)
        elif(response == 'n'):
            response = navigateF(p)
            print("You got so confused navigating the forest that you came back to the same first path!")
        else:
            yesnoInputFail()

def easyMonsters(version, name, coins = 25, xp = 25):
    stats = ""
    if(version == "fast"):
        stats = getStats(3, 200, 20, 20)
    elif(version == "normal"):
        stats = getStats(5,10,20,30)
    elif(version == "slow"):
        stats = getStats(10, 2, 2, 40)
    elif(version == "boss"):
        stats = getStats(12, 15, 15, 100)
        coins *= 4
        xp *= 4
    return Enemy(name, stats, coins, xp)

def mediumMonsters(version, name, coins = 75, xp = 75):
    stats = ""
    if(version == "fast"):
        stats = getStats(6, 333, 20, 35)
    elif(version == "normal"):
        stats = getStats(12,40,40,70)
    elif(version == "slow"):
        stats = getStats(22, 10, 10, 100)
    elif(version == "boss"):
        stats = getStats(24, 40, 40, 250)
        coins *= 4
        xp *= 4
    return Enemy(name, stats, coins, xp)

def hardMonsters(version, name, coins = 150, xp = 150):
    stats = ""
    if(version == "fast"):
        stats = getStats(15, 500, 20, 70)
    elif(version == "normal"):
        stats = getStats(30, 100, 100, 150)
    elif(version == "slow"):
        stats = getStats(50, 20, 20, 325)
    elif(version == "boss"):
        stats = getStats(75, 100, 100, 500)
        coins*= 4
        coin *= 4
    return Enemy(name, stats, coins, xp)

def dragon(name):
    stats = getStats(125, 666, 555, 1500)
    return Enemy(name, stats, 1200, 1000)

def getRandomMonster(arr):
    num = random_num(len(arr)-1)
    return arr[num]

def skyPaths():
    print("1. Go to the cloud shop! ")
    print("2. Go explore the sky dungeon")
    print("3. Keep searching to the left")
    print("4. Keep searching to the right \n")

def skyZone(p):
    print("You reach the top of the tree and find that you can magically walk on the clouds")
    print("These clouds have a bit of a bounce to it as you hop forward")
    print("Through the mist, you can see a cloud shop and what looks to be a dungeon in the distance!\n")
    input(" ")
    clear()
    response = ""
    while response not in choices:
        skyPaths()
        response = input("Select a path to choose (1, 2, 3, or 4)\n")
        clear()
        if(response == "1"):
            monster = getRandomMonster(skyCreatures)
            print("You start heading towards the shop, when suddenly a " + monster.name + " attacks you!")
            battle(p,monster)
            print("Thankfully, you survived that attack and go into the shop")
            store(getRandomMonster(skyCreatures), 15)
            response = ""
        elif(response == "2"):
            print("You start heading to the dungeon, when you come across a happy little cloud child")
            print("She sneezes a small puff of cloud as you pass them")
            input(" ")
            clear()
            print("You smile at the kid, and start walking past them, but the entire cloud you are on turns grey")
            print("The child takes the form of a demon witch and flies above you looking down upon you")
            print("YoU thInk YoU aRE goInG in My dOmaIN yOunG tRaveLer? I thInK NOT!")
            print("The witch spawned many monsters to try and stop you from entering the dungeon")
            input(" ")
            clear()
            for i in range(random_num(6)):
                monster = getRandomMonster(skyCreatures)
                print("The witch's " + monster.name + " comes to battle you!\n" )
                battle(p, monster)
            print("Wow I can't believe that witch spawned all those creatures on me!")
            print("HEHEHEHEHEEEEEEEE you coward face me peasant in my dungeon if you want to kill me!")
            input(" ")
            clear()
            response = ""
        elif(response == "3"):
            chanceFate(p)
            response = ""
        elif(response == "4"):
            chanceFate(p)
            response = ""
        else:
            choiceInputFail()

def chanceFate(p):
    chance = random_num(3)
    if(chance == 1):
        monster = getRandomMonster(skyCreatures)
        print("You get attacked by a " + monster.name + "!\n")
        input(" ")
        clear()
        battle(p, monster)
    elif(chance == 2):
        if(p.coins < 5):
            print("Nothing seems to interesting over here!")
        else:
            print("As you walked, a thief quickly took gold from you!")
            if(p.coins < 25):
                p.coins-=5
            elif(p.coins < 75):
                p.coins-=20
            elif(p.coins < 250):
                p.coins -= 50
            else:
                p.coins -= 100
    else:
        monster = getRandomMonster(skyCreatures)
        monster2 = getRandomMonster(skyCreatures)
        print("You get attacked by a " + monster.name + "!\n")
        input(" ")
        clear()
        battle(p, monster) 
        print("You get attacked again by the monsters friend, a " + monster2.name + "!\n")
        input(" ")
        clear()
        battle(p, monster2)
        print("You find a treasure chest and find that there are 20 coins inside!")
        p.coins += 20

def navigateF(p):
    goblinStats = getStats(4, 350, 1, 30)
    goblin = Enemy("goblin", goblinStats, 6, 10)
    print("You see a many possible ways to travel")
    response = ""
    while response not in choices:
        forestPaths(p)
        response = input("Select a path to choose (1, 2, 3, or 4)\n")
        clear()
        if(response == "1"):
            print("You start scaling the tree, branch by branch you are almost to the top")
            monster = getRandomMonster(skyCreatures)
            print("You see a " + monster.name + " on a thick tree branch.")
            while response not in yes_no:
                response = input("Do you want to attack it? (Y/N)\n").lower()
                clear()
                if(response == 'y'):
                    battle(p,monster)
                elif(response == 'n'):
                    print("The " + monster.name + " strikes you without hesitation")
                    print("You lose " + str(monster.stats.str) + " health!")
                    p.stats.hp -= monster.stats.str
                    input(" ")
                    clear()
                    battle(p, monster)
                else:
                    yesnoInputFail()
                skyZone(p)
        elif(response == "2"):
            pass
        elif(response == "3"):
            pass
        elif(response == "4"):
            pass
        else:
            choiceInputFail()

def forestPaths(p):
    print("1. Climb to the top of the tree ")
    print("2. Cross the flowing river")
    print("3. Keep searching to the left")
    print("4. Keep searching to the right \n")

def investFpath(p):
    print("As you continue to the path you hear rustling in a bush nearby")
    response = ""
    while response not in yes_no:
        response = input("Do you want to draw your weapon?(y/n)").lower()
        clear()
        if(response == 'y'):
            print("Drawing your " + p.weapon.name + " you are alert that there might be enemies nearby")
            print("Three small, but nimble goblins jump out of the bushes and surprise you!")
            input(" ")
            clear()
            goblins = []
            for i in range(3):
                goblinStats = getStats(4, 350, 1, 30)
                goblin = Enemy("goblin", goblinStats, 6, 10)
                battle(p, goblin)
                if(i == 1):
                    print("The second goblin jumps and attacks you with its claws")
                elif(i == 2):
                    print("The last goblin jumps right into battle!")
                input(" ")
                clear()
            print("After you kill the goblins, you quickly go to examine the path")
        elif(response == 'n'):
            print("You don't seem to alarmed by the rustling and continue to examine the pathway")
            print("Noticing footprints and what looks to be chariot tracks, realize that people are close")
            input(" ")
            clear()
            print("Suddenly, four men in gladiator armor appear from the bushes and demand to know what you are doing\n")
            gladiator(p)
        else:
            yesnoInputFail()
        print("The path diverges into many different directions...")
        navigateF(p)

def gladiatorTalk(p):
    print("Response to the gladiator:")
    print("1. I am " + p.name + " and am here to slay the dragon in the dragon's cove")
    print("2. You don't need to know who I am, leave me at once")
    print("3. I'm here to train with you because I am the chosen one")
    print("4. ... \n")

def gladiator(p):
    gladiators = []
    for i in range(4):
        gladiatorStats = getStats(7, 4, 3, 25)
        gladiator = Enemy("gladiator", gladiatorStats, 7, 12)
        gladiators.append(gladiator)
    response = ""
    while response not in choices:
        gladiatorTalk(p)
        response = input("The leader of the clan states: Who are you and what do you want!? (pick 1, 2, 3, or 4)").lower()
        clear()
        if(response == "1"):
            print("WHY! We pray to the dragon gods every night! You must now die! \n")
            input(" ")
            clear()
            for i in range(4):
                battle(p, gladiators[i])
            input(" ")
            clear()
            print("After defeating all the gladiators, you are confident that you can continue to inspect the path!")
            input(" ")
            clear()
        elif(response == "2"):
            print("Alright you aren't getting passed us!")
            input(" ")
            clear()
            for i in range(2):
                battle(p, gladiators[i])
            input(" ")
            clear()
            print("Nevermind feel free to pass us, you mean no harm to us!\n")
            print("Finally, some peace and quiet you can continue to inspect the path!")
            input(" ")
            clear()
        elif(response == "3"):
            print("Oh you must be octavius on the quest to kill the minotaur!\n")
            input(" ")
            clear()
            print("You spend quite some time training with the gladiators and gain skill points!")
            p.stats.sp += 3
            p.skillRaise()
            print("You thank the gladiators and go on your way to continue inspecting the path")
        elif(response == "4"):
            print("Looks like this person doesn't speak lets make em' speak")
            input(" ")
            clear()
            battle(p, gladiators[0])
            print("They killed vlad! Noooooooooooooo!")
            print("RETREAT!")
            input(" ")
            clear()
        else:
            choiceInputFail()

hawk = easyMonsters("fast", "hawk")
bat = easyMonsters("fast", "bat")
manticore = mediumMonsters("fast", "manticore")
gargoyle = easyMonsters("slow", "gargoyle")
thunderbird = easyMonsters("fast", "thunderbird")
darkfairy = easyMonsters("normal", "dark fairy")
raven = easyMonsters("normal", "raven")
vampire = mediumMonsters("normal", "vampire")
skyCreatures = [hawk, bat, manticore, gargoyle, thunderbird, darkfairy, raven, vampire]

shark = mediumMonsters("normal", "corrupted shark")
squid = easyMonsters("slow", "zombie squid")
siren = easyMonsters("normal", "siren")
octupus = easyMonsters("normal", "devil octupus")
alligator = easyMonsters("fast", "robogator")
seawitch = easyMonsters("fast", "seawitch")
seamonster = easyMonsters("slow", "sea monster")
seasnake = easyMonsters("normal", "sea snake")

riverCreatures = [shark, squid, siren, octupus, alligator, seawitch, seamonster, seasnake]

spider = easyMonsters("fast", "arachnid")
zombie = easyMonsters("slow", "zombie")
ogre = mediumMonsters("slow", "ogre")
goblin = easyMonsters("normal", "goblin")
mummy = easyMonsters("normal", "mummy")
werewolf = easyMonsters("fast", "werewolf")
spirit = easyMonsters("fast", "dark spirit")
robot = easyMonsters("normal", "robot")

forestCreatures = [spider, zombie, ogre, goblin, mummy, werewolf, spirit, robot]

clear()
name = input("Hello! What is your name, soldier\n")
playerStats = getStats(10, 30, 20, 50)
p = Player(name, playerStats)
clear()
print("Hello, " + p.name + ". You are chosen to go on this quest to slay the fire dragon!\n")
input("press enter to continue")
clear()
print("Throughout all your training, you gained these skills:\n")
print_skills()
print("These skills are going to play a roll in whether you defeat the dragon or not\n")
input(" ")
clear()
# Begin Game!
print("You leave early morning, and come across to a nearby village for food and supplies\n")
wolfStats = getStats(4, 15, 0, 20)
wolf = Enemy("wolf", wolfStats, 3, 2)
store(wolf, 5)
print("You ask one of the villagers and receive a map to the dragon's den.")
print("Looking at the map you need to first travel through the forest of darkness")
input(" ")
clear()
forest(p)

