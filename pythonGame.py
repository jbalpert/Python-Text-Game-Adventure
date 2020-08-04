import random 
import math
import sys
import os

escape = False
choices = ["1", "2", "3", "4"]
yes_no = ["y", "n", "Y", "N"]
directions = ["1", "2", "3"]      

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
    def print_spell(self):
        print("********************************")
        print("| Spell stats :                |")
        print("|    Name     : " + stringBuilder(self.name, 15) + "|")
        print("|    Mana     : " + stringBuilder(self.mana, 15) + "|")
        print("|    Power    : " + stringBuilder(self.power, 15) + "|")
        print("********************************")

class Weapon(Item):
    def __init__ (self, name, coins, damage, speed):
        super().__init__(name, "weapon", coins)
        self.damage = damage
        self.speed = speed
    def print_weapon(self):
        print("*******************************")
        print("| Weapon stats:                |")
        print("|    Name     : " + stringBuilder(self.name, 15) + "|")
        print("|    Damage   : " + stringBuilder(self.damage, 15) + "|")
        print("|    Speed    : " + stringBuilder(self.speed, 15) + "|")
        print("*******************************")

class Armor(Item):
    def __init__ (self, name, coins, resistance):
        super().__init__(name, "armor", coins)
        self.resistance = resistance
    def print_armor(self):
        print("**************************************")
        print("| Armour stats :                     |")
        print("|     Name     : " + stringBuilder(self.name, 20) + "|")
        print("| Resistance   : " + stringBuilder(self.resistance, 20) + "|")
        print("**************************************")

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
        self.escape = False
        self.bossesDefeated = 0

    def print_stats(self):
        print("***********************************")
        print("| Player stats  :                |")
        print("|    Name       : " + stringBuilder(self.name, 15) + "|")
        print("|    Coins      : " + stringBuilder(self.coins, 15) + "|")
        print("| Bosses Killed : " + stringBuilder(self.bossesDefeated, 15) + "|")
        print("***********************************")
        pause()
        self.weapon.print_weapon()
        pause()
        self.armor.print_armor()
        pause()
        self.spell.print_spell()
        pause()
        self.stats.print_all_stats()
        pause()

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
        num = random_num(3)
        if(num == 1):
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
            hit = math.ceil(hit)
            print("You dealt " + str(hit) + " damage to the " + enemy.name + "\n")
            enemy.stats.hp -= hit
            if(self.dexCheck()):
                self.attack(enemy)

    def castSpell(self, enemy):
        print("You chose to attack the enemy with your " + self.spell.name + "!\n")
        hit = math.ceil(self.spell.power * self.stats.int)
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
        pause()

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
            pause()
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
        pause()
    
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
        pause()
class Enemy:
    def __init__(self, name, stats, coins, experience):
        self.name = name
        self.stats = stats
        self.anger = 0
        self.coins = coins
        self.xp = experience
    
    def dexCheck(self):
        if(random_num(100) < math.floor(self.stats.dex * .1)):
            print("The enemies incredible speed allows it to strike AGAIN\n")
            return True
        else:
            return False

    def attack(self, player):
        hit = randomish_num(self.stats.str)
        if(hit == random.randint(math.floor(self.stats.str/2),self.stats.str)):
            print("Luckily, the " + self.name + " missed you!\n")
        elif(hit <= player.armor.resistance and player.armorCheck()):
            print("Your " + player.armor.name + " prevented you from taking damage from the enemy's attack\n")
        else:
            num = random_num(4)
            if(num == range(1,4)):
                hit -= player.armor.resistance
            if(hit < 1):
                hit = random_num(2)
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
    
    def print_all_stats(self):
        print("***********************************")
        print("|              Stats              |")
        print("| Strength          : " + stringBuilder(self.str, 12) + "|")
        print("| Dexterity         : " + stringBuilder(self.dex, 12) + "|")
        print("| Intelligence      : " + stringBuilder(self.int, 12) + "|")
        print("| Total Health      : " + stringBuilder(self.totalHP, 12) + "|")
        print("| Hit Points        : " + stringBuilder(self.hp, 12) + "|")
        print("| Mana              : " + stringBuilder(self.mana, 12) + "|")
        print("| Food              : " + stringBuilder(self.food, 12) + "|")
        print("| Experience        : " + stringBuilder(self.xp, 12) + "|")
        print("| Experience needed : " + stringBuilder(self.xpToLevelUp, 12) + "|")
        print("| Level             : " + stringBuilder(self.level, 12) + "|")
        print("***********************************")

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

    def toFullSaturation(self):
        self.toFullHealth()
        self.toFullHunger()
        self.toFullMana()

    def addHunger(self, amount):
        self.food += amount
        if(self.food > self.foodCap):
            self.food = self.foodCap

    def buffStats(self, percent, add=0):
        self.str = math.floor((self.str * percent) + add)
        self.dex = math.floor((self.dex * percent) + add)
        self.int = math.floor((self.int * percent) + add)
        self.totalHP = math.floor((self.totalHP * percent) + add)
        self.toFullSaturation()

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

