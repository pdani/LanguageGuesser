#!/usr/bin/env python

import sys

from guess.language import Language
from guess.sampletext import SampleText

def print_results(phrase, eng, ger, fra, spa):
    # Probability-proportional values of the phrase for given languages
    probs = {
        "English": eng.getProbability(sampletext=phrase),
        "German": ger.getProbability(sampletext=phrase),
        "French": fra.getProbability(sampletext=phrase),
        "Spanish": spa.getProbability(sampletext=phrase)
    }
    
    # Sort languages by their probability
    keys = probs.keys()
    keys.sort(key=probs.__getitem__, reverse=True)

    print "\rLanguage probabilities in descending order:"

    for key in keys:
        print "%s: %f" % (key, probs[key])

def main():
    # Loading language sample files
    eng = Language('data/ep-01-en.test')
    ger = Language('data/ep-01-de.test')
    fra = Language('data/ep-01-fr.test')
    spa = Language('data/ep-01-es.test')
    
    if len(sys.argv) <= 1:
        # Simple cmdline-based UI
        while True:
            try:
                line = raw_input(">>> ")
            except EOFError:
                break
            
            # Make statistics from entered line
            phrase = SampleText(phrase=line)
            # Print out results
            print_results(phrase, eng, ger, fra, spa)
    else:
        # Make statistics from phrase argument
        phrase = SampleText(phrase=" ".join(sys.argv[1:]))
        # Print out results
        print_results(phrase, eng, ger, fra, spa)

if __name__ == "__main__":
    main()
