from numpy import *  
import time  

def sigmoid(inX):
    return 1.0 / (1 + exp(-inX))  

def trainLogRegres(train_x, old_train_y, opts):
    # calculate training time  
    startTime = time.time()

    train_x = train_x/train_x.max()
    numSamples, numFeatures = shape(train_x)
    maxValue,minValue = old_train_y.max(), old_train_y.min()
    numValues = maxValue - minValue + 1
    alpha = opts['alpha']; maxIter = opts['maxIter']
    weights = zeros([numFeatures, numValues])
    weights = random.uniform(0.001,0.002,size=[numFeatures, numValues])

    train_y = zeros([numSamples,numValues])
    for i in range(numSamples):
        train_y[i][old_train_y[i]-minValue] = 1

    for k in range(maxIter):  
        output = sigmoid(train_x * weights)
        error = train_y - output
        weights = weights + alpha * train_x.transpose() * error

    print('Took %fs!' % (time.time() - startTime))  
    return weights  


def loadData():  
    train_x = []  
    train_y = []  
    fileIn = open('./data/attr.csv').readlines()
    for i in range(len(fileIn)):
        lineArr = fileIn[i].strip().split(',')
        train_x.append([1])
        for j in range(len(lineArr)-1):
            train_x[i].append(float(lineArr[j]))
        train_y.append(int(lineArr[-1]))
    return mat(train_x), mat(train_y).transpose()  
  
  
## step 1: load data  
print( "step 1: load data..."  )
train_x, train_y = loadData()
test_x = train_x; test_y = train_y  
## step 2: training...  
print( "step 2: training..."  )
opts = {'alpha': 0.0001, 'maxIter': 5000}  
optimalWeights = trainLogRegres(train_x, train_y, opts)
savetxt('./data/result.csv', optimalWeights, delimiter = ',')  


def testLogRegres(weights, test_x, test_y):
    numSamples, numFeatures = shape(test_x)
    minValue = test_y.min()
    matchCount = 0  
    for i in range(numSamples):
        predict_value = (test_x[i, :] * weights)
        predict = (argmax(predict_value))
        if int(predict)+minValue == int(test_y[i,0]):  
            matchCount += 1  
    accuracy = float(matchCount) / numSamples  
    return accuracy  
accuracy = testLogRegres(optimalWeights, test_x, test_y)
print(accuracy)

