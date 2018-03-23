import random
import sys
from observable import Observable
from observer import Observer


class room(Observable):
    def update(self, *args, **kwargs):
        pass

class NPC(Observer):

    #All NPCs have names, attacks and health scores
    def __init__(self, name, atk, health):
        self.name = name
        self.atk = atk
        self.health = health

    #Set the name of the NPC to the name
    def setName(self, name):
        self.name-name

    #Get the NPC's Name
    def getName(self):
        return self.name

    #Set the health of the NPC
    def setHealth(self, health):
        self.health=health

    #Get the health of the NPC
    def getHealth(self):
        return self.health

    #Set the attack value for the NPC
    def setAtk(self, atk):
        self.atk=atk

    #Return the attack value for the NPC
    def getAtk(self):
        return self.atk

    #The method to actually attack the player
    def attack(self, player):
        player.setHealth(player.getHealth() - self.atk)


#A Ghoul, nasty creatures. Paralytic claws, bad smell
class Ghoul(NPC):
    def __init__(self, attack, health):
        self.name = "Ghoul"
        self.attack = attack
        self.health = health

#Vampires now 30% less likely to sparkle
class Vampire(NPC):
    def __init__(self, attack, health):
        self.name = "Vampire"
        self.attack = attack
        self.health = health

#Werewolf, like a werebear but less cool
class Werewolf(NPC):
    def __init__(self, attack, health):
        self.name = "Werewolf"
        self.attack = attack
        self.health = health

#The foot soldiers of the apocalypse
class Zombie(NPC):
    def __init__(self, attack, health):
        self.name = "Zombie"
        self.attack = attack
        self.health = health

#The real monsters in this dungeon
class Human(NPC):

    def __init__(self, name, atk, health):
        self.name = "Steve" #All people are named Steve, Don't ask
        self.atk = -1 #Steve does negative 1 damage to the player
        self.health = 100 #Steve has 100 health

#All weapons have a unique name, an attack modifier and limited uses
class Weapon(object):
    name = ""
    atkMod = 1.0
    uses = 1

    #returns the name of the weapon
    def getName(self):
        return self.name

    #returns the attackmodifier of the weapon
    def getAtkMod(self):
        return self.atkMod

    #returns the number of uses left on the weapon
    def getUses(self):
        return self.uses

    #Sets the name of the weapon
    def setName(self, name):
        self.name = name

    #Sets the attack modifier of the weapon
    def setAtkMod(self, atkMod):
        self.atkMod = atkMod

    #Sets the number of uses of the weapon
    def setUses(self, uses):
        self.uses = uses

    #Reduces the number of uses by one
    def decrementUse(self):
        self.uses = self.uses - 1


#Adding a secret weapon or two into the game for the lolz
#Will be added to inventory with a cheat code
class AK47(Weapon):
    name="Ak-47"  #For When you absolutely need to kill every... -Pulp Fiction
    atkMod= 9000.1 #ATTACK IS OVER 9000!
    uses=10000000000 #Ammo is plentiful in your house?

#For those who want a more fantasy experience, same stats as the candy
#More fantastical
class BroadSword(Weapon):
    name="Sword"
    atkMod=1.0
    uses= 1000000 #How many uses does a Sword have?

#Great for Killing Zombies
class CrossBow(Weapon):
    name = "CrossBow"
    atkMod = random.uniform(1.0, 1.75)
    uses = 2 #CrossBow bolts break after two shots

#Javelins, are just short spears that you throw
class Javelin(Weapon):
    name = "Javelin"
    atkMod = random.uniform(2.0, 2.4)
    uses = 4 #Javelins shatter after 4 throws

#D&D equivalent of a molotov, kill it with fire
class AlchemistFire(Weapon):
    name = "AlchemistFire"
    atkMod = random.uniform(3.5, 5.0)
    uses = 1 #Fire bombs only work once, otherwise they aren't very good

