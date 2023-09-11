# Imports ----------------------------------------------------------------------------------

import random
import time
import os


# Variables ----------------------------------------------------------------------------------

running = True
inbunker = True
onjourney = False
generator = False
waterfilter = False
rain = False
startgame = True
saveinfo = '  '
completiondistance = 500
locx = 1
locy = 1
sick = 0
distance = 11
enemydistance = 0
health = 100
water = 100
foodnum = 100
day = 0
journeydays = 0
actions = 3
y = 0
location = 0
fooditems = []
startitems = random.randint(5, 9)
gardenbook = 0
waterbook = 0
genbook = 0
boatbook = 0
gunbook = 0
items = []
worldmap = [['+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+'],
            ['| ','■ ','| ','  ','| ','  ','| ','  ','| ','  ','| ','  ','| ','  ','| ','  ','| ','  ','| ','  ','| '],
            ['+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+'],
            ['| ','  ','| ','  ','| ','  ','| ','  ','| ','  ','| ','  ','| ','  ','| ','  ','| ','  ','| ','n ','| '],
            ['+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+'],
            ['| ','  ','| ','  ','| ','  ','| ','n ','| ','n ','| ','n ','| ','  ','| ','  ','| ','○ ','| ','  ','| '],
            ['+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+'],
            ['| ','  ','| ','n ','| ','  ','| ','  ','| ','  ','| ','  ','| ','n ','| ','  ','| ','  ','| ','○ ','| '],
            ['+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+'],
            ['| ','  ','| ','  ','| ','n ','| ','n ','| ','  ','| ','  ','| ','  ','| ','  ','| ','n ','| ','  ','| '],
            ['+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+'],
            ['| ','  ','| ','  ','| ','  ','| ','○ ','| ','  ','| ','  ','| ','  ','| ','  ','| ','  ','| ','  ','| '],
            ['+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+'],
            ['| ','  ','| ','  ','| ','  ','| ','  ','| ','  ','| ','  ','| ','  ','| ','  ','| ','○ ','| ','  ','| '],
            ['+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+=','==','+']]


# Classes ----------------------------------------------------------------------------------

class food:
        
    def __init__(self, quality, type, foodinc, healthinc, waterinc):
        self.quality = quality
        self.type = type
        self.foodinc = foodinc
        self.waterinc = waterinc
        self.healthinc = healthinc

    def __str__(self):
        return self.type
    
class item:
        
    def __init__(self, uses, type, damage):
        self.uses = uses
        self.type = type
        self.damage = damage
        
    def __str__(self):
        return self.type
    
    def usefulness(self):
        return self.uses



# Functions ----------------------------------------------------------------------------------

def attack(name, damage, attackstring):
    global cont, y, infight, health, dmg, onjourney, inbunker
    enemyhealth = 100
    infight = True
    while infight:
        clearscreen()
        print('--------------------------FIGHT--------------------------')
        print(f'You stand in front of {name}, readying to attack.')
        print(f'You have {health}/100 health and they have {enemyhealth}/100 health.')
        print(f'You look for something in your inventory to attack with.')
        print('or you could use your fists.')
        print('A: Use fists')
        print('B: Use Item')
        print('C: Eat')
        print('D: Flee')
        print('------------------SELECT ONE TO CONTINUE-----------------')
        cont = input('').lower()
        dmg = random.randint(10,25)
        if cont == 'a':
            enemyhealth = int(enemyhealth) - dmg
            clearscreen()
            print('--------------------------FIGHT--------------------------')
            print(f'You punch {name} as hard as you can, dealing {dmg} damage')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            cont == input('').upper()
            clearscreen()
        elif cont == 'b':
            clearscreen()
            print('-------------------Your Item Inventory-------------------')
            for obj in items:
                print(obj)
            print('----------------TYPE WHAT YOU WANT TO USE----------------')
            cont = input('').lower()
            clearscreen()
            for x in range(0, int(len(items))):
                y = items[x].type
                if y == cont:
                    enemyhealth = int(enemyhealth) - int(items[x].damage)
                    clearscreen()
                    print('--------------------------FIGHT--------------------------')
                    print(f'You {items[x].uses} {name}. ')
                    print(f'Enemy -{items[x].damage} damage!')
                    print('-----------------PRESS ENTER TO CONTINUE-----------------')
                    cont == input('')
        elif cont == 'c':
            eat()
        elif cont == 'd':
            clearscreen()
            print('----------------------------------------------------------')
            print('You fled.')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            input('')
            clearscreen()
            return False
        
        if enemyhealth <= 0:
            clearscreen()
            print('--------------------------FIGHT--------------------------')
            print(f'You eliminate {name}, proudly taking your victory.')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            cont == input('')
            clearscreen()
            return True
        
        health = int(health) - int(damage)
        clearscreen()
        print('--------------------------FIGHT--------------------------')
        print(f'{name} {attackstring}')
        print(f'Health - {damage}!')
        print('-----------------PRESS ENTER TO CONTINUE-----------------')
        cont == input('')

        if health <= 0:
            health = 1
            clearscreen()
            print('----------------------------------------------------------')
            print(f'You died. {name} killed you.')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            input('')
            onjourney = False
            inbunker = False
            quit()
        

def percentage(val1, val2):
    return val1/val2*100

def stats():
    clearscreen()
    print('--------------------------STATS--------------------------')
    print(f'You have {health}/100 health, {water}/100 water, and')
    print(f'{foodnum}/100 food!')
    print('-----------------PRESS ENTER TO CONTINUE-----------------')
    input('')

