from guess.word import Word

class SampleText(object):
    """Class for preprocessing a sample text, and calculating its properties"""
    def __init__(self, filename=None, phrase=None):
        """Constructor"""
        
        # Read file or string
        if filename is not None:
            self.text = open(filename, "r").read().decode('utf-8')
        else:
            self.text = phrase.decode('utf-8')
        
        # Initializing properties to None, must be calculated at first use
        self._bigrammFreqs = None
        self._unigrammFreqs = None
        self._words = None
        self._probs = None
    
    @property
    def words(self):
        """
        Returns a dictionary of words in sampletext, where keys are the words,
        and values are pairs in the form of (<word object>, frequency).
        """
        
        # Caching
        if self._words is not None:
            return self._words
        
        # Split text into words, and preprocess them (filter for alphanums,
        # make them lowercase)
        words = self.text.split()
        words = [filter(unicode.isalpha, word).lower() for word in words]
        
        # Filter out empty strings
        words = filter(lambda x: x != "", words)
        
        self._words = {}
        
        # Counting word frequencies, making word objects
        for word in words:
            if self._words.has_key(word):
                t = self._words[word]
                self._words[word] = (t[0], t[1] + 1)
            else:
                self._words[word] = (Word(word), 1)
        
        return self._words
    
    def _freqs(self, grammType='bigramm'):
        """
        Used by *Freqs methods. Calculates the freqencies of gramms in the
        sampletext. Returns with a dictionary, where the keys are the gramms,
        and the values are the frequencies.
        """
        # Getting the given attribute (self._bigrammFreqs
        # or self._unigrammFreqs)
        grammFreqs = self.__getattribute__('_%sFreqs' % grammType)
        
        # Caching
        if grammFreqs is not None:
            return grammFreqs
        
        grammFreqs = {}
        
        # Walking through words in sampletext
        for (word, (wordobj, num)) in self.words.iteritems():
            # Getting the given dicionary of wordobj (wordobj._bigrammFreqs
            # or wordobj._unigrammFreqs)
            freqs = wordobj.__getattribute__(grammType + 'Freqs')
            # Walking through gramms of the words, and sum the frequencies of
            # them in sampletext
            for (gramm, freq) in freqs.iteritems():
                if grammFreqs.has_key(gramm):
                    # Increase by the product of number of word and grammfreq in
                    # the word
                    grammFreqs[gramm] += num * freq
                else:
                    grammFreqs[gramm] = num * freq
        # Set the given attribute (self._bigrammFreqs or self._unigrammFreqs)
        self.__setattr__('_%sFreqs' % grammType, grammFreqs)
        return grammFreqs
    
    @property
    def bigrammFreqs(self):
        """Bigramm frequencies of the sampletext"""
        return self._freqs('bigramm')
    
    @property
    def unigrammFreqs(self):
        """Unigramm frequencies of the sampletext"""
        return self._freqs('unigramm')
                    
    @property
    def probabilities(self):
        """
        Based on a given formula, calculates a value for every bigramms in the
        sampletext which can be used to calculate the most probable language
        """
        
        # Caching
        if self._probs is not None:
            return self._probs
        
        self._probs = {}
        
        # Number of different characters in the text
        distinctChars = len(self.unigrammFreqs)
        
        # Walking through bigramms exist in the text
        for (bigramm, bifreq) in self.bigrammFreqs.iteritems():
            # Get the first character of the bigramm, and its frequency 
            unigramm = bigramm[0]
            unifreq = self.unigrammFreqs[unigramm]
            
            # The actual formula to calculate the value for the bigramm
            self._probs[bigramm] = (bifreq + 1.0) / (unifreq + distinctChars)

        return self._probs
