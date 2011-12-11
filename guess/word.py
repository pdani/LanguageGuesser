class Word(object):
    """Class for representing a word, and extracting its relevant properties"""
    def __init__(self, word = ""):
        """Consturctor"""
        
        # Concatenating a $ before, and a @ after every word
        self._word = u"$%s@" % word
        self._length = len(self._word)
        
        # Initializing properties to None, needs to be calculated at first use
        self._bigrammFreqs = None
        self._unigrammFreqs = None
    
    @property
    def bigrammFreqs(self):
        """
        Calculates the frequencies of bigramms, returns a dictionary with the
        bigramms as keys, and the frequencies as values
        """
        
        # Caching
        if self._bigrammFreqs is not None:
            return self._bigrammFreqs
            
        self._bigrammFreqs = {}
        
        # Walking through every bigramms in the word
        for i in range(self._length - 1):
            # Getting the i-th bigramm
            bigramm = self._word[i:i+2]
            
            # Incrementing the corresponding frequency-counter by one
            if self._bigrammFreqs.has_key(bigramm):
                self._bigrammFreqs[bigramm] += 1
            else:
                self._bigrammFreqs[bigramm] = 1
        
        return self._bigrammFreqs
    
    @property
    def unigrammFreqs(self):
        """
        Calculates the frequencies of unigramms, returns a dictionary with the
        unigramms as keys, and the frequencies as values
        """
        
        # Caching
        if self._unigrammFreqs is not None:
            return self._unigrammFreqs
        
        # Counting characters (unigramms)
        self._unigrammFreqs = {}
        for char in self._word:
            if self._unigrammFreqs.has_key(char):
                self._unigrammFreqs[char] += 1
            else:
                self._unigrammFreqs[char] = 1
        
        return self._unigrammFreqs
        
