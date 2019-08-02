import numpy as np
from models.baseModels import BaseRegressor

class LinearRegressor(BaseRegressor):
    """
    warped implementation of a linear regression optimized using
    the least square method
    """
    def fit(self,X,Y):
        Xtr = np.hstack((np.ones((X.shape[0],1)),X))
        Ytr = Y.reshape((Y.size,1))
        inv = np.linalg.inv(Xtr.T.dot(Xtr))
        self.beta = inv.dot(Xtr.T).dot(Ytr)
        
    def predict(self,X):
        Xex = np.hstack((np.ones((X.shape[0],1)),X))
        return Xex.dot(self.beta)

