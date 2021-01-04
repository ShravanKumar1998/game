# Card Class
import pygwidgets
import pygame

class Card():
    def __init__(self, window, rank, suit, value):
        self.window = window
        self.rank = rank
        self.suit = suit
        self.value = value
        # must add code here to save away parameters in instance variables
        # and create two Image objects, one for the current card, one for the backOfCard
        pass     # you can remove this line when you add your own

    # You can remove the print statement below
    # These are just place holders.
    def conceal(self):
        print('Must conceal the card here')

    def setLoc(self, locTuple):
        print('Called setLoc method, passed in', locTuple)

    def reveal(self):
        print('Must reveal card here')

    def getName(self):
        print('Get the name of the card here')

    def getValue(self):
        print('Get the value of the card here')
        pass
    
    def draw(self):
        print('Draw the card here')

    def getCardNameAndValue(self):
        print("Get the card name and value here")
        return "CardName", 0