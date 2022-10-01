"""

GIA Word Meaning tests

sample two synonyms and a word
find the outlier word


"""
import random
#from nltk.corpus import wordnet as wn
#import nltk
#nltk.download('wordnet')
#nltk.download('omw-1.4')


# the vocabulary is a list of couple of words. Similar words should be in the same tuple.
# Avoid having syns in different tuples
VOCABULARY = [("dog", "cat"), 
              ("good", "lovely"),
              ("car", "train"),
              ("person", "individual"),
              ("math", "history"),
              ("bad", "evil"),
              ("computer", "smartphone"),
              ("Windows", "Linux"),
              ("Tie Fighter", "X-Wing"),
              ("Mars", "Saturn")]


def makeWordMeaningItem():

    # pick two sets from the vocabulary
    set1, set2 = random.sample(VOCABULARY,2)

    # similar word is set1
    word1, word2 = set1
    # odd word from the other set
    word3 = random.choice(set2)

    # shuffle
    words = [word1, word2, word3]
    random.shuffle(words)

    return word3, {"words" : words}

if __name__ == '__main__':

    for _ in range(3):
        print(makeWordMeaningItem())