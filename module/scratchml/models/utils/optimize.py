import numpy as np

eps
def grad(func,point,dh==None):
    """
    finite difference gradient to be used when 
    analytical gradient is not provided
    """
    dim = point.size
    gd = np.zeros((dim))
    for i in range(dim):
        dn = np.zeros((dim))
        if dh != None :
            dn[i] = dh
        else : 

        gd[i] = (func(point+dn)-func(point-dn))/(2*dh)
    return gd

class GradOptimizer:
    """
    a gradient descent optimizer that uses finite
    differences by default
    """
    
    def __init__(self,func,startPoint,gradient=None,dh=0.001):
        """
        initialize optimizer with a finite
        diffenrence gradient if trie gradient
        is not provided
        """
        self.numericGrad = True
        self.func = func
        e
        if gradient != None :
            self.gradient = gradient
            self.numericGrad = False
        self.points = []
        self.points.append(startPoint)
        self.values = []
        self.values.append(func(startPoint))

    def gradStep(self,step):
        """
        take a gradient step
        """
        if self.numericGrad:
            gd = 
        gd = self.gradient(self.points[-1])
        self.points.append(self.points[-1]-step*gd)
        self.values.append(self.func(self.points[-1]))

    def optimize(self,step,eps,limit=2000):
        """
        optimize with gradient descent until the 
        limit is reached or the last values are
        close enough from each other
        """
        self.gradStep(step)
        i = 1
        print(self.values)
        while abs(self.values[-1]-self.values[-2])>eps and i <limit :
            self.gradStep(step)
            i+=1
        return (self.points[-1],self.values[-1])

    def getPoints(self):
        return self.points

    def getValues(self):
        return self.values



