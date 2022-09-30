from giatests.giaNumberSpeedAccuracy import makeNumberSpeedAccuracyItem
from giatests.giaReasoning import makeReasoningItem
from giatests.giaWordMeaning import makeWordMeaningItem
from giatests.giaSpatialViasualization import makeSpatialVisualizationItem
from giatests.giaPerceptualSpeed import makePerceptualSpeedItem


class GIAtest():
    def __init__(self):
        self.result = None
        self.data = None

    def makeStatement(self, testName):
        if testName == "Reasoning":
            self.result, self.data = makeReasoningItem()
        elif testName == "PerceptualSpeed":
            self.result, self.data = makePerceptualSpeedItem()
        elif testName == "NumberSpeedAccuracy":
            self.result, self.data = makeNumberSpeedAccuracyItem()
        elif testName == "SpatialVisualization":
            self.result, self.data = makeSpatialVisualizationItem()
        elif testName == "WordMeaning":
            self.result, self.data = makeWordMeaningItem()
        else:
            raise ValueError
        return self.result, self.data



    def compareAnswer(self, answer):
        return self.result == answer