#No story is complete without the protagonist
class Player(object):

    #Random Genetics chooses our stats...
    health = random.randint(100, 125)
    atk = random.randint(10, 20)

    inventory = [] #Inventory is for storing weapons

    def setHealth(self, health):
        self.health = health

    def getHealth(self):
        return self.health

    def setAtk(self, atk):
        self.atk = atk

    def getAtk(self):
        return self.atk

    def getInventory(self):
        return self.inventory

    inventory.append(BroadSword) #every adventurer gets a sword
    i=1
    while i<10:
        rand=random.randint(0,2) #Randomly distribute weapons
        if rand==0:
            inventory.append(CrossBow)
        elif rand==1:
            inventory.append(Javelin)
        else:
            inventory.append(AlchemistFire)

    def combat(self, monster, weapon):
        #Swords effect everyone equally
        if weapon.getName() == "Sword":
            monster.setHealth(monster.getHealth() -weapon.getAtkMod() *self.atk)
            monster.update()

            #Headshots from a crossbow hurt zombies more
        elif weapon.getName() == "CrossBow":
            if monster.getName() == "Zombie":
                monster.setHealth(monster.getHealth() -2 *(weapon.getAtkMod() *self.atk))
                monster.update()
            #The bolts aren't silver, Werewolf shrugs it off
            elif monster.getName() == "Werewolf":
                pass
            #Bolts do normal damage to the rest
            else:
                monster.setHealth(monster.getHealth() -weapon.getAtkMod() *self.atk)
                monster.update()

        elif weapon.get_name() == "Javelin":
            #Werewolves and Vampires are immune to Javelins
            if monster.getName() == "Vampire" or monster.getName() == "Werewolf":
                pass
            #The rest take normal javelin damage
            else:
                monster.setHealth(monster.getHealth() -weapon.getAtkMod() *self.atk)
                monster.update()

        elif weapon.get_name() == "AlchemistFire":
            #Ghouls are strangely flammible
            if monster.getName() == "Ghoul":
                monster.setHealth(monster.getHealth()-5 *(weapon.getAtkMod() *self.atk))
                monster.update()

            #Normal fire damage for everyone else
            else:
                monster.setHealth(monster.getHealth() -weapon.getAtkMod() *self.atk)
                monster.update()
        else:
            #AK is effective for all monsters
            monster.setHealth(monster.getHealth() -weapon.getAtkMod() *self.atk)
            monster.update()

    #Going into battle with a broken weapon is a death sentence
    def weaponCheck(self, weapon):
        if w.getUses() == 0:
            self.inventory.remove(weapon)

#Dungeons have rooms, that have monsters
class dungeon(object):

    def __init__(self, sizeX,sizeY):
        self.sizeX=sizeX
        self.sizeY=sizeY
        self.dungeonMap = [[0 for x in range(sizeX)] for y in range(sizeY)]

    def getSizeX(self):
        return self.sizeX  # Size in the x direction
    def getSizeY(self):
        return self.sizeY  # Size in the Y direction

    def getDungeonMap(self):
        return self.dungeonMap #The x,y plane

    #Fill the dungeon with monsters and rooms
    def populate(self):
        #Creates the dungeon so that it is x * y rooms
        for room in range(0, (self.sizeX * self.sizeY)):
            for x in range(0, self.sizeX):
                for y in range(0, self.sizeY):

                    room = room() #monsters are in the rooms
                    rand = random.randint(0, 10) #Random number of monsters
                    for i in range(0, rand): #Each monster is random

                        #Randomly choose a monster to spawn
                        rand = random.randint(0, 3)


                        if rand == 0: #Randomly create a Zombie
                            atk = random.randint(0, 10)
                            health = random.randint(50, 100)
                            z = Zombie(atk, health)
                            house.add_observer(z)
                            z.update()

                        if rand == 1: #Randomly create a vampire
                            atk = random.randint(10, 20)
                            health = random.randint(100, 200)
                            v = Vampire(atk, health)
                            house.add_observer(v)
                            v.update()

                        if rand == 2:#Randomly create a ghoul
                            atk = random.randint(15, 30)
                            health = random.randint(40, 80)
                            g = Ghoul(atk, health)
                            house.add_observer(g)
                            g.update()

                        if rand == 3:#Randomly create a werewolf
                            atk = random.randint(0, 40)
                            health = 200 #werewolves have constant health
                            w = Werewolf(attack,health)
                            house.add_observer(w)
                            w.update()
                    self.dungeonMap[x][y] = room

