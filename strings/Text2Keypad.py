"""Text To Keypad Note"""
from string import ascii_uppercase


def textToKeypad(s):
    Mob = ["2", "22", "222", "3", "33", "333", "4", "44",
           "444", "5", "55", "555", "6", "66", "666", "7",
           "77", "777", "7777", "8", "88", "888", "9", "99",
           "999", "9999"]
    map = dict(zip(ascii_uppercase, Mob))
    if(s == "0"):
        return "0"

    return map[s]


print(textToKeypad("B"))
