#!/usr/bin/env python

import sys

from guess.language import Language
from guess.sampletext import SampleText

def gen_results(st, eng, ger, fra, spa):
    probs = {
        "English": eng.getProbability(sampletext=st),
        "German": ger.getProbability(sampletext=st),
        "French": fra.getProbability(sampletext=st),
        "Spanish": spa.getProbability(sampletext=st)
    }

    keys = probs.keys()
    keys.sort(key=probs.__getitem__, reverse=True)

    print "\rLanguage probabilities in descending order:"

    for key in keys:
        print "%s: %f" % (key, probs[key])

def main():
    eng = Language('data/ep-01-en.test')
    ger = Language('data/ep-01-de.test')
    fra = Language('data/ep-01-fr.test')
    spa = Language('data/ep-01-es.test')
    
    if len(sys.argv) <= 1:
        while True:
            print ">>> ",
            line = sys.stdin.readline()
            
            if not line:
                break
            
            phrase = SampleText(phrase=line)
            gen_results(phrase, eng, ger, fra, spa)
    else:
        phrase = SampleText(phrase=" ".join(sys.argv[1:]))
        gen_results(phrase, eng, ger, fra, spa)

if __name__ == "__main__":
    main()