def eat():
    global health, water, foodnum, cont, actions
    clearscreen()
    print('---------------What would you like to eat?---------------')
    for obj in fooditems:
        print(obj)
    print('----------------TYPE WHAT YOU WANT TO EAT----------------')
    val = input('').lower().strip()
    clearscreen()
    for x in range(0, int(len(fooditems))):
        y = fooditems[x].type
        if y == val:
            print('----------------------------------------------------------')
            print(f'You ate the {fooditems[x].type}')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            cont = input('')
            clearscreen()
            print('--------------------------STATS--------------------------')
            print(f'You HAD {health}/100 health, {water}/100 water, and')
            print(f'{foodnum}/100 food!')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            cont = input('')
            health = int(health) + int(fooditems[x].healthinc)
            water = int(water) + int(fooditems[x].waterinc)
            foodnum = int(foodnum) + int(fooditems[x].foodinc)
            if health > 100:
                health = 100
            if water > 100:
                water = 100
            if foodnum > 100:
                foodnum = 100
            stats()
            fooditems.pop(x)
            actions -= 1
            return

def removefood(val):
    for x in range(0, int(len(fooditems))):
        y = fooditems[x].type
        if y == val:
            fooditems.pop(x)
            return True
    return False
            
def haveitem(val):
    for x in range(0, int(len(items))):
        y = items[x].type
        if y == val:
            return True
    return False

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def displaymap(val):
    global cont, location, saveinfo, locx, locy, bunkloc
    while True:
        clearscreen()
        print('---------------------------MAP---------------------------')
        print('■ = You, n = City/Buildings, and ○ = Other Bunkers.')
        print('---------------------------------------------------------')
        for list in worldmap:
            for x in list:
                print(x, end="")
            print('')
        if not val:
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            input('')
            return
        else:
            worldmap[locy][locx] = saveinfo
            print('---------------------------------------------------------')
            print('Select a direction to move: (USES WASD!)')
            print('W: Up')
            print('S: Down')
            print('A: Left')
            print('D: Right')
            print('E: Return Home')
            print('------------------SELECT ONE TO CONTINUE-----------------')  
            cont = input('').lower()
            if cont == 'd' and locx != 19:
                locx += 2
            if cont == 'w' and locy != 1:
                locy -= 2
            if cont == 's' and locy != 13:
                locy += 2
            if cont == 'a' and locx != 1:
                locx -= 2
            if cont == 'e':
                worldmap[locy][locx] = saveinfo
                locx = 1
                locy = 1
                saveinfo = worldmap[locy][locx]
                worldmap[locy][locx] = '■ '
                return
            saveinfo = worldmap[locy][locx]
            bunkloc = locy
            if saveinfo == 'n ':
                city()
                return
            elif saveinfo == '○ ':
                otherbunker()
                return
            worldmap[locy][locx] = '■ '

def city():
    global cont, health, rand, location, saveinfo, locx, locy, bunkloc
    rand = random.randint(0, 7)
    if rand == 0:
        clearscreen()
        print('-----------------------INTERACTION-----------------------')
        print('You see a box of bandages on the floor. It is next to')
        print('blood stains but some are new. Do you take it?')
        print('A: Yes')
        print('B: No')
        print('-----------------SELECT ONE TO CONTINUE------------------')
        cont = input('').lower()
        if cont == 'a':
            fooditems.append(food('okay', 'old bandage', 0, 30, 0))
            clearscreen()
            print('-----------------------INTERACTION-----------------------')
            print('You gained bandages.')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            cont = input('')
        clearscreen()
    if rand == 1:
        clearscreen()
        print('-----------------------INTERACTION-----------------------')
        print('You see some bottles of water on the floor. It seems')
        print('clean to drink. Do you take it?')
        print('A: Yes')
        print('B: No')
        print('-----------------SELECT ONE TO CONTINUE------------------')
        cont = input('').lower()
        if cont == 'a':
            fooditems.append(food('okay', 'dirty water', 0, 0, 20))
            fooditems.append(food('okay', 'dirty water', 0, 0, 20))
            clearscreen()
            print('-----------------------INTERACTION-----------------------')
            print('You gained 2 water.')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            cont = input('')
        clearscreen()
    if rand == 2:
        clearscreen()
        print('-----------------------INTERACTION-----------------------')
        print('You someone sneaking around with many apples. It seems')
        print('easy to take from them. Do you take it?')
        print('A: Yes')
        print('B: No')
        print('-----------------SELECT ONE TO CONTINUE------------------')
        cont = input('').lower()
        if cont == 'a':
            if attack('Apple Guy', random.randint(11,14), 'chucks an apple at you!'):
                fooditems.append(food('good', 'apple', 25, 20, 10))
                fooditems.append(food('good', 'apple', 25, 20, 10))
                clearscreen()
                print('-----------------------INTERACTION-----------------------')
                print('You gained 2 apple.')
                print('-----------------PRESS ENTER TO CONTINUE-----------------')
                cont = input('')
            else:
                fooditems.append(food('good', 'apple', 25, 20, 10))
                clearscreen()
                print('-----------------------INTERACTION-----------------------')
                print('You collect the chucked apple.')
                print('-----------------PRESS ENTER TO CONTINUE-----------------')
                cont = input('')
        clearscreen()
    worldmap[locy][locx] = saveinfo
    locx = 1
    locy = 1
    saveinfo = worldmap[locy][locx]
    worldmap[locy][locx] = '■ '