#This is the instance that makes the dungeon
class instance(object):

    def __init__(self, sizeX,sizeY):
        self.sizeX = sizeX
        self.sizeY = SizeY

        self.p = Player()
        self.d = dungeon(sizeX,SizeY)
        self.d.populate()
        self.playerXPos = 0
        self.playerYPos = 0
        temp = self.d.getDungeonMap()

         # the current position the player is in
        self.curr = temp[self.playerXPos][self.playerYPos]

    def getPlayerXPos(self):
        return self.playerXPos

    def getPlayerYPos(self):
        return self.playerYPos

    #Allows the hero to move
    def move(self, direction):
        if direction == "north":
            i = self.playerYPos
            if (i + 1) > (self.sizeY - 1): #make sure they can go that way
                print("There is a solid wall in that direction")
            else:
                self.playerYPos = self.playerYPos + 1
                temp = self.d.getDungeonMap();
                self.curr = temp[self.playerXPos][self.playerYPos]

        if direction == "south":
            i = self.playerYPos
            if (i - 1) < 0:  #make sure they can go that way
                print("There is a solid wall in that direction")
            else:
                self.playerYPos = self.playerYPos - 1
                temp = self.d.getDungeonMap();
                self.curr = temp[self.playerXPos][self.playerYPos]

        if direction == "east":
            i = self.playerXPos
            if (i + 1) > (self.sizeX - 1):  #make sure they can go that way
                print("There is a solid wall in that direction")
            else:
                self.playerXPos = self.playerXPos + 1
                temp = self.d.getDungeonMap();
                self.curr = temp[self.playerXPos][self.playerYPos]

        if direction == "west":
            i = self.playerXPos
            if (i - 1) < 0:  #make sure they can go that way
                print("There is a solid wall in that direction")
            else:
                self.playerXPos = self.playerXPos - 1
                temp = self.d.getDungeonMap();
                self.curr = temp[self.playerXPos][self.playerYPos]

    #Gotta attack monsters to kill monsters
    def slayMonster(self, monster, weapon):
        self.p.attack(monster, weapon)

    #monsters die..
    def mosterDeath(self, monster):
        self.curr.remove_observer(monster)
        h = Human()#Monster becomes a human upon death. Thats where people come from
        self.curr.add_observer(h)

    #Look at your sweet, sweet loot
    def checkInventory(self):
        for weapon in self.p.getInventory():
            print(weapon.getName(), weapon.getUses())

     #Determines if the game has been won
    def win(self, dun):
        cleared = True #Assume there are no monsters left
        for x in range(0, dun.getSizeX()):
            for y in range(0, dun.getSizeY()):
                temp = dun.dungeonMap[x][y] #Look in all the rooms
                for m in temp.observers:
                    if m.get_name() != "Steve": #All humans are Steve
                        cleared = False #Someone is not Steve...


        if cleared == True: #No room is not clear, the game is over
            return 1
        return 0  #At least one room is not clear yet

