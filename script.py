# run this script to create simulations of consistency
# require functions of AI made decisions

# TO-DO LIST
# - Implement card effects
# - Run turn 1 simulations
# - Fix up card implementation
# - Implement field
# - Implement opponent information
# - Build AI past turn 1

from database import *
from effects import *
import random

# print information
def printInfo():
    # print("DECK")
    # print(playerDeck)
    print("HAND")
    print(playerHand)
    # print("PRIZES")
    # print(playerPrizes)
    # print("DISCARD")
    # print(playerDiscard)

# restarts game
def restartGame():
    playerDeck = MewMewWorlds.copy()
    playerHand = []
    playerPrizes = []
    playerDiscard = []

# sets up the game
def setUpGame():
    random.shuffle(playerDeck)
    counterCheck = drawCards(playerDeck, playerHand, 7)
    mulliganCount = 0

    # for tracking mulligans
    while (counterCheck == 0):
        shuffleCards(playerHand, playerDeck)
        random.shuffle(playerDeck)
        counterCheck = drawCards(playerDeck, playerHand, 7)
        mulliganCount += 1
    drawCards(playerDeck, playerPrizes, 6)

# draws a specified number of cards
# returns: counter check for basic
def drawCards(source, dest, number):
    counter = 0
    for i in range(0,number):
        card = source.pop()
        # debugging for basic
        if (card.cardType == "Pokemon"):
            if (card.stage == "Basic"):
                counter += 1
        dest.append(card)

    return counter

# shuffles hand into deck
def shuffleCards(source, dest):
    for i in range(0,len(source)):
        card = source.pop()
        dest.append(card)
    random.shuffle(dest)

def discardCard(source, card):
    if (card in source):
        source.remove(card)
        playerDiscard.append(card)