def otherbunker():
    global cont, location, saveinfo, locx, locy, bunkloc
    if bunkloc == 5:
        clearscreen()
        print('-----------------------INTERACTION-----------------------')
        print('You come across another bunker with a mom and their')
        print('child. They seems to have some resources and would')
        print('be benificial to steal from. Do you?')
        print('A: Yes')
        print('B: No')
        print('-----------------SELECT ONE TO CONTINUE------------------')
        cont = input('').lower()
        if cont == 'a':
            if attack('The mother', random.randint(14,17), 'attack you with fierce slaps!'):
                fooditems.append(food('good', 'apple', 25, 20, 10))
                fooditems.append(food('good', 'apple', 25, 20, 10))
                fooditems.append(food('okay', 'bandage', 0, 50, 0))
                fooditems.append(food('okay', 'bandage', 0, 50, 0))
                clearscreen()
                print('-----------------------INTERACTION-----------------------')
                print('You gained 2 apple and 2 bandages.')
                print('-----------------PRESS ENTER TO CONTINUE-----------------')
                cont = input('')
    if bunkloc == 7:
        clearscreen()
        print('-----------------------INTERACTION-----------------------')
        print('You come across another bunker a lone man who seems to')
        print('have lots of food. They are fat. Do you want to steal')
        print('whatever they have?')
        print('A: Yes')
        print('B: No')
        print('-----------------SELECT ONE TO CONTINUE------------------')
        cont = input('').lower()
        if cont == 'a':
            if attack('The guy', random.randint(19,22), 'body slams you with all their weight!'):
                fooditems.append(food('good', 'apple', 25, 20, 10))
                fooditems.append(food('good', 'apple', 25, 20, 10))
                fooditems.append(food('good', 'apple', 25, 20, 10))
                fooditems.append(food('good', 'apple', 25, 20, 10))
                clearscreen()
                print('-----------------------INTERACTION-----------------------')
                print('You gained 4 apple and bandages.')
                print('-----------------PRESS ENTER TO CONTINUE-----------------')
                cont = input('')
    if bunkloc == 11:
        clearscreen()
        print('-----------------------INTERACTION-----------------------')
        print('A doctor who came to your country during these bad times')
        print('seems to be helping people with their wounds. There are')
        print('nice resources only protected by the doctor. ')
        print('Do you? or do you not?')
        print('A: Yes')
        print('B: No')
        print('-----------------SELECT ONE TO CONTINUE------------------')
        cont = input('').lower()
        if cont == 'a':
            if attack('The doctor', random.randint(23,27), 'hits you with his equipment!'):
                fooditems.append(food('okay', 'bandage', 0, 50, 0))
                fooditems.append(food('okay', 'bandage', 0, 50, 0))
                fooditems.append(food('okay', 'bandage', 0, 50, 0))
                fooditems.append(food('okay', 'bandage', 0, 50, 0))
                clearscreen()
                print('-----------------------INTERACTION-----------------------')
                print('You gained 4 bandages.')
                print('-----------------PRESS ENTER TO CONTINUE-----------------')
                cont = input('')
    if bunkloc == 13:
        clearscreen()
        print('-----------------------INTERACTION-----------------------')
        print('You see enemy soldiers in the distance. They seems to ')
        print('have taken over someones bunker and its resources. Do')
        print('want to make an effort to fight for your country?')
        print('They have guns afterall.')
        print('A: Yes')
        print('B: No')
        print('-----------------SELECT ONE TO CONTINUE------------------')
        cont = input('').lower()
        if cont == 'a':
            if attack('The soldiers', random.randint(25,75), 'clutch their guns in their hands and shoot!'):
                fooditems.append(food('good', 'apple', 25, 20, 10))
                fooditems.append(food('good', 'apple', 25, 20, 10))
                fooditems.append(food('okay', 'bandage', 0, 50, 0))
                fooditems.append(food('okay', 'bandage', 0, 50, 0))
                items.append(item('grasp your ak and shoot', 'ak', 75))
                clearscreen()
                print('-----------------------INTERACTION-----------------------')
                print('You gained 2 apple, 2 bandages and an ak')
                print('-----------------PRESS ENTER TO CONTINUE-----------------')
                cont = input('')
    worldmap[locy][locx] = saveinfo
    locx = 1
    locy = 1
    saveinfo = worldmap[locy][locx]
    worldmap[locy][locx] = '■ '

def inv():
    clearscreen()
    print('-------------------Your Food Inventory-------------------')
    for obj in fooditems:
        print(obj)
    print('-----------------PRESS ENTER TO CONTINUE-----------------')
    input('')
    clearscreen()
    print('-------------------Your Item Inventory-------------------')
    for obj in items:
        print(obj)
    print('-----------------PRESS ENTER TO CONTINUE-----------------')
    input('')
    clearscreen()