if __name__ == '__main__':

    x=input("What is the size East to West?") #set the x size of the  dungeon
    y=input("What is the size North to South?")#set the y size of the dungeon

    #start the actual game
    ins = instance(x,y)

    # intro sequence
    print("\nYour Journey begins as many other journeys end, with you coming home")
    print("\nYou just came home from the grocery store, your bags full of candy.")
    print("\nHallloween is tomorrow night, and you're all set.")
    print("\nThe candy is calling to you, you want a peice...")
    check=True #A boolean to make sure they eat the candy
    while(True):
        i=str.lower(input("Do you eat a peice of candy?"))
        if i==yes or i==y: #There is no choice
            print("A single peice isn't going to hurt anyone right?")
            check=False
        elif i==no or i==n: #Only the illusion of choice
            print("You want to say no, but who can resist candy?")
            check=False
        else:
            print("[This is a yes or no question]")
    #Candy must be eaten for this story to go anywhere
    print("\nYou eat a peice of candy, and then another and another...")
    print("\nThings get fuzzy after that point...")
    print("\nYou vaguely recognize that you are stumbling to bed for a sugar induced slumber")
    print("\n****Fade to Black****")
    print("\n")
    print("\n")
    print("\n") #Giveing the impression that time has elapsed
    print("\n")
    print("\n")
    print("\nYou begin to awaken, but this is not your room...")
    print("\nYou seem to be inside of a well lit cave system.")
    print("\nThere is a bag lying in front of you, there is a note pinned to it.")
    print("\nThe note says: \"It's dangerous to go alone, take this!\"")


    while ins.p.getHealth() > 0: #While the player isn't dead
        if ins.win(ins.d) == 1:  #If the player has won...
                print("\nAll monsters are dead, murdered in their home")
                print("\nWho is the real monster now?")
                #“Beware that, when fighting monsters,
                #you yourself do not become a monster...
                #for when you gaze long into the abyss.
                #The abyss gazes also into you.”
                #-Friedrich Nietzsche
                sys.exit(0)

        #Ask them what they want to do
        print("\nWhat do you do? (Move, Attack, Inv, Exit): ")
        command = str.lower(input()) #Ignore the case of the letters

        if command == "move":
            print("\nEnter direction to travel:")
            direction = str.lower(input())
            ins.move(direction)

            print("\nMonsters you just walked in on: ("+ str(ins.getPlayerXPos()) + ", " +str(ins.getPlayerYPos())+"): ")

            for x in ins.curr.observers:
                print(x.getName(), "%.2f" % x.getHealth())

        elif command == "attack":

            print ("\nChoose your weapon")
            weapon = str.lower(input())
            tmp = Weapon()
            hasWeapon = False
            #First we must confirm that they have the weapon
            if len(ins.curr.observers) != 0:
                for monster in ins.curr.observers:
                    for w in ins.p.inventory:
                        if weapon == w.getName():
                            hasWeapon = True
                            #Attack the monster
                            ins.slayMonster(monster,w)
                            tmp = w
                            break

                if hasWeapon== True:
                     #Then we decrease the uses left
                    tmp.decrementUse()
                    if tmp.getUses() == 0: #If the weapon is broken after use
                        ins.p.weaponCheck(tmp)

                    i = 0
                    while i < len(ins.curr.observers):
                        #Remove the dead monsters
                        if ins.curr.observers[i].getHealth() <= 0:
                            ins.mosterDeath(ins.curr.observers[i])
                            i = i - 1
                        i = i + 1

                    #Monsters turn to hurt the player
                    for NPC in ins.curr.observers:
                        NPC.attack(ins.p)

                    print("\nPlayer Health:")
                    print(ins.p.getHealth())

                    print("\nMonster Health:")
                    for x in ins.curr.observers:
                        print(x.getName(), "%.2f" % x.getHealth())


                else:
                    #You can't use a weapon you don't have
                    print("\nYou don't have that")

            else:
                #No enemies to fight
                print("\nThere are no monsters here")

        elif command == "inv" or command=="inventory":
            #Sweet, sweet loot
            print ("\nInventory:")
            ins.checkInventory()

        elif command == "exit":
            #Quitting the game....
            print("\nQuitters never win")
            sys.exit(0)

        elif command=="cheater":
            #A little cheating makes the game easy..
            print("\nYou have chosen the path of the cheater")
            print("\nA wizard appears next to you and offers you a new weapon")
            print("\nAn AK-47 is handed to you.")
            print("\nThe wizard says, \"Accept no substitutes\"")
            print("\nThe wizard poofs away. Fucking wizards, am I right?")
            ins.p.inventory.append(AK47)

        else:
            #Catch all for if the command is not one of the above
            print("\nI didn't understand you, try again")

    #Queue Dark Souls death screen...
    print("\nYou died. Game Over")
    sys.exit(0)
