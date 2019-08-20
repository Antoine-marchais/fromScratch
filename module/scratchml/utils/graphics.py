import matplotlib.colors as col
import numpy as np

class Canvas :
    """
    a customfg canvas to draw ml related graphics
    """
    def __init__(self,ax,size=(200,300)):
        """
        the nboundos are set following the 
        [left,bottom,right,top]  notation,
        and the image is createds
        """
        self.ax = ax
        self.bounds = [ax.get_xlim()[0],ax.get_ylim()[0],ax.get_xlim()[1],ax.get_ylim()[1]]
        self.realWidth = self.bounds[2] - self.bounds[0]
        self.realHeight = self.bounds[3] - self.bounds[1]
        self.width = size[1]
        self.height = size[0]
        self.pixelWidth = self.realWidth/self.width
        self.pixelHeight = self.realHeight/self.height
        self.img =255* np.ones((size[0],size[1],3),dtype=np.uint8)

    def almostEqual(self,a,b,tol=None):
        """
        equality with margin for scalar values
        """
        if tol==None :
            tol=self.pixelWidth*1.5
        return (a>=b-tol and a<=b+tol)

    def getPixelAt(self,x,y):
        """
        returns the coordinates of the pixel coresponding
        to the given point
        """
        Bcoord = int((x-self.bounds[0])/self.realWidth*self.width)
        Acoord = int((self.bounds[3]-y)/self.realHeight*self.height)
        return np.array([min(Acoord,self.width-1),min(Bcoord,self.height-1)])

    def getPointAt(self,Acoord,Bcoord):
        """
        returns the geometrical point corespondisng to the
        given pixel
        """
        x = self.bounds[0]+Bcoord/self.width*self.realWidth+self.pixelWidth/2
        y = self.bounds[1]+(self.height-Acoord)/self.height*self.realHeight-self.pixelHeight/2
        return np.array([x,y])

    def fillIf(self,func,color="red"):
        """
        color all the points declared in tge correct region
        by the given function, use almostEqual in
        equations for curves
        """
        for i in range(self.height):
            for j in range(self.width):
                if func(self.getPointAt(i,j)):
                    self.img[i,j,::]=255*np.array(col.to_rgb(color),dtype=np.uint8)
        self.render()

    def render(self):
        """
        show the current image
        """
        extent = [self.bounds[0],self.bounds[2],self.bounds[1],self.bounds[3]]
        self.ax.imshow(self.img,interpolation="nearest",alpha=0.3,extent=extent)