def interact():
    global actions, gardenbook, waterbook, genbook, boatbook, gunbook, generator, waterfilter
    clearscreen()
    print('---------------What Would You Like To Do?----------------')
    print('You look around the room for something to interact with.')
    print('A: Bookshelf')
    print('B: Garden')
    print('C: Generator')
    print('D: Water Filering Device')
    print('E: Cancel')
    print('-----------------SELECT ONE TO CONTINUE------------------')
    cont = input('').lower().strip()
    if cont == 'a':
        clearscreen()
        print('--------------What Would You Like To Read?---------------')
        print('You look in the bookshelf for something to read. You find:')
        print('A: Gardening')
        print('B: Water Filtration Systems')
        print('C: Generator Manual')
        print('D: Boating')
        print('E: Cancel')
        print('-----------------SELECT ONE TO CONTINUE------------------')
        cont = input('').lower()
        clearscreen()
        if cont == 'a' and gardenbook != 5:
            gardenbook += 1
            print('---------------------------------------------------------')
            print(f'You read {percentage(gardenbook, 5)}% of the book')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            actions -= 1
            cont = input('').upper()
            return
        elif cont == 'b' and waterbook != 4:
            waterbook += 1
            print('---------------------------------------------------------')
            print(f'You read {percentage(waterbook, 4)}% of the book')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            actions -= 1
            cont = input('').upper()
            return
        elif cont == 'c' and genbook != 6:
            genbook += 1
            print('---------------------------------------------------------')
            print(f'You read {percentage(genbook, 6)}% of the book')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            actions -= 1
            cont = input('').upper()
            return
        elif cont == 'd' and boatbook != 10:
            boatbook += 1
            print('---------------------------------------------------------')
            print(f'You read {percentage(boatbook, 10)}% of the book')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            actions -= 1
            cont = input('').upper()
            return
        elif cont == 'e':
            return
        print('---------------------------------------------------------')
        print('You read nothing. You stared at the wall.')
        print('-----------------PRESS ENTER TO CONTINUE-----------------')
        cont = input('').upper()
        
    if cont == 'b':
        clearscreen()
        if not generator and gardenbook < 5:
            print('----------------------------------------------------------')
            print('You go to the garden. It cannot be farmed as it needs')
            print('UV light to grow. You also need knowledge of gardening.')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            input('')
        elif gardenbook < 5:
            print('----------------------------------------------------------')
            print('You go to the garden. You need knowledge of gardening.')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            input('')
        elif gardenbook >= 5 and generator:
            print('----------------------------------------------------------')
            print('You go to the garden. You can farm it, costing 1 action')
            print('but producing 1 apple.')
            print('A: Yes')
            print('B: No')
            print('-----------------SELECT ONE TO CONTINUE------------------')
            cont = input('').lower()
            if cont == 'a':
                clearscreen()
                fooditems.append(food('good', 'apple', 25, 20, 10))
                print('----------------------------------------------------------')
                print('You picked an apple') 
                print('-----------------PRESS ENTER TO CONTINUE-----------------')
                cont = input('').upper()
                actions -= 1
            else:
                return
    if cont == 'c':
        clearscreen()
        if genbook != 6:
            print('----------------------------------------------------------')
            print('You look at the generator with the intent to fix it, but') 
            print('absolutely no idea how to fix it. There must be a way')
            print('to learn how.')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            cont = input('')
            return
        elif not generator and genbook >= 6:
            print('----------------------------------------------------------')
            print('You look at the generator and swiftly realize that you') 
            print('need to flip a switch to turn it on. It works now.')
            print('That took you 4 hours. You are proud.')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            cont = input('')
            generator = True
        elif generator:
            print('----------------------------------------------------------')
            print('You already fixed this.') 
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            cont = input('')
            return
        actions -= 1
    if cont == 'd':
        clearscreen()
        if waterbook != 4:
            print('----------------------------------------------------------')
            print('You have no clue how to fix the water filter. Maybe you')
            print('can learn? But where?') 
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            cont = input('')
            return
        elif not waterfilter and waterbook >= 4:
            print('----------------------------------------------------------')
            print('You quickly fix this dang thing. It had a rock that') 
            print('clogged it. Good thing for your expertise.')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            cont = input('')
            waterfilter = True
            actions -= 1
        elif waterfilter:
            print('----------------------------------------------------------')
            print('Do you want to use 1 action to produce 1 water? ')
            print('A: Yes')
            print('B: No')
            print('-----------------SELECT ONE TO CONTINUE------------------')
            cont = input('').lower()
            if cont == 'a':
                clearscreen()
                fooditems.append(food('okay', 'water', 0, 0, 50))
                print('----------------------------------------------------------')
                print('You got 1 water') 
                print('-----------------PRESS ENTER TO CONTINUE-----------------')
                cont = input('').upper()
                actions -= 1
            else:
                return
    if cont == 'e':
        return
    return

