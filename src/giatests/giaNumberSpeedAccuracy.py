"""

GIA Number Speed Accuracy tests


sample three random integers (positive?)

order them and compute high-median and media-low
answer is the number that have max([high-median, media-low])


"""
import random



DIFF = 5
MINVAL = DIFF+10 #offset from 0
MAXVAL = 100 #exclusive


def compute(numbers):
    # solves the riddle
    numbers.sort()

    if numbers[2]-numbers[1] == numbers[1]-numbers[0]:
        return None
    elif numbers[2]-numbers[1] > numbers[1]-numbers[0]:
        return numbers[2]
    else:
        return numbers[0]


def makeTriplet():

    solution = None

    # the while avoid symmetry
    while not solution:
        # sample two numbers
        numbers = random.sample(range(MINVAL, MAXVAL), 2)

        # make the max number such as the diff is similar to median-min
        n = max(numbers) + abs(numbers[0]-numbers[1]) + random.randint(1, DIFF)*random.choice([-1,+1])
        numbers.append(n)
        # compute the solution (check if max-median == median-min)
        solution = compute(numbers)

    # shuffle
    random.shuffle(numbers)
    return numbers, str(solution)




def makeNumberSpeedAccuracyItem():

    numbers,solution = makeTriplet()

    return solution, {"numbers" : numbers}

if __name__ == '__main__':

    for _ in range(3):
        print(makeNumberSpeedAccuracyItem())
