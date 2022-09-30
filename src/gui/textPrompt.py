
import matplotlib.pyplot as plt
SHOWIMAGEPAUSESECS = 1

class GIAprompt():
    def __init__(self):
        pass

    def printWelcome(self):
        print("Welcome to the GIA test!")

    def printStartTest(self, name):
        print("Get ready to start the %s test!" % name)
        input("Press a key to start...")

    def printResult(self, result, detailedResult):
        print("Congratulation! You're overall score is %s" % result)
        print("More in details...")
        for testName,v in detailedResult.items():
            print("*"*40)
            print("%s Test" % testName)
            for k, val in v.items():
                print(k,val)


    def printReasoningStatement(self, item, name1, name2, adj1, adj2 = None):
        print(item % (name1, adj1, name2))
        input("Press ENTER...")
        if adj2:
            print("Who is %s?" % adj2)
        else:
            print("Who is %s?" % adj1)
        return input()

    def printReasoningResult(self,result):
        if result:
            print("OK!")
        else:
            print("KO!")

    def printPerceptualSpeedStatement(self,firstrow,secondrow):
        print("*" * 40)

        print(firstrow)
        print(secondrow)

        return input("How many same characters?\n")

    def printPerceptualSpeedResult(self,result):

        if result:
            print("OK!")
        else:
            print("KO!")

    def printNumberSpeedAccuracyStatement(self,numbers):
        print("*" * 40)
        numbers = [str(n) for n in numbers]
        print('  '.join(numbers))


        return input("Which number is farthest from the median?\n")

    def printNumberSpeedAccuracyResult(self,result):

        if result:
            print("OK!")
        else:
            print("KO!")

    def printSpatialVisualizationStatement(self, images):
        print("*" * 40)

        fig, axs = plt.subplots(2, len(images))

        for col, (original,modified) in enumerate(images):
            axs[0][col].imshow(original)
            axs[1][col].imshow(modified)

        plt.show(block=False)
        plt.pause(SHOWIMAGEPAUSESECS)
        
        answer = input("How many pairs (top/bottom) contain the same image? (mirror image excluded).\n")

        plt.close(fig)

        return answer

    def printSpatialVisualizationResult(self, result):

        if result:
            print("OK!")
        else:
            print("KO!")

    def printWordMeaningStatement(self,words):
        print("*" * 40)

        print('  '.join(words))


        return input("Which word is the odd one out?\n")

    def printWordMeaningResult(self,result):

        if result:
            print("OK!")
        else:
            print("KO!")