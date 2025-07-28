from enum import Enum
from objects.phones import Phone
from config.fx import *

class Action(Enum):
    STOP = 1
    FRICATIVE = 2
    NASAL = 3
    AFFRICATE = 4
    LIQUID = 5
    SEMIVOWEL = 6

unvoiced = ["CH", "F", "HH", "K", "P", "S", "SH", "T", "TH"]

stops = ["B", "D", "G", "K", "P", "T"]
fricatives = ["DH", "F", "HH", "S", "SH", "TH", "V", "Z", "ZH"]
nasals = ["M", "N", "NG"]
affricates = ["CH", "JH"]
liquids = ["L", "R"]
semivowels = ["W", "Y"]

class Consonant(Phone):
    def __init__(self, arpa: str, fx: str, is_voiced: bool, action: Action):
        super().__init__(arpa, fx)
        self.is_voiced = is_voiced
        self.action = action

def classify_consonant(token):
    arpa = token
    fx = globals()[(f"fx_{arpa}")] # creates fx_ variable

    # check if voiced
    if arpa in unvoiced:
        is_voiced = False
    else:
        is_voiced = True

    # assign action
    if arpa in stops:
        action = Action.STOP
    elif arpa in fricatives:
        action = Action.FRICATIVE
    elif arpa in nasals:
        action = Action.NASAL
    elif arpa in affricates:
        action = Action.AFFRICATE
    elif arpa in liquids:
        action = Action.LIQUID
    elif arpa in semivowels:
        action = Action.SEMIVOWEL

    consonant = Consonant(arpa, fx, is_voiced, action)
   
    return consonant
