"""

GIA perceptual speed tests


print a row of 4 lower chars
print an identical row of same chars but as capitalized chars
select a random number between 0 and 4 of the chars
flip random number of chars to different chars

the answer is the number of same chars (lower,capitalized)

a b c d
A G S D

(a,A) and (d,D) are the same, so 2 chars



"""
import random
import string

NCHARS = 4

def makePerceptualSpeedItem():

    # how many chars are both lower and capitalized
    sameChar = random.randint(0,NCHARS)

    pos = set()

    # randomly set the positions in the list of the same chars
    while len(pos) < sameChar:
        pos.add(random.randint(0,NCHARS-1))

    # sample the chars - double the length of string
    chars = random.sample(string.ascii_lowercase,2*NCHARS)

    for i in range(NCHARS):
        # capitalized the second half and make the chars equal to the ones in pos
        if i in pos:
            chars[NCHARS+i] = chars[i].upper()
        else:
            chars[NCHARS+i] = chars[NCHARS+i].upper()

    firstrow = ''.join(chars[:NCHARS])
    secondrow = ''.join(chars[NCHARS:])


    return str(sameChar), {"firstrow" : firstrow,"secondrow" : secondrow}

if __name__ == '__main__':

    for _ in range(3):
        print(makePerceptualSpeedItem())