def randomevent():
    global cont, health
    rand = random.randint(0, 10)
    if rand == 0:
        clearscreen()
        print('-----------------------INTERACTION-----------------------')
        print('A man appears at your bunker door. He asks for only an')
        print('apple. He will bandages in return.')
        print('A: Accept')
        print('B: Decline')
        print('C: Attack')
        print('-----------------SELECT ONE TO CONTINUE------------------')
        cont = input('').lower()
        clearscreen()
        if cont == 'a':
            removefood('apple')
            fooditems.append(food('okay', 'bandage', 0, 50, 0))
            print('-----------------------INTERACTION-----------------------')
            print('You gained a bandages. It can help you heal.')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            cont = input('')
            clearscreen()
        elif cont == 'b':
            print('-----------------------INTERACTION-----------------------')
            print('He keeps the bandages and leaves.')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            cont = input('')
            clearscreen()
        elif cont == 'c':
            if attack('The Man', random.randint(5,10), 'attempts to strangle you with his bandages.'):
                fooditems.append(food('okay', 'bandage', 0, 50, 0))
                clearscreen()
                print('-----------------------INTERACTION-----------------------')
                print('You gained bandages. (It is food, as you eat them).')
                print('-----------------PRESS ENTER TO CONTINUE-----------------')
                cont = input('')
                clearscreen()
    elif rand == 1:
        clearscreen()
        print('-----------------------INTERACTION-----------------------')
        print('A man appears at your bunker door. He asks for only an')
        print('apple. He will give his jacket in return.')
        print('A: Accept')
        print('B: Decline')
        print('C: Attack')
        print('-----------------SELECT ONE TO CONTINUE------------------')
        cont = input('').lower()
        clearscreen()
        if cont == 'a':
            removefood('apple')
            items.append(item('use your jacket to shmack', 'jacket', 10))
            print('-----------------------INTERACTION-----------------------')
            print('You gained a jacket. It can help you survive the rain.')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            cont = input('')
            clearscreen()
        elif cont == 'b':
            print('-----------------------INTERACTION-----------------------')
            print('He said its okay, as he will only starve.')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            cont = input('')
            clearscreen()
        elif cont == 'c':
            if attack('The Man', random.randint(10,14), 'whips out his jacket and smacks you as hard as he can.'):
                items.append(item('use your jacket to shmack', 'jacket', 10))
                clearscreen()
                print('-----------------------INTERACTION-----------------------')
                print('You gained a jacket.')
                print('-----------------PRESS ENTER TO CONTINUE-----------------')
                cont = input('')
                clearscreen()
    elif rand == 2:
        clearscreen()
        print('-----------------------INTERACTION-----------------------')
        print('A child appears at your bunker front door. They want')
        print('water for their dehydrated mother. They will give a')
        print('fire starting kit.')
        print('A: Accept')
        print('B: Decline')
        print('C: Attack')
        print('-----------------SELECT ONE TO CONTINUE------------------')
        cont = input('').lower()
        clearscreen()
        if cont == 'a':
            removefood('water')
            items.append(item('use the kit to whack', 'fire starting kit', 15))
            print('-----------------------INTERACTION-----------------------')
            print('They give you the kit and say thanks.')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            cont = input('').lower()
            clearscreen()
        elif cont == 'b':
            print('-----------------------INTERACTION-----------------------')
            print('The child curses you and performs voodoo magic on you.')
            print('Health -10.')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            health -= 10
            cont = input('').lower()
            clearscreen()
        elif cont == 'c':
            if attack('The child', random.randint(4,7), 'punches you as hard as he can.'):
                items.append(item('use the kit to whack', 'fire starting kit', 15))
                clearscreen()
                print('-----------------------INTERACTION-----------------------')
                print('You gained a fire starting kit.')
                print('-----------------PRESS ENTER TO CONTINUE-----------------')
                cont = input('').lower()
                clearscreen()
    elif rand == 3:
        clearscreen()
        print('-----------------------INTERACTION-----------------------')
        print('A hunter appears at your front door with a knife in his')
        print('hand. He says its for cutting the apple you will')
        print('give him. What do you do? He does not seem skilled.')
        print('A: Accept')
        print('B: Decline')
        print('C: Attack Him')
        print('-----------------SELECT ONE TO CONTINUE------------------')
        cont = input('').lower()
        clearscreen()
        if cont == 'a':
            removefood('apple')
            print('-----------------------INTERACTION-----------------------')
            print('You lose an apple.')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            cont = input('').lower()
            clearscreen()
        elif cont == 'b':
            health -= 50
            print('-----------------------INTERACTION-----------------------')
            print('He utilizes his knife on you.')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            cont = input('').lower()
            clearscreen()
        elif cont == 'c':
            if attack('The hunter', random.randint(1, 30), 'hits you with his knife'):
                items.append(item('hold your knife and jab', 'knife', 45))
                clearscreen()
                print('-----------------------INTERACTION-----------------------')
                print('You gained knife.')
                print('-----------------PRESS ENTER TO CONTINUE-----------------')
                cont = input('').lower()
                clearscreen()
    elif rand == 4:
        clearscreen()
        print('-----------------------INTERACTION-----------------------')
        print('Two kids appear at your front door, dehydrated and barely')
        print('able to speak. They desperately need water. Will you')
        print('give them water?')
        print('A: Accept')
        print('B: Decline')
        print('C: Eat in front of them')
        print('D: Attack them')
        print('-----------------SELECT ONE TO CONTINUE------------------')
        cont = input('').lower()
        clearscreen()
        if cont == 'a':
            removefood('water')
            print('-----------------------INTERACTION-----------------------')
            print('They thank you.')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            cont = input('').lower()
            clearscreen()
        elif cont == 'b':
            print('-----------------------INTERACTION-----------------------')
            print('They collapse in front of your door. Avoid them while')
            print('walking out.')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            cont = input('').lower()
            clearscreen()
        elif cont == 'c':
            health -= 1
            eat()
            print('-----------------------INTERACTION-----------------------')
            print('They punch you to beat you up with their last bit of')
            print('energy. Health -1.')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            cont = input('').lower()
            clearscreen()
        elif cont == 'd':
            if attack('The children', 1, 'smack you with a small slap.'):
                clearscreen()
                print('-----------------------INTERACTION-----------------------')
                print('You gained nothing at all. Except the fact that you had')
                print('attacked them. What was the point?')
                print('-----------------PRESS ENTER TO CONTINUE-----------------')
                cont = input('').lower()
                clearscreen()
    elif rand == 5 and not haveitem('ak'):
        clearscreen()
        print('-----------------------INTERACTION-----------------------')
        print('A short lady with her son appears at the door of your')
        print('bunker asking for help. She wants water')
        print('and the son will give an ak-47.')
        print('A: Yes')
        print('B: No')
        print('C: Attack them')
        print('-----------------SELECT ONE TO CONTINUE------------------')
        cont = input('').lower()
        clearscreen()
        if removefood('water') and cont == 'a':
            items.append(item('grasp your ak and shoot', 'ak', 75))
            clearscreen()
            print('-----------------------INTERACTION-----------------------')
            print('The 5 year old boy hands you the ak-47.')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            cont = input('')
            return
        elif cont == 'c':
            if attack('The 5 year old', random.randint(50,75), 'shoots you with his gun...'):
                clearscreen()
                print('-----------------------INTERACTION-----------------------')
                print('You gained nothing at all.')
                print('-----------------PRESS ENTER TO CONTINUE-----------------')
                cont = input('').lower()
                clearscreen()
        else:
            clearscreen()
            print('-----------------------INTERACTION-----------------------')
            print('They called you a scammer as you do not have what they. ')
            print('want. The kid stares at you as he holds his gun and walks')
            print('away. Scary.')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            cont = input('')
            return
    elif rand >= 6:
        return


# The start of the intro ----------------------------------------------------------------------------------

if startgame:
    clearscreen()
    print('----------------------------------------------------------')
    print('                Welcome to this text game.')
    print('  type the letter associated with the option you want to')
    print('    choose. Press enter to continue dialouge and text.')
    print('                 Are you ready to start?')
    print('-----------------PRESS ENTER TO CONTINUE-----------------')
    cont = input('')
    time.sleep(0.5)

    clearscreen()
    print('----------------------------------------------------------')
    print('You hear sirens blaring outside your front door, the')
    print('screams of the people you know echoing through the streets.')
    print('You look through your window to see bombs dropping')
    print('from the sky, whistling as they fall.')
    print('-----------------PRESS ENTER TO CONTINUE-----------------')
    cont = input('')
    time.sleep(0.5)

    clearscreen()
    print('----------------------------------------------------------')
    print('You must grab as many things as you can before you go')
    print('into your bunker, for you must escape this country')
    print('when the time is right, and the sky calms.')
    print('-----------------PRESS ENTER TO CONTINUE-----------------')
    cont = input('')
    time.sleep(0.5)


