import random
from itertools import product


substitutions = {"e":"3", "i":"1", "o":"0", "s":"$", "a":"@","S":"$", "E":"3"} 
endings = ["01", "02", "20", "19"]

# returns a list of words with substiuted letters
def substitute_letters(word):
    words = []
    possibilities = [c + substitutions.get(c, "") for c in word]
    for subbed in product(*possibilities):
        words.append("".join(subbed))
    return words

# Given a word like 'business' this function will return a list of possible substitutions
# such as ["Bus1n3ss01", "bus1Ness01", "Bus1n3ss20"] etc
def fuzz(word):
    words = substitute_letters(word)
    newWords=[]
    for word in words:
        for ending in endings:
            newWord= word+ending
            newWords.append(newWord)
    print(newWords)



# Add wordlist option
# Add single word option

fuzz("SLSRTC")

