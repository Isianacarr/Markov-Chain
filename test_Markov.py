#test_Markov.py

import Markov as markov

def makeWordModel(filename):
    #Creates a Markov Model from words in filename
    infile = open(filename)
    model = markov.Markov()
    for line in infile:
        words = line.split()
        for w in words:
            print(w)
            model.add(w)
    infile.close()
    #Add a sentinel at the end of the text

    model.add(None)
    model.reset()
    return model

def generateWordChain(markov, n):
    #Generates up to n words of output from a model
    words = []

    for i in range(n):
        next = markov.randomNext()
        if next is None: break
        words.append(next)

    return " ".join(words)