# Item choosing ----------------------------------------------------------------------------------

if startgame:
    while startitems != 0:
        clearscreen()

        print('----------------------------------------------------------')
        print(f'Pick {startitems} things before you enter the bunker.')
        print('A: Apple')
        print('B: Water')
        print('C: Canned Food')
        print('-----------------SELECT ONE TO CONTINUE------------------')
        cont = input('').lower().strip()
        clearscreen()
        
        print('----------------------------------------------------------')
        if cont == 'a':
            fooditems.append(food('good', 'apple', 25, 20, 10))
            print('You picked an apple') 
        elif cont == 'b':
            fooditems.append(food('okay', 'water', 0, 0, 50))
            print('You picked water')
        elif cont == 'c':
            fooditems.append(food('excellent', 'canned food', 30, 5, 30))
            print('You picked canned food')
        else:
            print('You picked nothing!')
        print('-----------------PRESS ENTER TO CONTINUE-----------------')
        cont = input('')
        startitems -= 1
    time.sleep(0.5)
    inv()


    clearscreen()
    print('----------------------------------------------------------')
    print('You enter the bunker with your items in hand. ')
    print('You walk around the dusty room and see whats around.')
    print('-----------------PRESS ENTER TO CONTINUE-----------------')
    cont = input('')
    time.sleep(0.5)

    clearscreen()
    print('----------------------------------------------------------')
    print('You see your bed. The sheets covered in dust, but')
    print('its better than nothing.')
    print('-----------------PRESS ENTER TO CONTINUE-----------------')
    cont = input('')
    time.sleep(0.5)

    clearscreen()
    print('----------------------------------------------------------')
    print('You see a bookshelf. It contains few books but must')
    print('have some useful information.')
    print('-----------------PRESS ENTER TO CONTINUE-----------------')
    cont = input('')
    time.sleep(0.5)

    clearscreen()
    print('----------------------------------------------------------')
    print('You see a water filtering device. It seems to be broken')
    print('but is needed for cleaning the dirty water that flows to')
    print('your bunker.')
    print('-----------------PRESS ENTER TO CONTINUE-----------------')
    cont = input('')
    time.sleep(0.5)

    clearscreen()
    print('----------------------------------------------------------')
    print('You see a generator. It does not seem to work and needs')
    print('fixing. You are stuck with only power for lights.')
    print('You will need it to get out.')
    print('-----------------PRESS ENTER TO CONTINUE-----------------')
    cont = input('')
    time.sleep(0.5)

    clearscreen()
    print('----------------------------------------------------------')
    print('You see a small area to grow foods. It seems to use water')
    print('from outside but does not get sunlight. It needs power to')
    print('turn on the UV lights for the plants to grow.')
    print('-----------------PRESS ENTER TO CONTINUE-----------------')
    cont = input('')
    time.sleep(0.5)
    startgame = False

# In Bunker ---------------------------------------------------------------------------------

while inbunker:
    actions = 3
    cont = None
    if day >= 10 and generator:
        randomevent()
    while actions != 0:
        clearscreen()
        print('---------------What Would You Like to Do?----------------')
        if day <= 10:
            print(f'It is currently day {day} today. You hear bombs and')
            print('war outside the bunker, although it seems to be calming.')
            print('It is best to stay inside.')
        else:
            print(f'It is currently day {day} today. It seems it has calmed')
            print('outside. Maybe its time to explore and prepare to leave.')
        while True:
            print('----------------------------------------------------------')
            print('Pick one of the following to do. Once you used up your')
            print(f'actions for the day, sleep. You have {actions} actions left.')
            print('A: Interact')
            print('B: Eat')
            print('C: Sleep')
            print('D: Explore Outside')
            print('E: Inventory')
            print('F: Stats')
            print('G: Display Map')
            print('H: Start Journey To Leave Your Country')
            print('-----------------SELECT ONE TO CONTINUE------------------')
            cont = input('').lower().strip()
            if cont == 'a' and actions != 0:
                interact()
                cont = None
            if cont == 'b' and actions != 0: #EAT
                eat()
                cont = None
            if cont == 'c': #SLEEP
                clearscreen()
                print('--------------------------SLEEP--------------------------')
                print('You head towards your bed, ready to sleep.')
                if actions == 3:
                    print('It was a short day, but tiring regardless.')
                elif actions == 2:
                    print('You did something today, enough to make you tired.')
                elif actions == 1:
                    print('You did a lot today. Rest was needed.')
                elif actions == 0:
                    print('You did too much today, sleeping instantly as you')
                    print('enter your bed.')
                print('-----------------PRESS ENTER TO CONTINUE-----------------')
                actions = 0
                input('')
                cont = None
                break
            if cont == 'd' and actions != 0 and day >  10 and generator:
                actions -= 1
                clearscreen()
                print('----------------------------------------------------------')
                print('You exit your bunker, ready to explore.')
                print('-----------------PRESS ENTER TO CONTINUE-----------------')
                cont = input('')
                displaymap(True)
                cont = None
            elif cont == 'd':
                clearscreen()
                print('----------------------------------------------------------')
                print('It must to be safe outside and you must fix the generator.')
                print('-----------------PRESS ENTER TO CONTINUE-----------------')
                cont = input('')
                cont = None
            if cont == 'e': 
                inv()
                cont = None
            if cont == 'f': 
                stats()
                cont = None
            if cont == 'g': 
                displaymap(False)
                cont = None
            if cont == 'h' and generator and day >= 10:
                clearscreen()
                print('----------------------------------------------------------')
                print('Are you sure you want to leave? You will not be able to')
                print('return.')
                print('A: Yes, Leave')
                print('B: No, Stay')
                print('-----------------PRESS ENTER TO CONTINUE-----------------')
                cont = input('').lower()
                if cont == 'a':
                    inbunker = False
                    onjourney = True
                    break
                else:
                    pass
            elif cont == 'h':
                clearscreen()
                print('----------------------------------------------------------')
                print('It must to be safe outside and you must fix the generator.')
                print('-----------------PRESS ENTER TO CONTINUE-----------------')
                cont = input('')
                cont = None
            clearscreen()
    water -= random.randint(25, 33)
    foodnum -= random.randint(4, 8)
    stats()
    if health <= 0:
        clearscreen()
        print('----------------------------------------------------------')
        print('You died. You starved!')
        print('-----------------PRESS ENTER TO CONTINUE-----------------')
        input('')
        quit()
        
    if water <= 0:
        clearscreen()
        print('----------------------------------------------------------')
        print('Your water levels are too low such that you lose health.')
        print('Health -50.')
        print('-----------------PRESS ENTER TO CONTINUE-----------------')
        input('')
        health -= 50
    elif foodnum == 0:
        clearscreen()
        print('----------------------------------------------------------')
        print('Your food levels are too low. You suffer from malnutrition!')
        print('Health -33..')
        print('-----------------PRESS ENTER TO CONTINUE-----------------')
        input('')
        health -= 33
    day += 1
    