small_hp = Potion("Small HP potion", 15, 50)
medium_hp = Potion("Medium HP potion", 35, 100)
large_hp = Potion("Large HP potion", 75, 250)
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
    return Stats(randomish_num(math.ceil(strength)), randomish_num(math.ceil(dexterity)), randomish_num(math.ceil(intelligence)), randomish_num(math.ceil(health)))

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
    print("4.) Health       = " + stringBuilder(p.stats.totalHP, 5)  + "Affects your total amount of hp")
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
    print("5. Press 5 to view your stats!")
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
                    response = input("What would you like to purchase? (Type <1, 2, 3, 4, or 5> based on the corresponding items)\n")
                    clear()
                    if(response == "1"):
                        store_buy(potions[0], potions)
                    elif(response == "2"):
                        store_buy(weapons[0], weapons)
                    elif(response == "3"):
                        store_buy(food[0], food)
                    elif(response == "4"):
                        store_buy(armor[0], armor)
                    elif(response == "5"):
                        p.print_stats()
                    else:
                        print("Please respond with 1, 2, 3, or 4 to purchase something, you're wasting electricty!\n")
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
    pause()
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
    pause()
    while(player.stats.hp > 0 and enemy.stats.hp > 0 and not player.escape):
        turn = fight(player, enemy, turn)
        printHealth(player, enemy)
        pause()
    if(player.stats.hp <= 0):
        print("You lose! Should've trained harder! THE END! \n")
        sys.exit(":(")
    elif(player.escape):
        print("You left quickly to saftey! Phew that was a close one!\n")
        enemy.stats.toFullHealth()
        enemy.coins = math.ceil(enemy_coins * .75)
        enemy.xp = math.ceil(enemy_xp * .75)
        player.escape = False
        pause()
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
    print("5. Print your statistics                              ")
    print("******************************************************\n")
    
# Runs the battle
def fight(player, enemy, turn):
    response = ""
    if(turn == player.name):
        while response not in choices:
            response = ""
            printHealth(player, enemy)
            fightMenu()
            response = input("It is your turn! (Type <1, 2, 3, 4, or 5> based on the corresponding options to fight!)\n")
            clear()
            if(response == "1"):
                player.attack(enemy)
            elif(response == "2" and player.stats.mana >= player.spell.mana):
                player.castSpell(enemy)
            elif(response == "3"):
                player.rest()
            elif(response == "4"):
                if(player.retreat()):
                    player.escape = True
            elif(response == "5"):
                player.print_stats()
            else:
                print("You need to respond with 1, 2, 3, or 4 or you don't have enough mana to cast the spell!\n")
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
    continueQuest = True
    response = ""
    print("You come across a dense forest with towering trees, you have a bad feeling about this.")
    print("Despite your concerns, you are a warrior and continue and enter the forest")
    print("Cutting through vines with your "  + p.weapon.name + " you see a path in the distance")
    while response not in yes_no:
        response = input("Do you want to investigate the path? (Y/N)\n").lower()
        clear()
        if(response == 'y'):
            investFpath(p)
        elif(response == 'n'):
            navigateF(p)
        else:
            yesnoInputFail()
        if(p.bossesDefeated >= 2):
            while response not in yes_no:
                response = input("would you like to continue your quest (Y) or go back to the forest (N) (Y/N) \n warning you must complete another boss to come back to this message \n").lower()
                if(response == 'y'):
                    pass
                elif(response == 'n'):
                    continueQuest = False
                else:
                    yesnoInputFail()
        elif(not (p.bossesDefeated >= 2) and response in yes_no):
            print("You got so confused navigating the land that you came back to the same first path!")
            print("Defeat two bosses to find the next piece of the map!\n")
        if(not continueQuest):
            response = ""



        elif(response in yes_no):
            print("You got so confused navigating the land that you came back to the same first path!")
            print("Defeat two bosses to find the next piece of the map!\n")

def labyrinth(p):
    print("You come out of the forest more confident than ever knowing that you defeated very powerful bosses\n")
    print("However, you know that there will be tougher challenges in the future!\n")
    pause()
    print("You find yourself in the village of siawathi where there are no enemies and you can finally take a break\n")
    print("You meet some folks, grab a few drinks and feast. The people display excellent hospitality.\n")
    pause()
    print("After a couple of nights in the village, healing wounds and scars from monsters, you feel well rested to continue!\n")
    print("You regain all your hunger, health, and mana throughout these nights.\n")
    p.print_stats()

def easyMonsters(version, name, coins = 25, xp = 25):
    stats = ""
    if(version == "fast"):
        stats = getStats(3, 200, 20, 20)
    elif(version == "normal"):
        stats = getStats(5,10,20,30)
    elif(version == "slow"):
        stats = getStats(10, 2, 2, 40)
    elif(version == "boss"):
        stats = getStats(12, 15, 15, 150)
        coins *= 4
        xp *= 4
    return Enemy(name, stats, coins, xp)

