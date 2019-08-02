import numpy as np
from abc import ABC,abstractmethod
from utils import metrics as mts

class BaseRegressor(ABC):
    """
    base class for most regressors
    """
    @abstractmethod
    def fit(self,X,Y):
        pass
    
    @abstractmethod
    def predict(self,X):
        pass

    def getPerf(self,X,Y,cv_folds,metric="RMSE"):
        meanMetric = 0
        nfolds = 0
        for tr,ts in cv_folds:
            self.fit(X[tr],Y[tr])
            Ypred = self.predict(X[ts])
            meanMetric += mts.rmse(Ypred,Y[ts])
            nfolds += 1
        return meanMetric/nfolds
