class Word(object):
    def __init__(self, word = ""):
        self._word = u"$%s@" % word
        self._length = len(self._word)
        self._bigrammFreqs = None
        self._unigrammFreqs = None
    
    @property
    def bigrammFreqs(self):
        if self._bigrammFreqs is not None:
            return self._bigrammFreqs
            
        self._bigrammFreqs = {}
        for i in range(self._length - 1):
            bigramm = self._word[i:i+2]
            if self._bigrammFreqs.has_key(bigramm):
                continue
            freq = 1
            for j in range(i + 1, self._length - 1):
                if bigramm == self._word[j:j+2]:
                    freq += 1
                    
            self._bigrammFreqs[bigramm] = freq
        
        return self._bigrammFreqs
    
    @property
    def unigrammFreqs(self):
        if self._unigrammFreqs is not None:
            return self._unigrammFreqs
        
        self._unigrammFreqs = {}
        for char in self._word:
            if self._unigrammFreqs.has_key(char):
                self._unigrammFreqs[char] += 1
            else:
                self._unigrammFreqs[char] = 1
        
        return self._unigrammFreqs
        