def mediumMonsters(version, name, coins = 75, xp = 75):
    stats = ""
    if(version == "fast"):
        stats = getStats(12, 333, 20, 35)
    elif(version == "normal"):
        stats = getStats(14,40,40,70)
    elif(version == "slow"):
        stats = getStats(20, 10, 10, 130)
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

def displayPaths(zone):
    print("1. Go to the " + zone + " shop! ")
    print("2. Go explore the " + zone + " dungeon")
    print("3. Keep searching to the left")
    print("4. Keep searching to the right \n")

zoneText = {
    "sky" : "You reach the top of the tree and find that you can magically walk on the clouds\n These clouds have a bit of a bounce to it as you hop forward\nThrough the mist, you can see a cloud shop and what looks to be a dungeon in the distance!\n",
    "river" : "You reach the a giant flowing river and can are debating whether you should cross it\nYou keep walking toward it step by step\nYou realize that this river has some monsters nearby!\n",
    "forest" : "It is incredibly difficult to see the forest as you try to navigate in utter darkness\n You see a small glimpse of light in the distance\n"
}

def preDungeon(zone):
    if(zone == "sky"):
        print("You start heading to the dungeon, when you come across a happy little cloud child")
        print("She sneezes a small puff of cloud as you pass them")
        pause()
        print("You smile at the kid, and start walking past them, but the entire cloud you are on turns grey")
        print("The child takes the form of a demon witch and flies above you looking down upon you")
        print("YoU thInk YoU aRE goInG in My dOmaIN yOunG tRaveLer? I thInK NOT!")
        print("The witch spawned many monsters to try and stop you from entering the dungeon")
        pause()
        for i in range(random_num(4)):
            monster = getRandomMonster(skyCreatures)
            print("The witch's " + monster.name + " comes to battle you!\n" )
            battle(p, monster)
        print("Wow I can't believe that witch spawned all those creatures on me!")
        print("HEHEHEHEHEEEEEEEE you coward face me peasant in my dungeon if you want to kill me!")
        pause()
        response = ""
    elif(zone == "river"):
        print("Two dungeon guards stand before you armed with tridents\n")
        print("They instantly read your mind and know that you seek to slay the king drgaon\n")
        print("You shall not pass!\n")
        pause()
        for i in range(2):
            battle(p,mediumMonsters("fast", "river guard", 45, 45))
        print("You have won, but you won't last in the dungeon!\n")
        pause()
    elif(zone == "forest"):
        centaur = hardMonsters("slow", "king centaur")
        print("You find a centaur that seems to be peaceful sharpening his axe\n")
        print("You walk over to the centaur and find that he is alone.")
        pause()
        print("The centaur notices you and grips his axe waiting for you to make a move\n")
        response = ""
        while response not in yes_no:
            response = input("Do you fight the centaur? (Y/N) \n").lower()
            clear()
            if(response == "y"):
                print("You start rushing towards the centaur, you see that this opponent is not just any centaur,\n")
                print("They are the king of centaurs\n")
                pause()
                battle(p, centaur)
            elif(response == "n"):
                print("You decide to be friendly towards the centaur\n")
                talkCentaur(p)
            else:
                yesnoInputFail()
            print("You find yourself walking to the dungeon and hope to survive its horrible monsters\n")
            pause()
def talkCentaur(p):
    response = ""
    while response not in yes_no:
        response = input("Do you talk to the centaur? (Y/N) \n").lower()
        clear()
        if(response == "y"):
            print("You reach into your backpack and grab some leftover steak bits and offer the centaur the food\n")
            print("Centaur: A young traveler on a journey to slay thy dragon \n")
            print("very noble indeed, when I once was your age, I thought to bringth honor to my family\n")
            print("I slayed the demon warrior a few years past\n")
            pause()
            print("The centaur grabbed the food and thanked you\n")
            print("How do you know why I am here?\n")
            pause()
            print("Centaur: I am glenciotus the king of the centaurs, I know all who is living\n")
            print("I am here in this forest because there is evil that lurks throughout this place")
            print("This forest needs to be restored to what it once was...\n")
            pause()
            print("How can I help you restore the life within the forest?\n")
            pause()
            print("The forest lord has been corrupted by evil demons spawned by the dragon")
            print("If you can heal the forest lord, you will save the forest!")
            pause()
            print("Where is the forest lord?\n")
            print("The centaur used magic to light a path that leaded to a dark dungeon surrounded by dark vines and dead overgrown plants")
            pause()
            print("Go at once, and take this necklace it will provide you with magic powers")
            print("You put on the necklace and receive +7 intelligence")
            p.stats.int += 7
        elif(response == "n"):
            print("You avoid the centaur not sure if they are evil or not\n")
            print("You hear rustling in the bushes and you get knocked out cold\n")
            pause()
            print("You wake up and you see 3 monsters carrying you to what looks to be a dungeon\n")
            print("You hit one of their arms and go into battle\n")
            for i in range(3):
                battle(p, getRandomMonster(forestCreatures))
        else:
            yesnoInputFail()

def directionsMenu():
    print("You enter the a room to see three other doors")
    print("Door 1: Left door")    
    print("Door 2: Center door")
    print("Door 3: Right door")

