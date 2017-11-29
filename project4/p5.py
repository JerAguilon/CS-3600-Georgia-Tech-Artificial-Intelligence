# import sys
# from NeuralNetUtil import buildExamplesFromPenData, buildExamplesFromCarData
# from NeuralNet import buildNeuralNet
# from math import pow, sqrt

# def stats(data):
#     dataList = data[1]
#     mean = sum(dataList) / float(len(dataList))

#     _sqError = [pow((i - mean), 2) for i in dataList]
#     std = sqrt(sum(_sqError)/len(dataList))

#     minimum = min(dataList)
#     maximum = max(dataList)
#     return minimum, maximum, mean, std

# penData = buildExamplesFromPenData()
# carData = buildExamplesFromCarData()

# penResults = []
# carResults = []
# for i in range(5):
#     print("ITERATING")
#     penResult = buildNeuralNet(penData, maxItr = 200, hiddenLayerList = [24])
#     print(penResult)
#     penResults.append(penResult)


# penMin, penMax, penMean, penStd = stats(penResults)

# print("{} {} {} {}".format(penMin, penMax, penMean, penStd))

from NeuralNetUtil import buildExamplesFromCarData,buildExamplesFromPenData
from NeuralNet import buildNeuralNet
import cPickle
from math import pow, sqrt

def average(list):
    return sum(list)/float(len(list))

def stDeviation(list):
    mean = average(list)
    diffSq = [pow((val-mean),2) for val in list]
    return sqrt(sum(diffSq)/len(list))

penData = buildExamplesFromPenData()
def testPenData(hiddenLayers = [1]):
    return buildNeuralNet(penData,maxItr = 200, hiddenLayerList =  hiddenLayers)

carData = buildExamplesFromCarData()
def testCarData(hiddenLayers = [1]):
    return buildNeuralNet(carData,maxItr = 200,hiddenLayerList =  hiddenLayers)

def q5Test():
    print "Q5 Test\n"
    print "Now testing Pen Data\n"
    iteration = 0
    penDataList = []
    while iteration < 5:
        penNet, testAccuracy = testPenData()
        penDataList.append(testAccuracy)
        iteration += 1

    print "Max of the Pen Data is:", max(penDataList)
    print "Average of the Pen Data is:", average(penDataList)
    print "Standard Deviation of the Pen Data is:", stDeviation(penDataList)
    print "\n"

    print "Now testing Car Data\n"
    iteration = 0
    carDataList = []
    while iteration < 5:
        carNet, testAccuracy = testCarData()
        carDataList.append(testAccuracy)
        iteration += 1

    print "Max of the Car Data is:", max(carDataList)
    print "Average of the Car Data is:", average(carDataList)
    print "Standard Deviation of the Car Data is:", stDeviation(carDataList)
    print "\n"

q5Test()
