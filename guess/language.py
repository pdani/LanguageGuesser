from guess.sampletext import SampleText
from math import *

class Language(object):
    def __init__(self, filename):
        self.sampleText = SampleText(filename=filename)
        
    def getProbability(self, phrase=None, sampletext=None):
        if phrase is not None:
            phrase = SampleText(phrase=phrase)
        
        if sampletext is not None:
            phrase = sampletext
        
        probability = 0.0
        
        for (bigramm, freq) in phrase.bigrammFreqs.iteritems():
            if self.sampleText.probabilities.has_key(bigramm):
                probability += freq * log(self.sampleText.probabilities[bigramm])
        
        return probability
        