def dungeon(p, zone, roomNum, monsterArr, level, boss):
    print("You have reached the " + zone + " dungeon! Good Luck Warrior!\n")
    left = True
    right = True
    isOpen = True
    for i in range(roomNum):
        response = ""
        while response not in directions:
            directionsMenu()
            response = input("Please pick a door (1, 2, 3)\n")
            clear()
            if response in directions:
                if(response == "1" and left):
                    right = False
                    isOpen = True
                    direction = "left"
                elif(response == "2"):
                    isOpen = True
                    right = True
                    left = True
                    direction = "center"
                elif(response == "3" and right):
                    left = False
                    isOpen = True
                    direction = "right"
                elif((response == "1" and not left) or (response == "3" and not right)):
                    isOpen = False
                    print("You were already in that room and it is now locked!\n")
                else:
                    isOpen = False
                    print("Please pick a door please!!! (1, 2, 3)")
                if(isOpen):
                    dungeonFate(p, direction, monsterArr, boss, level)
    print("You have made it far through the dungeon and feel the earth shaking \n")
    print("You see the dungeon boss in the distance. The " + boss.name + "!\n")
    pause()
    print("HAHAHA you think you can defeat me!? You and what army!\n")
    print("You run into battle and fight it\n")
    battle(p, boss)
    p.bossesDefeated +=1
    print("Phew, you were no match for me! For I am " + p.name + "!\n")
    print("You find a many treasure chests to loot!")
    if(level > 1.4):
        for i in range(3):
            loot_l(p, level)
        loot_m(p, level)
    elif(level > 1.2):
        for i in range(3):
            loot_m(p, level)
        loot_s(p, level)
    else:
        for i in range(3):
            loot_s(p, level)
        loot_m(p, level)
        print("You exited the dungeon content with the loot you recieved\n")

