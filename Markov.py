#Markov.py
#A Markov Model is a statistical technique for modeling systems that change over time
import random

class Markov(object):
    """A simple trigram Markov model. The current state is a sequence of
    the two words seen most recently. Initally, the state is (None, None),
    since no words have been seen. Scanning the model to go through the sequence
    of states: [(None,None), (None, 'The'), ('The', 'man'), ('man', 'ate'),
    ('ate', 'the'), ('the', 'pasta')]
    """
    def __init__(self):
        """post: creates an empty Markov model with  initial state ('None', 'None')"""
        self.model ={} #maps states to a list of words
        self.state = (None, None) #Last two words processed

    def add(self,word):
        """post: Adds word as a possible following word for current state of the
        Markov Model and sets state to incorporate word as most recently seen.

        ex: If state was ('the','man') and the word is 'ate', the 'ate' is added
        as a word that can follow '... the man' and the state is now ('man', 'ate')"""

        if self.state in self.model:#If we have an existing list of words for this state
            self.model[self.state].append(word) # Just add this new word
        else: # First occurance of this state
            self.model[self.state] = [word] #create a new list

        self._transition(word) #Transition to the next state given the next word

    def reset(self):
        """post: The model state is set to its initial (None, None) state.

        note: this does not change the transition information that has been learned
        so far (via add()), it just resets the state so that we can start adding
        transitions or making predictions for a 'fresh' sequence"""

        self.state = (None, None)

    def randomNext(self):


        lst = self.model[self.state]
        pick = random.choice(lst)
        self._transition(pick)
        return pick

    def _transition(self, next):
        #Help function to construct next state

        self.state = (self.state[1], next)
