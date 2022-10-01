"""

GIA reasoning tests

There is a sentence such as "A is better than B".
Then the sentence disappear and there is a question about A and B.

We sample two names and an adjective.
Then we make the sentence like:
sentence = "A is %s than B" % adj
sentence = "A is as not as %s than B?" % adj

Finally we ask the question:
question = "Who is %s?" % invadj or adj
question = "Who is %s?" % invadj


"""
import random

# some names
NAMES = ["Han", "Leia", "Luke","Anakin", "Obi"]

# some adj and the opposite
ADJ = [("heavier", "lighter"),
       ("happier", "sadder"),
       ("smarter", "duller"),
       ("faster", "slower"),
       ("bigger", "smaller"),
       ("meaner", "kinder"),
       ("quicker", "slower"),
       ("more beautiful", "less beautiful"),
       ("more interesting", "less interesting")
       ]

# The template of the sentences. The boolean helps to manage the "as not as" form.
ITEM = [
    ("%s is %s than %s",True),
    ("%s is as not as %s than %s?",False)
]



def makeReasoningItem():

    # pick two names
    name1, name2 = random.sample(NAMES,2)

    # sample an adj
    adj = random.choice(ADJ)
    # pick the item
    item, straight = random.choice(ITEM)

    # randomly choose if to use or not the antonym adjective in the question
    if random.random() > 0.5:

        if straight:
            return name1, {"item" : item, "name1" : name1, "name2" : name2, "adj1" : adj[0], "adj2" : None}
        else:
            return name2, {"item": item, "name1": name1, "name2": name2, "adj1": adj[0], "adj2": None}

    else:

        if straight:
            return name2, {"item": item, "name1": name1, "name2": name2, "adj1": adj[0], "adj2": adj[1]}
        else:
            return name1, {"item": item, "name1": name1, "name2": name2, "adj1": adj[0], "adj2": adj[1]}


if __name__ == '__main__':

    for _ in range(3):
        print(makeReasoningItem())