def dungeonFate(p, direction, monsterArr, boss, level=1):
    print("You chose to go through the " + direction + " door!\n")
    pause()
    response = ""
    chance = random_num(50)
    if(chance == 1):
        print("You find a hidden dungeon shop beneath by triggering a hidden pressure plate\n")
        store(getRandomMonster(monsterArr), 100)
    elif(chance in range (2,4) or chance == 24):
        monster = getRandomMonster(monsterArr)
        print("You get attacked by a " + monster.name + "!\n")
        pause()
        battle(p, monster)
        print("You received a wand to teleport you back to the village shop and go back to the shop\n")
        pause()
        store(wolf, 5)
        print("The wand fizzles out as you return back to the dungeon\n")
        pause()
    elif(chance in range(4,6)):
        monster = getRandomMonster(monsterArr)
        choice = ""
        ogre = ""
        while choice not in yes_no:
            choice = input("A " + monster.name + " demands that you pay 10 coins to him (Y/N) \n").lower()
            if(choice == 'y'):
                if(p.coins >= 10):
                    p.coins -= 10
                else:
                    ogre = "mad"
            elif(choice == 'n'):
                ogre = "mad"
            else:
                yesnoInputFail()
        if(ogre == "mad"):
            print("The " + monster.name + " lets out an ear piercing scream and starts charging at you!\n")
            pause()
            battle(p, monster)
    elif(chance == 8):
        choice = ""
        human = ""
        while choice not in yes_no:
            choice = input("An injured human asks that you give food to him (Y/N) \n").lower()
            if(choice == 'y'):
                if(p.stats.food >= 5):
                    p.stats.food -= 5
                    human = "happy"
                else:
                    print("You don't have enough food for the human.\n")
            elif(choice == 'n'):
                pass
            else:
                yesnoInputFail()
        if(human == "happy"):
            print("The human gives you a health potion that you happily drink!\n")
            p.stats.addHealth(50)
            print("You gained 50 health points from the potion")
    elif(chance == 9):
        choice = ""
        devil = ""
        while choice not in yes_no:
            choice = input("A devil spirit asks you to try and cast him a dark spell (Y/N) \n").lower()
            if(choice == 'y'):
                if(p.stats.int > 45):
                    print("You start casting the dark spell, and the devil spirit starts laughing hard\n")
                    pause()
                    print("You take in your surroundings and a green cloud of fart fills the room\n")
                    devil = "happy"
                else:
                    print("You attempt to cast the spell, but you are not experienced enough in the art of wizardry\n")
                    print("Although the devil looks disappointed, the devil lets you pass")
                pause()
            elif(choice == 'n'):
                print("The devil looks extremely disappointed in you and takes out his blade to fight!")
                devil = "mad"
            else:
                yesnoInputFail()

        if(devil == "happy"):
            print("HAHAHAHA I pranked youuuuuuu (the devil laughs sooo hard) for your troubles, I'll give you a mystic ring\n")
            while choice not in yes_no:
                choice = input("Do you take the ring? (Y/N) \n").lower()
                if(choice == 'y'):
                    print("You put the ring on, and you instantly feel stronger, you gain 2 strength!\n")
                    p.stats.str += 2
                else:
                    print("You decide not to take the ring, probably a smart idea since it came from a devil\n")            
        elif(devil == "mad"):
            print("You hurt my feelings, now you must DIE!\n")
            pause()
            battle(p, mediumMonsters("fast", "mysterious devil"))
    elif(chance == 10 or chance == 11):
        choice = ""
        print("You are extremely lucky!\n")
        while choice not in yes_no:
            choice = input("You find a chest in the middle of the room. Do you open it? (Y/N) \n").lower()
            if(choice == 'y'): 
                coins = random_num(30)
                p.coins += coins
                print("You gained " + str(coins) + " coins from that chest")
            elif(choice == 'n'):
                print("You decide not to open the chest and continue the mission\n")
            else:
                yesnoInputFail()
    elif(chance in range(12,18)):
        choice = ""
        monsters = []
        for i in range(4):
            monsters.append(getRandomMonster(monsterArr))
        print("You see a group of monsters in this room and don't know what to do!\n")
        print("You cast a spell that turns you invisible for 1 minute, but that's not enough time for you to get past them unnoticed\n")
        print("Specifically, you see a giant " + monsters[0].name + ", fast " + monsters[1].name + ", an angry " + monsters[2].name + ", and a fierce " + monsters[3].name + " in the room")
        pause()
        fight = True
        while choice not in choices:
            print("1.) Surprise attack them with your " + p.weapon.name + "!")
            print("2.) Lure them away by throwing some of your food in a corner")
            print("3.) Attempt to sneak past them")
            print("4.) Transform yourself into a phoenix to fight (Uses the rest of your mana)")
            choice = input("Select an option (1, 2, 3, or 4)\n")
            if(choice == '1'): 
                for i in range(4):
                    p.attack(monsters[i])
            elif(choice == '2'):
                if(p.stats.food >= 10):
                    print("You throw 10 pieces of your food and lure away the enemies and make a dash for the next room\n")
                    p.stats.food -= 10
                    fight = False
                    print("You luckily escaped!")        
                else:
                    print("You reach into your bag, realizing that you don't have enough food. The monster's hear you loud and clear and move to attack you\n")
            elif(choice == '3'):
                if(random_num(100) < math.floor((p.stats.dex) * .5)):
                    print("You successfully sneaked past the enemies!")
                    fight = False
                else:
                    print("You tripped on a rock and see the monsters sprint towards you\n")
            elif(choice == '4'):
                if(p.stats.int > 35 and p.stats.mana > 10):
                    print("You sway your hands and use the remaining power you have to transform into a minion\n")
                    playerStats = ""
                    if(p.stats.mana > 100):
                        playerStats = getStats(50, 700, 85, 355)
                        p.stats.mana = 0
                    elif(p.stats.mana > 50):
                        playerStats = getStats(25, 600, 50, 205)
                    else:
                        playerStats = getStats(15, 500, 30, 105)
                    minion = Player("Phoenix", playerStats)
                    for i in range(4):
                        battle(minion, monsters[i])
                    fight = False
                else:
                    print("You did not have enough mana or intelligence to cast the spell\n")
                    choice = ""
            else:
                choiceInputFail()   
        if(fight):
            for i in range(4):
                battle(p, monsters[i])
        else:
            loot_m(p, level)
    elif(chance == 18):
        print("You step into a snake trap! You lose 10 health!\n")
        p.stats.hp -= 10
        if(p.stats.hp <= 0):
            print("You lose! Should've trained harder! THE END! \n")
            sys.exit(":(")
    elif(chance == 19):
        choice = ""
        while choice not in yes_no:
            choice = input("You find a chest in the middle of the room. Do you open it? (Y/N) \n").lower()
            if(choice == 'y'): 
                loot_s(p, level)
            elif(choice == 'n'):
                print("You decide not to open the chest and continue the mission\n")
            else:
                yesnoInputFail()
    elif(chance in range(20,24)):
        print("A young goblin shouts: leTs plAy a GameE")
        print("If yOU guEss mY nuMbeR yoU wIn iF nOt, I wilL gEt mY FaMiLy to KILL YOU")
        value = guess_number()
        if(value):
            coins = randomish_num(24)
            p.coins += coins
            print("You gained " + str(coins) + " coins from the goblin")
        else:
            for i in range(5):
                battle(p, goblin)
                goblin.stats.buffStats(1.1)
    elif(chance == 25):
        choice = ""
        while choice not in yes_no:
            chance = random_num(100)
            choice = input("You find a shawarma on a table in an ugly room. Do you eat it? (Y/N) \n").lower()
            if(choice == 'y'): 
                if(chance >= 80):
                    print("mmmmmmm yummy! That tasted so good! You gained 15 hunger points \n")
                    p.stats.addHunger(15)
                else:
                    print("ewww that was disgusting. The food you ate was 4 years old. You lose all your hunger points and are starving\n")
                    p.stats.food = 0
            elif(choice == 'n'):
                print("You decide not to eat the shawarma and continue the mission\n")
            else:
                yesnoInputFail()
    elif(chance == 26):
        choice = ""
        while choice not in yes_no:
            chance = random_num(100)
            choice = input("You walk into a room with many book shelves do you want to read? (Y/N) \n").lower()
            if(choice == 'y'): 
                if(chance >= 50):
                    print("You read a book on wizardry and gain + 3 intelligence\n")
                    p.stats.int += 3
                else:
                    monster = getRandomMonster(monsterArr)
                    print("You start reading a book and fall asleep in boredom\n")
                    pause()
                    print("You wake up with a mad " + monster.name + " right beside you. Still sleepily you go into battle\n")
                    print("Because you are sleepy, the monster is faster than it usually is\n")
                    monster.stats.dex += 150
                    battle(p, monster)
            elif(choice == 'n'):
                print("You decide not to read and continue the mission\n")
            else:
                yesnoInputFail()
    elif(chance == 27 or chance == 28):
        choice = ""
        while choice not in yes_no:
            chance = random_num(100)
            choice = input("You find an old man sitting at a table with a coin. Do you want to gamble with him? (Y/N) \n").lower()
            if(choice == 'y' and p.coins > 20): 
                if(chance >= 80):
                    print("The old man was a liar and stole 10 coins from you \n")
                    p.coins -= 10
                else:
                    outcome = "heads"
                    chance = random_num(100)
                    print("The old man states if I flip my coin and it lands on heads I win 10 coins, if it lands on tails you win\n")
                    pause()
                    if(chance >= 60):
                        outcome = "tails"
                    print("The coin launches from the nice old man's thumb and it lands on " + outcome + "!" )
                    if(outcome == "tails"):
                        print("You won 10 coins!")
                        p.coins += 10
                    else:
                        print("You lost 10 coins")
                        p.coins -= 10
                    choice = input("Care to play again? Y for yes or type anything for no").lower() 
                    if(choice == 'y'):
                        choice == ""
                    else:
                        choice = "n"                   
            elif(choice == 'n' or p.coins < 20):
                print("You decide not to gamble and continue the mission\n")
            else:
                yesnoInputFail()
    elif(chance == 29):
        choice = ""
        while choice not in yes_no:
            chance = random_num(100)
            choice = input("You find a shawarma on a table in an ugly room. Do you eat it? (Y/N) \n").lower()
            if(choice == 'y'): 
                if(chance >= 80):
                    print("mmmmmmm yummy! That tasted so good! You gained 15 hunger points \n")
                    p.stats.addHunger(15)
                else:
                    print("ewww that was disgusting. The food you ate was 4 years old. You lose all your hunger points and are starving\n")
                    p.stats.food = 0
            elif(choice == 'n'):
                print("You decide not to eat the shawarma and continue the mission\n")
            else:
                yesnoInputFail()
    elif(chance in [31, 32, 33, 34, 35, 36]):
        monster = getRandomMonster(monsterArr)
        print("You get attacked by a " + monster.name + "!\n")
        pause()
        battle(p, monster)
        print("You find a treasure chest and find that there are 20 coins inside!")
        p.coins += (20*level)
    else:
        monster = getRandomMonster(monsterArr)
        monster2 = getRandomMonster(monsterArr)
        print("You get attacked by a " + monster.name + "!\n")
        pause()
        battle(p, monster) 
        print("You get attacked again by the monsters friend, a " + monster2.name + "!\n")
        pause()
        battle(p, monster2)
        print("You find a chest and see what is inside")
        loot_s(p, level)
    pause()

