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
def testPenData(hiddenLayers = [24]):
    return buildNeuralNet(penData,maxItr = 200, hiddenLayerList =  hiddenLayers)

carData = buildExamplesFromCarData()
def testCarData(hiddenLayers = [16]):
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


def q6Test():
    #80 total neural networks ran
    print "Q6 Test"
    print "Now testing Pen Data\n"
    numPerceptrons = 0
    perceptronIncrement = 5
    while numPerceptrons <= 40:
        print "Now testing Pen Data with", numPerceptrons, "perceptrons\n"
        iteration = 0
        penDataList = []
        while iteration < 5:
            penNet, testAccuracy = testPenData(hiddenLayers=[numPerceptrons])
            penDataList.append(testAccuracy)
            iteration += 1
        print "The set of Pen Data with", numPerceptrons, "perceptrons"
        print "Max of the Pen Data is:", max(penDataList)
        print "Average of the Pen Data is:", average(penDataList)
        print "Standard Deviation of the Pen Data is:", stDeviation(penDataList)
        print "\n"
        numPerceptrons += perceptronIncrement

    print "Now testing Car Data\n"
    numPerceptrons = 0
    perceptronIncrement = 5
    while numPerceptrons <= 40:
        print "Now testing Car Data with", numPerceptrons, "perceptrons\n"
        iteration = 0
        carDataList = []
        while iteration < 5:
            penNet, testAccuracy = testCarData(hiddenLayers=[numPerceptrons])
            carDataList.append(testAccuracy)
            iteration += 1
        print "The set of Car Data with", numPerceptrons, "perceptrons"
        print "Max of the Car Data is:", max(carDataList)
        print "Average of the Car Data is: ", average(carDataList)
        print "Standard Deviation of the Car Data is: ", stDeviation(carDataList)
        print "\n"
        numPerceptrons += perceptronIncrement

"""
def q7Test():
    numPerceptrons = 0
    perceptronIncrement = 5
    while numPerceptrons <= 40:
        iteration = 0
        penDataList = []
        while iteration < 5:
            testAccuracy = numPerceptrons
            penDataList2.append(testAccuracy)
            iteration += 1
        print penDataList
        numPerceptrons += perceptronIncrement
"""

q6Test()
