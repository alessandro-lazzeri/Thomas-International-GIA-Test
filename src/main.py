
from gui.textPrompt import GIAprompt
from giatests.scorer import Scorer
from giatests.giaTest import GIAtest

NUMBER_OF_QUESTION_PER_TEST = 2

if __name__ == '__main__':
    giatest = GIAtest()
    gui = GIAprompt()
    scorer = Scorer(NUMBER_OF_QUESTION_PER_TEST)

    gui.printWelcome()

    gui.printStartTest("Number Speed Accuracy")
    for _ in range(NUMBER_OF_QUESTION_PER_TEST):
        res, data = giatest.makeStatement("NumberSpeedAccuracy")
        answer = gui.printNumberSpeedAccuracyStatement(**data)
        res = giatest.compareAnswer(answer)
        scorer.addScore("NumberSpeedAccuracy",res)

    gui.printStartTest("Reasoning")
    for _ in range(NUMBER_OF_QUESTION_PER_TEST):
        res, data = giatest.makeStatement("Reasoning")
        answer = gui.printReasoningStatement(**data)
        res = giatest.compareAnswer(answer)
        scorer.addScore("Reasoning", res)

    gui.printStartTest("Word Meaning")
    for _ in range(NUMBER_OF_QUESTION_PER_TEST):
        res, data = giatest.makeStatement("WordMeaning")
        answer = gui.printWordMeaningStatement(**data)
        res = giatest.compareAnswer(answer)
        scorer.addScore("WordMeaning", res)

    gui.printStartTest("Spatial Visualization")
    for _ in range(NUMBER_OF_QUESTION_PER_TEST):
        res, data = giatest.makeStatement("SpatialVisualization")
        answer = gui.printSpatialVisualizationStatement(**data)
        res = giatest.compareAnswer(answer)
        scorer.addScore("SpatialVisualization", res)

    gui.printStartTest("Perceptual Speed")
    for _ in range(NUMBER_OF_QUESTION_PER_TEST):
        res, data = giatest.makeStatement("PerceptualSpeed")
        answer = gui.printPerceptualSpeedStatement(**data)
        res = giatest.compareAnswer(answer)
        scorer.addScore("PerceptualSpeed", res)

    scorer.computeTotalScore()

    gui.printResult(scorer.getTotalScore(), scorer.getDetailedScore())
