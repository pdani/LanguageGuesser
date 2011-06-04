from guess.word import Word

class SampleText(object):
    def __init__(self, filename=None, phrase=None):
        if filename is not None:
            self.text = open(filename, "r").read().decode('utf-8')
        else:
            self.text = phrase.decode('utf-8')
        self._bigrammFreqs = None
        self._unigrammFreqs = None
        self._words = None
        self._probs = None
    
    @property
    def words(self):
        if self._words is not None:
            return self._words
        
        words = self.text.split()
        words = [filter(unicode.isalpha, word) for word in words]
        words = filter(lambda x: x != "", words)
        
        self._words = {}
        
        for word in words:
            if self._words.has_key(word):
                t = self._words[word]
                self._words[word] = (t[0], t[1] + 1)
            else:
                self._words[word] = (Word(word), 1)
        
        return self._words
    
    def _freqs(self, grammType='bigramm'):
        grammFreqs = self.__getattribute__('_%sFreqs' % grammType)
        if grammFreqs is not None:
            return grammFreqs
        
        grammFreqs = {}
        
        for (word, (wordobj, num)) in self.words.iteritems():
            freqs = wordobj.__getattribute__(grammType + 'Freqs')
            for (gramm, freq) in freqs.iteritems():
                if grammFreqs.has_key(gramm):
                    grammFreqs[gramm] += num * freq
                else:
                    grammFreqs[gramm] = num * freq
        return grammFreqs
        
    
    @property
    def bigrammFreqs(self):
        return self._freqs('bigramm')
    
    @property
    def unigrammFreqs(self):
        return self._freqs('unigramm')
                    
    @property
    def probabilities(self):
        if self._probs is not None:
            return self._probs
        
        self._probs = {}
        distinctChars = len(self.unigrammFreqs)
        for (bigramm, bifreq) in self.bigrammFreqs.iteritems():
            unigramm = bigramm[0]
            unifreq = self.unigrammFreqs[unigramm]
            
            prob = (bifreq + 1.0) / (unifreq + distinctChars)
            
            self._probs[bigramm] = prob

        return self._probs
        