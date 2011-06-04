#!/usr/bin/env pypy

import sys

from guess.language import Language, SampleText

def main():
    eng = Language('data/ep-01-en.test')
    ger = Language('data/ep-01-de.test')
    fra = Language('data/ep-01-fr.test')
    spa = Language('data/ep-01-es.test')
    
    if len(sys.argv) <= 1:
        while True:
            print "Puszi Reka :) >>> ",
            line = sys.stdin.readline()
            
            if not line:
                break
            
            phrase = SampleText(phrase=line)
            probs = {
                "English": eng.getProbability(sampletext=phrase),
                "German": ger.getProbability(sampletext=phrase),
                "French": fra.getProbability(sampletext=phrase),
                "Spanish": spa.getProbability(sampletext=phrase)
            }
    
            keys = probs.keys()
            keys.sort(key=probs.__getitem__, reverse=True)
        
            print "\rLanguage probabilities in descending order:"
        
            for key in keys:
                print "%s: %f" % (key, probs[key])

    else:
        phrase = SampleText(phrase=" ".join(sys.argv[1:]))
        probs = {
            "English": eng.getProbability(sampletext=phrase),
            "German": ger.getProbability(sampletext=phrase),
            "French": fra.getProbability(sampletext=phrase),
            "Spanish": spa.getProbability(sampletext=phrase)
        }

        keys = probs.keys()
        keys.sort(key=probs.__getitem__, reverse=True)
        
        print "Language probabilities in descending order:"
        
        for key in keys:
            print "%s: %f" % (key, probs[key])
    
if __name__ == "__main__":
    main()