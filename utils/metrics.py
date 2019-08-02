import numpy as np

def rmse(actual,expected):
    n = actual.size
    rss = np.sum((actual-expected)**2)
    return(np.sqrt(rss/n))
