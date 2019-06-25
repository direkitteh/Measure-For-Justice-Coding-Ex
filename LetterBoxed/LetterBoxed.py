# Laura Durant
# Measures For Justice Coding Eval
# Letter Boxed
# 4/22/19

import io
import re

def readFile(filename):
    file = open(filename, 'r')
    return file.read()

def clean(word):
    # may as well replace anything that isn't a letter
    # I'm assuming non-letters aren't disqualifying
    # in theory someone could put 1337 5p34k but that's cheating
    return re.sub("[^a-zA-Z]", '', word).lower()

def disqualifyEdges(word, sides):
    word = clean(word)
    for adj in sides:
        # check if any letters are incorrectly next to each other
        # by the way, I tried "["+adj+"]{2+}" first but it seemed buggy
        if re.search("["+adj+"]["+adj+"]", word, flags=re.IGNORECASE) is not None:
            return True
    return False

def removePhrases(words):
    ret = words.copy()
    for word in words:
        if ' ' in word:
            ret.remove(word)
    return ret

def solve(puz, dictionary):
    # I'm assuming the puzzle is valid. If untrustworthy, check here.
    
    words = str.split(dictionary, '\n')
    # if phrases aren't allowed, uncomment this line
    #words = removePhrases(words)
    
    passedWords = []
    sides = str.split(puz, ",")
    chars = puz.replace(',','')
    for i in range(len(words)):
        if i >= len(words):
            # this means we removed words
            return
        word = words[i]
        cleaned = clean(word)
        if len(cleaned) < 3:
            continue
        if re.search("[^" + chars + "]", cleaned, flags=re.IGNORECASE) is not None:
            continue
        if disqualifyEdges(cleaned, sides):
            continue
        # important to check previous words bc of shared letter req
        for secondWord in words[i:] + passedWords:
            secondCleaned = clean(secondWord)
            if len(secondCleaned) < 3:
                continue
            letters = set(cleaned + secondCleaned)
            if len(letters) < 9:
                continue
            # would splitting out the shared letter req improve speed?
            if re.match("^" + cleaned[-1] + "[" + chars + "]*$", secondCleaned, flags=re.IGNORECASE) is None:
                # if the overlap is correct, 2nd word has unusable chars
                # don't revisit words unnecessarily
                if secondCleaned[0] is cleaned[-1] and secondWord not in passedWords:
                    words.remove(secondWord)
                continue
            if disqualifyEdges(secondCleaned, sides):
                continue
            # could change the output here to send it to a file instead
            print(word,secondWord,sep=", ")
        # remember to revisit valid words
        passedWords += [word]

# for fun, you could change these two lines to take & validate user input
dictFile = 'words.txt'
puzzle = 'RME,WCL,KGT,IPA'
solve(puzzle, readFile(dictFile))