def AI_Test(consCheck):
    print("IN AI TEST")
    # print(playerHand)
    counter = 0
    suppCount = 0
    stadCount = 0
    for card in playerHand:
        if (card.cardType == "Pokemon"):
            if (card.name == "Mewtwo & Mew-GX"):
                playCard(playerHand, playerDiscard, selectCard(playerHand, card.name))
                print("MEW MEW ACTIVE")
            elif (card.name == "Mimikyu"):
                playCard(playerHand, playerDiscard, selectCard(playerHand, card.name))
                print("MIMIKYU ACTIVE")
            elif (card.name == "Mew"):
                playCard(playerHand, playerDiscard, selectCard(playerHand, card.name))
                print("MEW ACTIVE")
            elif (card.stage == "Basic"):
                playCard(playerHand, playerDiscard, selectCard(playerHand, card.name))
                print(card.name.upper() + " ACTIVE")

            break

    while (len(playerHand) > 0 and counter == 0):
        counter = 1
        # if (selectCard(playerHand, "Mysterious Treasure")):
        #     if (selectCard(playerHand, "Mewtwo & Mew-GX")):
        #         if (len(searchEffect(playerDeck, "Jirachi-GX", "name")) > 0):
        #             addToHand(playerDeck, playerHand, selectCard(playerDeck, "Jirachi-GX"))
        #             playCard(playerHand, playerDiscard, selectCard(playerHand, "Mysterious Treasure"))
        #             print("MYSTERIOUS TREASURE")

        if (selectCard(playerHand, "Cherish Ball")):
            if (selectCard(playerHand, "Mewtwo & Mew-GX")):
                if (len(searchEffect(playerDeck, "Jirachi-GX", "name")) > 0):
                    addToHand(playerDeck, playerHand, selectCard(playerDeck, "Jirachi-GX"))
                    playCard(playerHand, playerDiscard, selectCard(playerHand, "Cherish Ball"))
                    print("CHERISH BALL")
                    if (selectCard(playerHand, "Jirachi-GX")):
                        playCard(playerHand, playerDiscard, selectCard(playerHand, "Jirachi-GX"))
                        print("PLAY JIRACHI")
                    counter = 0

            elif (selectCard(playerHand, "Mewtwo & Mew-GX") == None):
                if (len(searchEffect(playerDeck, "Mewtwo & Mew-GX", "name")) > 0):
                    addToHand(playerDeck, playerHand, selectCard(playerDeck, "Mewtwo & Mew-GX"))
                    playCard(playerHand, playerDiscard, selectCard(playerHand, "Cherish Ball"))
                    print("CHERISH BALL")
                    if (selectCard(playerHand, "Mewtwo & Mew-GX")):
                        playCard(playerHand, playerDiscard, selectCard(playerHand, "Mewtwo & Mew-GX"))
                        print("MEW MEW")
                    counter = 0

            if (consCheck == False):
                if (len(searchEffect(playerDeck, "Dedenne-GX", "name")) > 0):
                    addToHand(playerDeck, playerHand, selectCard(playerDeck, "Dedenne-GX"))
                    playCard(playerHand, playerDiscard, selectCard(playerHand, "Cherish Ball"))
                    print("CHERISH BALL")
                    counter = 0

        if (selectCard(playerHand, "Viridian Forest") and stadCount == 0):
            playCard(playerHand, playerDiscard, selectCard(playerHand, "Viridian Forest"))
            stadCount = 1
            print("VIRIDIAN FOREST")
            counter = 0
            # Discards a card that can't be used
            if (selectCard(playerHand, "Solgaleo-GX")):
                playCard(playerHand, playerDiscard, selectCard(playerHand, "Solgaleo-GX"))
                addToHand(playerDeck, playerHand, selectCard(playerDeck, "Fire"))
                print("USE VIRIDIAN FOREST")
            elif (selectCard(playerHand, "Naganadel-GX")):
                playCard(playerHand, playerDiscard, selectCard(playerHand, "Naganadel-GX"))
                addToHand(playerDeck, playerHand, selectCard(playerDeck, "Fire"))
                print("USE VIRIDIAN FOREST")
            elif (selectCard(playerHand, "Espeon & Deoxys-GX")):
                playCard(playerHand, playerDiscard, selectCard(playerHand, "Espeon & Deoxys-GX"))
                addToHand(playerDeck, playerHand, selectCard(playerDeck, "Fire"))
                print("USE VIRIDIAN FOREST")
            elif (selectCard(playerHand, "Latios-GX")):
                playCard(playerHand, playerDiscard, selectCard(playerHand, "Latios-GX"))
                addToHand(playerDeck, playerHand, selectCard(playerDeck, "Fire"))
                print("USE VIRIDIAN FOREST")

        if (selectCard(playerHand, "Escape Board")):
            playCard(playerHand, playerDiscard, selectCard(playerHand, "Escape Board"))
            print("ESCAPE BOARD")
        if (selectCard(playerHand, "Welder") and len(searchEffect(playerHand, "Fire", "name")) >= 2 and suppCount == 0):
            playCard(playerHand, playerDiscard, selectCard(playerHand, "Welder"))
            drawEffect(playerDeck, playerHand, 3)
            suppCount = 1
            print("WELDER")
            counter = 0

        if (selectCard(playerHand, "Lillie") and suppCount == 0):
            playCard(playerHand, playerDiscard, selectCard(playerHand, "Lillie"))
            drawEffect(playerDeck, playerHand, 8 - len(playerHand))
            suppCount = 1
            print("LILLIE")
            counter = 0

# simulates consistency checks
# returns: number of consistency cards
def simulateGames(consCount):
    restartGame()
    setUpGame()
    return checkConsistency(playerHand)

# checks if you have a consistency card in hand
# returns: number of consistency cards
def checkConsistency(playerHand):
    counter = 0
    for card in playerHand:
        if (card.consCheck == True):
            counter += 1

    return counter

# runs the script
consCount = 0
for count in range(0, 20):
    consCheck = False
    playerDeck = MewMewWorlds.copy()
    playerHand = []
    playerPrizes = []
    playerDiscard = []
    # print("GAME " + str(count+1))
    if (simulateGames(consCount) > 0):
        consCount += 1
        consCheck = True

    # AI_Test(consCheck)
    # searchEffect(playerDeck, ["Psychic","Dragon"], "type")
    # printInfo()

print("CONSISTENCY: " + str(consCount))