def guess_number():
    guess = ""
    numberOfGuesses = 0
    guessesLeft = 8
    number = random_num(50)
    print("The NUmBer iS FRom 1 to 50 GooooooD lucK\n")
    while numberOfGuesses < 8:
        guess = ""
        while guess not in range(1,51):
            guess = input("GuESs aWayyy\n")
            if(guess.isdigit()):
                guess = int(guess)
            if(guess not in range(1,51)):
                print("You need to type a number between 1 and 50!")
            else:
                numberOfGuesses += 1
                guessesLeft = 8 - numberOfGuesses
                if(guess < number):
                    print("YoUR gUeSS is too LoW! You HaVE " + str(guessesLeft) + " left")
                elif(guess > number):
                    print("YoUR gUeSS is too HiGH! You HaVE " + str(guessesLeft) + " left")
                else:
                    print("WhAT HoW dID yOu GuesS my NumbER?\n")
                    print("The demon exploded into a million pieces\n")
                    return True
    print("AHAHAHAH you FaILEd noW tiMe FoR yOU to DIE!")
    return False
def loot_s(p, level):
    print("You find a small loot chest and decide to see what is inside it!\n")
    pause()
    num = random_num(10)
    if(num in range(1,8)):
        coins = math.ceil(15 * level)
        p.coins += coins
        print("You found " + str(coins) + " in the chest! You now have " + str(p.coins) + " coins\n")
    elif(num == 9):
        print("Oh no! The chest was a decoy! The chest attacks you!")
        mimic = Enemy("level " + str(level) + " mimic", getStats(6*level, 25*level, 5*level, 20*level), 10, 10)
        battle(p, mimic)
    else:
        print("Unfortunate, there is nothing, but cobwebs inside")
    pause()

