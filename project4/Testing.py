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

def printResults(results):
    print("MAX:     {}".format(max(results)))
    print("AVERAGE: {}".format(average(results)))
    print("STD:     {}".format(stDeviation(results)))

def q5():
    print("Q5")

    print("PENDATA")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    pen_results = []
    for i in range(5):
        pen_results.append(testPenData()[1])
    printResults(pen_results)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    print("CARDATA")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    car_results = []
    for i in range(5):
        car_results.append(testCarData()[1])
    printResults(car_results)

def q6():
    print("Q6")

    print("PENDATA")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for i in range(0, 41, 5):
        pen_results = []
        for _ in range(5):
            pen_results.append(testPenData()[1])
        print("PENDATA PERCEPTRON COUNT {}".format(i))
        printResults(pen_results)


    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("CARDATA")

    for i in range(0, 41, 5):
        car_results = []
        for _ in range(5):
            pen_results.append(testCarData()[1])
        print("CARDATA PEREPTRON COUNT {}".format(i))
        printResults(pen_results)
q6()