clearscreen()
print('----------------------------------------------------------')
print('You exit your bunker, ready to leave for the border.')
print('Except a group of enemy soldiers spot you. They wanted')
print('to question you, noticed you were not on their side.')
print('You try convincing them that you are, in fact, on their')
print('side and you support them.')
print('-----------------PRESS ENTER TO CONTINUE-----------------')
cont = input('')
time.sleep(0.5)

clearscreen()
print('----------------------------------------------------------')
print("They don't buy it. You run towards the border, knowing it")
print('will be a long journey. The soldiers chase you.')
print('-----------------PRESS ENTER TO CONTINUE-----------------')
cont = input('')
time.sleep(0.5)

# On Journey ----------------------------------------------------------------------

while onjourney:
    actions = 3
    cont = None
    rand = random.randint(0,8)
    clearscreen()
    if rand == 0:
        print('----------------------------------------------------------')
        print('You come across a wild boar searching for food. It seems')
        print(f'to be eating good. Do you hunt it?')
        print('A: Yes, hunt')
        print('B: No, ignore')
        print('-----------------SELECT ONE TO CONTINUE------------------')
        cont = input('').lower().strip()
        if cont == 'a':
            clearscreen()
            if attack('The wild boar', random.randint(20, 40), 'charges toward you and rams you.'):
                clearscreen()
                print('----------------------------------------------------------')
                print('The boar collaspes onto the floor. Do you want to take')
                print(f'its meat. Its easier with a knife.')
                print('A: Yes')
                print('B: No')
                print('-----------------SELECT ONE TO CONTINUE------------------')
                cont = input('').lower().strip()
                clearscreen()
                if cont == 'a' and haveitem('knife'):
                    fooditems.append(food('good', 'boar meat', 60, 0, 0))
                    fooditems.append(food('good', 'boar meat', 60, 0, 0))
                    fooditems.append(food('good', 'boar meat', 60, 0, 0))
                    fooditems.append(food('good', 'boar meat', 60, 0, 0))
                    print('----------------------------------------------------------')
                    print('You gained 4 boar meat.')
                    print('-----------------PRESS ENTER TO CONTINUE-----------------')
                    cont = input('')
                elif cont == 'a':
                    fooditems.append(food('good', 'boar meat', 60, 0, 0))
                    print('----------------------------------------------------------')
                    print('You gained 1 boar meat before you leave.')
                    print('-----------------PRESS ENTER TO CONTINUE-----------------')
                    cont = input('')
                
    if rand == 1:
        clearscreen()
        rain = True
        print('----------------------------------------------------------')
        print('It starts to rain heavily. It seems to be better to set')
        print(f'up camp and sleep early today. You may get sick from')
        print('the cold water, unless you got a jacket. Do you wait?')
        print('-----------------PRESS ENTER TO CONTINUE-----------------')
        cont = input('')
    if rand == 2:
        clearscreen()
        print('----------------------------------------------------------')
        print('You find a river with flowing water. It seems to be safe')
        print('to drink but who knows? Do you boil it first?')
        print('There are also boats you can take.')
        print('A: Yes (Must Have Fire Starting Kit)')
        print('B: No, take without cleaning')
        print("C: Don't Take At All")
        print('D: Use Boats To Travel')
        print('-----------------SELECT ONE TO CONTINUE------------------')
        cont = input('').lower().strip()
        if cont == 'a' and haveitem('fire starting kit'):
            clearscreen()
            fooditems.append(food('okay', 'water', 0, 0, 50))
            print('----------------------------------------------------------')
            print('You gained water.')
            print('-----------------SELECT ONE TO CONTINUE------------------')
            cont = input('')
        elif cont == 'b':
            clearscreen()
            fooditems.append(food('okay', 'dirty water', 0, -10, 40))
            print('----------------------------------------------------------')
            print('You gained dirty water.')
            print('-----------------SELECT ONE TO CONTINUE------------------')
            cont = input('')
        elif cont == 'd' and boatbook >= 10:
            travel = random.randint(35, 45)
            distance += travel
            clearscreen()
            print('----------------------------------------------------------')
            print(f'You traveled {travel}km. Now travelled {distance}km far.')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            cont = input('')
            cont = None
            actions -= 1
        elif cont == 'd' and boatbook <10:
            clearscreen()
            print('----------------------------------------------------------')
            print(f'You need to learn to boat first.')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            cont = input('')
            
    if rand == 3:
        clearscreen()
        print('----------------------------------------------------------')
        print('You see other enemy soldiers in the distance. Do you')
        print('fight them?')
        print('A: Yes')
        print('B: No')
        print('-----------------PRESS ENTER TO CONTINUE-----------------')
        cont = input('').lower().strip()
        clearscreen()
        if cont == 'a':
            if attack('The soldiers', random.randint(30,55), 'They shoot at you!'):
                fooditems.append(food('okay', 'water', 0, 0, 50))
                fooditems.append(food('okay', 'water', 0, 0, 50))
                fooditems.append(food('okay', 'water', 0, 0, 50))
                fooditems.append(food('okay', 'water', 0, 0, 50))
                fooditems.append(food('okay', 'water', 0, 0, 50))
                print('----------------------------------------------------------')
                print('You gained 5 water.')
                print('-----------------SELECT ONE TO CONTINUE------------------')
                cont = input('')
    if rand == 4:
        clearscreen()
        rain = True
        print('----------------------------------------------------------')
        print('You look at the forest your in. It seems quite dry and')
        print('would set fire easily. That is if you can. Do you?')
        print('A: Start Fire (Requires fire starting kit)')
        print('B: No')
        print('-----------------PRESS ENTER TO CONTINUE-----------------')
        cont = input('').lower()
        if cont == 'a' and haveitem('fire starting kit'):
            delaydistance = random.randint(5,10)
            print('----------------------------------------------------------')
            print('The forest sets on fire, delaying the chasing soldiers')
            print(f'by {delaydistance}km.')
            print('-----------------SELECT ONE TO CONTINUE------------------')
            cont = input('')
    while actions != 0:
        while True:
            clearscreen()
            print('---------------What Would You Like to Do?----------------')
            print(f'It is currently day {day} today. {journeydays} days have past')
            print('since you left your bunker for the border.')
            print(f'You have travelled {distance}km from the bunker.')
            print(f'The enemy soldiers are {distance - enemydistance}km away!')
            print('----------------------------------------------------------')
            if sick >= 1:
                print('----------------------------------------------------------')
                print(f'You somehow got sick, losing {sick} health per turn.')
                print(f'You have {health} health.')
            print('----------------------------------------------------------')
            print('Pick one of the following to do. Once you used up your')
            print(f'actions for the day, sleep. You have {actions} actions left.')
            print('A: Continue Towards Border')
            print('B: Eat')
            print('C: Sleep')
            print('D: Inventory')
            print('E: Stats')
            print('-----------------SELECT ONE TO CONTINUE------------------')
            cont = input('').lower().strip()
            if cont == 'a' and actions != 0:
                travel = random.randint(7, 10)
                distance += travel
                clearscreen()
                print('----------------------------------------------------------')
                print(f'You traveled {travel}km. Now travelled {distance}km in total.')
                print('-----------------PRESS ENTER TO CONTINUE-----------------')
                cont = input('')
                cont = None
                actions -= 1
            if cont == 'b' and actions != 0: #EAT
                eat()
                cont = None
            if cont == 'c': #SLEEP
                clearscreen()
                print('--------------------------SLEEP--------------------------')
                print('You set up camp, ready to sleep.')
                if actions == 3:
                    print('It was a short day, but you set your bed up for sleep.')
                elif actions == 2:
                    print('You did something today, so you set up your bed and sleep.')
                    if rain and not haveitem('jacket'):
                        sick += random.randint(1,3)
                elif actions == 1:
                    print('You did a lot today. Rest was needed.')
                    if rain and not haveitem('jacket'):
                        sick += random.randint(2,5)
                elif actions == 0:
                    if rain and not haveitem('jacket'):
                        sick += random.randint(5,10)
                    print('You did too much today, unable to prepare your bed')
                    print('for sleep. You had to sleep on the floor.')
                print('-----------------PRESS ENTER TO CONTINUE-----------------')
                actions = 0
                input('')
                cont = None
                break
            if cont == 'd': 
                inv()
                cont = None
            if cont == 'e': 
                stats()
                cont = None
        health -= sick
        enemydistance += random.randint(9, 14)
        water -= random.randint(25, 33)
        foodnum -= random.randint(4, 8)
        stats()
        if water <= 0:
            clearscreen()
            print('----------------------------------------------------------')
            print('Your water levels are too low such that you lose health.')
            print('Health -50.')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            input('')
            health -= 50
        elif foodnum == 0:
            clearscreen()
            print('----------------------------------------------------------')
            print('Your food levels are too low. You suffer from malnutrition!')
            print('Health -33.')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            input('')
            health -= 33
        if distance - enemydistance < 5:
            clearscreen()
            print('----------------------------------------------------------')
            print('Be wary! The enemys are approaching')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            input('')
        if enemydistance >= distance:
            clearscreen()
            print('----------------------------------------------------------')
            print('You died. The soldiers got to you!')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            input('')
            quit()
        if health <= 0:
            clearscreen()
            print('----------------------------------------------------------')
            print('You died. Your health was too low.')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            input('')
            quit()
        if distance >= completiondistance:
            clearscreen()
            print('----------------------------------------------------------')
            print('You arrive at what is the border. They do not let your ')
            print('through as you do not have a passport. You go along the ')
            print('of the border line.')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            input('')
            clearscreen()
            print('----------------------------------------------------------')
            print('After a while you decide to hop the border and illegally')
            print('cross. You make it to a nearby city where war relief ')
            print('efforts are made and you rest.')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            input('')
            clearscreen()
            print('----------------------------------------------------------')
            print('You won!')
            print('-----------------PRESS ENTER TO CONTINUE-----------------')
            input('')
        day += 1
        journeydays += 1
        sick -= 1
        rain = False