def loot_m(p, level):
    print("You find a medium loot chest and decide to see what is inside it!\n")
    pause()
    num = random_num(6)
    if(num in range(1,3)):
        coins = math.ceil(40 * level)
        p.coins += coins
        print("You found " + str(coins) + " in the chest! You now have " + str(p.coins) + " coins\n")
    elif(num == 3):
        print("Oh no! The chest was a decoy! The chest attacks you!")
        mimic = Enemy("level " + str(level) + " mimic", getStats(9*level, 30*level, 10*level, 35*level))
        battle(p, mimic)
    elif(num == 4):
        print("You see a clear pink potion and decide to drink it. The potion restored all your hunger, health, and mana!\n")
        p.stats.toFullSaturation()
    elif(num == 5):
        print("You see a clear purple potion and decide to drink it. The potion grants you 2 skill points!\n")
        p.stats.sp += 2
        p.skillRaise()
    else:
        print("You find an interesting ancient scroll, you translate and read the scroll out loud...\n")
        pause()
        print("Suddenly, you see an aura form around you.\n Not only did you regain all your missing health, but you now have a forcefield that allows you to withstand 50 hp of damage before getting hurt\n")
        p.stats.toFullHealth()
        p.stats.hp += 50
    pause()

def loot_l(p, level):
    print("You find a large loot chest and decide to see what is inside it!\n")
    pause()
    num = random_num(20)
    if(num in range(1, 10)):
        coins = math.ceil(75 * level)
        p.coins += coins
        print("You found " + str(coins) + " in the chest! You now have " + str(p.coins) + " coins\n")
    elif(num ==  10):
        print("Oh no! The chest was a decoy! The chest attacks you!")
        mimic = Enemy("level " + str(level) + " mimic", getStats(12*level, 35*level, 15*level, 50*level))
        battle(p, mimic)
    elif(num in range(11,13)):
        print("You find an interesting ancient scroll, you translate and read the scroll out loud...\n")
        pause()
        print("Suddenly, you see an aura form around you.\n Not only did you regain all your missing health, but you now have a forcefield that allows you to withstand 150 hp of damage before getting hurt\n")
        p.stats.toFullHealth()
        p.stats.hp += 150
    elif(num in range(13,16)):
        print("You see a clear purple potion and decide to drink it. The potion grants you 5 skill points!\n")
        p.stats.sp += 5
        p.skillRaise()
    elif(num in range(16,18)):
        print("You pick up a glowing red orb, you wonder what this orb does\n")
        pause()
        print("Your " + p.weapon.name + " starts glowing! The orb is a weapon enchanter!")
        upgrade = random_num(2)
        if(upgrade == 1):
            points = randomish_num(12)
            print("Your weapon gains " + str(points) + " speed points!\n")   
            p.weapon.speed += points
        else:
            points = randomish_num(8)
            print("Your weapon gains " + str(points) + " damage points!\n")   
            p.weapon.damage += points
    elif(num in range(18,20)):
        print("You pick up a glowing blue orb, you wonder what this orb does\n")
        pause()
        print("Your " + p.armor.name + " starts glowing! The orb is an armor enchanter!")
        points = randomish_num(8)
        print("Your armor gains " + str(points) + " resistance points!\n")   
        p.armor.resistance += points
        p.stats.totalHP += points
        p.stats.hp += points
    else:
        print("You found an infinity stone, you feel power surge into your skin as you grasp it\n")
        print("Previous stats:\n")
        print_skills()
        p.stats.buffStats(1.5)
        print("Current stats:\n")
        print_skills()
    pause()

def getZone(p, zone, zoneText, monsterArr, boss):
    print(zoneText[zone])
    pause()
    response = ""
    while response not in choices:
        displayPaths(zone)
        response = input("Select a path to choose (1, 2, 3, or 4)\n")
        clear()
        if(response == "1"):
            monster = getRandomMonster(monsterArr)
            print("You start heading towards the shop, when suddenly a " + monster.name + " attacks you!")
            battle(p,monster)
            print("Thankfully, you survived that attack and go into the shop")
            store(getRandomMonster(monsterArr), 15)
            response = ""
        elif(response == "2"):
            preDungeon(zone)
            dungeon(p, zone, randomish_num(8), monsterArr, 1, boss)
        elif(response == "3"):
            response = chanceFate(p, monsterArr)
        elif(response == "4"):
            response = chanceFate(p, monsterArr)
        else:
            choiceInputFail()

def chanceFate(p, monsterArr):
    print("You decide to explore!\n")
    input(" ")
    response = ""
    chance = random_num(15)
    if(chance in [1,2,3,4,5,6]):
        monster = getRandomMonster(monsterArr)
        print("You get attacked by a " + monster.name + "!\n")
        pause()
        battle(p, monster)
    elif(chance == 7 or chance == 8):
        if(p.coins < 5):
            print("Nothing seems too interesting over here!")
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
    elif(chance in [11,12,13,14,15]):
        monster = getRandomMonster(monsterArr)
        monster2 = getRandomMonster(monsterArr)
        print("You get attacked by a " + monster.name + "!\n")
        pause()
        battle(p, monster) 
        print("You get attacked again by the monsters friend, a " + monster2.name + "!\n")
        pause()
        battle(p, monster2)
        print("You find a treasure chest and find that there are 20 coins inside!")
        p.coins += 20
    else:
        print("You explore the surroundings and find 15 gold coins!\n")
        p.coins += 15
    return response

