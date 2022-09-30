"""

Compute the score of the GIA test

It measures performance (and timing).
The performance requires a population to evaluate the percentile.

Just keep track of done/correct/one/score.
The score use the penalty system of the test.

"""

PENALTIES = {
    "Reasoning" : -1,
    "PerceptualSpeed" : -0.25,
    "NumberSpeedAccuracy" : -0.5,
    "SpatialVisualization" : -0.5,
    "WordMeaning" : -0.5
}

# rankings should be percentile
RANKINGS = {
    "Low" : 15,
    "Below Average" :34,
    "Average" : 65,
    "Above Average" : 85,
    "High" : 86
}

def make_score_dict():
    return {"done" : 0,
            "correct" : 0,
            "wrong" : 0,
            "score" : 0}

class Scorer():
    def __init__(self, numberOfItems):
        self.numberOfItems = numberOfItems
        self.results = {
                "Reasoning" : make_score_dict(),
                "PerceptualSpeed" : make_score_dict(),
                "NumberSpeedAccuracy" : make_score_dict(),
                "SpatialVisualization" : make_score_dict(),
                "WordMeaning" : make_score_dict()
            }
        self.score = 0

    def addScore(self, testName, result):
        self.results[testName]["done"] += 1
        if result:
            self.results[testName]["correct"] += 1
            self.results[testName]["score"] += 1
        else:
            self.results[testName]["wrong"] += 1
            self.results[testName]["score"] += PENALTIES[testName]

    def computeTotalScore(self):
        """
        The score should be a ranking percentile over the participants.
        Without stats we can compute a performance vs the max score achievable.
        """
        self.score = 0
        for k,v in self.results.items():
            self.score += (v["score"] / v["done"])
        self.score /= 5

    def getDetailedScore(self):
        return self.results

    def getTotalScore(self):
        return self.score