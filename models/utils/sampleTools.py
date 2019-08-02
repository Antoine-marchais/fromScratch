import numpy as np
import numpy.random as rd

def getFolds(data,nFolds):
    """
    return a cross validation list of folds given a 
    dataset and the number of folds wanted
    """
    n = data.shape[0]
    nTest = n//nFolds
    nTrain = n-nTest
    folds = []
    for i in range(nFolds):
        testid = np.arange(nTest*i,nTest*(i+1))
        trainid = np.hstack((np.arange(0,nTest*i),np.arange(nTest*(i+1),n)))
        folds.append([trainid,testid])
    return folds

class RandomSet :
    """
    generate random data and the random target desired
    for fundamental testing of predictors
    """
    def __init__(self,nFeatures,nSamples,mean=0,variance=1):
        self.nFeatures = nFeatures
        self.nSamples = nSamples
        self.means=np.ones((nFeatures))*mean
        self.variances=np.ones((nFeatures))*variance
        self.createSet()

    def createSet(self):
        samples = 2*rd.random_sample((self.nSamples,self.nFeatures))-1
        samples = samples * self.variances
        self.set = samples + self.means
        

    def getSet(self):
        return self.set

    def setMeans(self,means):
        """
        set a vector of means for the sample distribution
        """
        self.means = np.array(means)
        self.createSet()

    def setVariances(self,variances):
        """
        set a vector of variance for the sample distribution
        """
        self.variances = np.array(variances)
        self.createSet()

    def getTargets(self,func,noise=1):
        """
        compute the targets of the samples with an additional
        gaussian noise
        """
        targets = np.zeros((self.nSamples))
        for i in range(self.nSamples):
            targets[i] = func(self.set[i])+noise*rd.normal()
        return targets


