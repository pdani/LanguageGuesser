from guess.sampletext import SampleText
from math import *

class Language(object):
    """Class for representing a language with its sampletext"""
    def __init__(self, filename):
        """Constructor"""
        
        # Creating the sampletext object
        self.sampleText = SampleText(filename=filename)
        
    def getProbability(self, phrase=None, sampletext=None):
        """
        Given a phrase string, or a SampleText instance, this method gives a
        value which is proportional with the probability of the fact, that
        the pharse is contained by this language
        """
        
        # String or sampletext
        if phrase is not None:
            phrase = SampleText(phrase=phrase)
        
        if sampletext is not None:
            phrase = sampletext
        
        # Initialization
        probability = 0.0
        
        # Walking through bigramms of the phrase
        for (bigramm, freq) in phrase.bigrammFreqs.iteritems():
            # If the bigramm can be found in the sampletext too, lets use its
            # probabilty-proportional value.
            if self.sampleText.probabilities.has_key(bigramm):
                probability += freq * log(self.sampleText.probabilities[bigramm])
        
        return probability
        