def navigateF(p):
    goblinStats = getStats(4, 350, 1, 30)
    goblin = Enemy("goblin", goblinStats, 6, 10)
    print("You see a many possible ways to travel")
    response = ""
    while response not in choices:
        forestPaths()
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
                    pause()
                    battle(p, monster)
                else:
                    yesnoInputFail()
                getZone(p, "sky", zoneText, skyCreatures, skyboss)
        elif(response == "2"):
            getZone(p, "river", zoneText, riverCreatures, riverboss)
        elif(response == "3"):
            getZone(p, "forest", zoneText, forestCreatures, forestlord)
        elif(response == "4"):
            response = chanceFate(p, forestCreatures)
        else:
            choiceInputFail()

def forestPaths():
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
            pause()
            goblins = []
            for i in range(3):
                goblinStats = getStats(4, 350, 1, 30)
                goblin = Enemy("goblin", goblinStats, 6, 10)
                battle(p, goblin)
                if(i == 0):
                    print("The second goblin jumps and attacks you with its claws")
                elif(i == 1):
                    print("The last goblin jumps right into battle!")
            print("After you kill the goblins, you quickly go to examine the path")
        elif(response == 'n'):
            print("You don't seem to alarmed by the rustling and continue to examine the pathway")
            print("Noticing footprints and what looks to be chariot tracks, realize that people are close")
            pause()
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
        response = input("The leader of the clan states: Who are you and what do you want!? (pick 1, 2, 3, or 4)\n").lower()
        clear()
        if(response == "1"):
            print("WHY! We pray to the dragon gods every night! You must now die! \n")
            pause()
            for i in range(4):
                battle(p, gladiators[i])
            pause()
            print("After defeating all the gladiators, you are confident that you can continue to inspect the path!")
            pause()
        elif(response == "2"):
            print("Alright you aren't getting passed us!")
            pause()
            for i in range(2):
                battle(p, gladiators[i])
            pause()
            print("Nevermind feel free to pass us, you mean no harm to us!\n")
            print("Finally, some peace and quiet you can continue to inspect the path!")
            pause()
        elif(response == "3"):
            print("Oh you must be octavius on the quest to kill the minotaur!\n")
            pause()
            print("You spend quite some time training with the gladiators and gain skill points!")
            p.stats.sp += 2
            p.skillRaise()
            print("You thank the gladiators and go on your way to continue inspecting the path")
        elif(response == "4"):
            print("Looks like this person doesn't speak lets make em' speak")
            pause()
            battle(p, gladiators[0])
            print("They killed vlad! Noooooooooooooo!")
            print("RETREAT!")
            pause()
        else:
            choiceInputFail()

def pause():
    input(" ")
    clear()

skyboss = easyMonsters("boss", "hydra")

hawk = easyMonsters("fast", "hawk")
bat = easyMonsters("fast", "bat")
manticore = mediumMonsters("fast", "manticore")
gargoyle = easyMonsters("slow", "gargoyle")
thunderbird = easyMonsters("fast", "thunderbird")
darkfairy = easyMonsters("normal", "dark fairy")
raven = easyMonsters("normal", "raven")
vampire = mediumMonsters("normal", "vampire")
skyCreatures = [hawk, bat, manticore, gargoyle, thunderbird, darkfairy, raven, vampire]

riverboss = easyMonsters("boss", "robo andaconda")

shark = mediumMonsters("normal", "corrupted shark")
squid = easyMonsters("slow", "zombie squid")
siren = easyMonsters("normal", "siren")
octupus = easyMonsters("normal", "devil octupus")
alligator = easyMonsters("fast", "robogator")
seawitch = easyMonsters("fast", "seawitch")
seamonster = easyMonsters("slow", "sea monster")
seasnake = easyMonsters("normal", "sea snake")

riverCreatures = [shark, squid, siren, octupus, alligator, seawitch, seamonster, seasnake]

forestlord = easyMonsters("boss", "forest lord")

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
playerStats = getStats(15, 30, 25, 50)
p = Player(name, playerStats)
print("Hello, " + p.name + ". You are chosen to go on this quest to slay the fire dragon!\n")
input("press enter to continue")
clear()
print("Throughout all your training, you gained these skills:\n")
print_skills()
print("These skills are going to play a roll in whether you defeat the dragon or not\n")
pause()
# Begin Game!
print("You leave early morning, and come across to a nearby village for food and supplies\n")
wolfStats = getStats(4, 15, 0, 20)
wolf = Enemy("wolf", wolfStats, 8, 8)
store(wolf, 5)
print("You ask one of the villagers and receive piece of a map to the dragon's den.")
print("Looking at the map you need to first travel through the forest of darkness")
pause()
forest(p)
labyrinth(p)

