import numpy as np
class Function:
    X=[]
    Y=[]
    Xm=[]
    Ym=[]
    Z=[]
    f=None
    lb=None
    ub=None
    def useF(self,x,y):
        return self.f(x,y)
class AckleyFunction(Function):
    def __init__(self):
        self.lb=-32.768
        self.ub= 32.768
        self.f=lambda x,y:-20.0 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2)))-np.exp(0.5 * (np.cos(2 * np.pi * x)+np.cos(2 * np.pi * y))) + np.e + 20
        xaxis = np.arange(self.lb, self.ub, 0.1)
        yaxis = np.arange(self.lb, self.ub, 0.1)
        self.X=xaxis
        self.Y=yaxis
        self.Xm, self.Ym = np.meshgrid(xaxis, yaxis)
        self.Z=self.f(self.Xm,self.Ym)


class ZakharovFunction(Function):
    def zakharov(self,x1,y):
        a= 0.5*x1+y
        b= x1*x1 +y*y +pow(a,2) +pow(a,4)
        return b
    def __init__(self):
        self.lb=-5
        self.ub= 10
        self.X = np.arange(-5, 10, 0.5)
        self.Y = np.arange(-5, 10, 0.5)
        self.Xm, self.Ym = np.meshgrid(self.X, self.Y)
        self.Z = self.zakharov(self.Xm,self.Ym)
    def useF(self,x,y):
        return self.zakharov(x,y)

class MichalewiczFunction(Function):
    def __init__(self):
        self.lb=0
        self.ub=np.pi
        self.f=lambda x,y: -1 * ( (np.sin(x) * np.sin((1 * x**2) / np.pi)**20) + (np.sin(y) * np.sin((2 * y**2) / np.pi)**20) )
        self.X = np.arange(0, np.pi, 0.1)
        self.Y = np.arange(0, np.pi, 0.1)
        self.Xm, self.Ym = np.meshgrid(self.X, self.Y)
        self.Z=self.f(self.Xm,self.Ym)
class LevyN13Function(Function):
    def __init__(self):
        self.f=lambda x,y: np.sin(3*np.pi*x)**2 + (x-1)**2*(1+np.sin(3*np.pi*y)*np.sin(3*np.pi*y))+ (y-1)*(y-1)*(1+np.sin(2*np.pi*y)*np.sin(2*np.pi*y))
        self.X = np.arange(-10, 10, 0.5)
        self.Y = np.arange(-10, 10, 0.5)
        self.Xm, self.Ym = np.meshgrid(self.X, self.Y)
        self.Z=self.f(self.Xm,self.Ym)
class LevyFunction(Function):
    def __init__(self):
        self.lb=-10
        self.ub= 10
        self.X = np.arange(-10, 10, 0.1)
        self.Y = np.arange(-10, 10, 0.1)
        self.Xm, self.Ym = np.meshgrid(self.X, self.Y)
        self.Z = np.zeros((len(self.X), len(self.Y)))
        for i in range(len(self.X)):
            for j in range(len(self.Y)):
                self.Z[i, j] = self.cZ(self.X[i], self.Y[j])
    def cZ(self,x,y):
        n = 2
        w = np.zeros(shape=[n])
        w[0] = 1 + ((x-1) / 4)
        w[1] = 1 + ((y-1) / 4)
        s = 0
        for i in range(n - 1):
            s += (w[i] - 1)**2 * (1 + 10 * np.sin(np.pi * w[i] + 1)**2)
        return np.sin(np.pi * w[0])**2 + s + (w[n - 1] - 1)**2 * (1 + np.sin(2 * np.pi * w[n - 1]))**2
    def useF(self,x,y):
        return self.cZ(x,y)
    
class GriewankFunction(Function):
    def __init__(self):
        self.lb=-600
        self.ub= 600
        self.f=lambda x,y: (x**2+y**2)/4000 -np.cos(x/np.sqrt(2))*np.cos(y/np.sqrt(3))+1
        self.X = np.arange(-600, 600, 0.5)
        self.Y = np.arange(-600, 600, 0.5)
        self.Xm, self.Ym = np.meshgrid(self.X, self.Y)
        self.Z=self.f(self.Xm,self.Ym)

class RastriginFunction(Function):
    def __init__(self):
        self.lb=-5.12
        self.ub= 5.12
        self.f=lambda x,y: 10 + x**2 - 10* np.cos(2 * np.pi * x)  +(y**2 - 10 * np.cos(2 * np.pi * y))
        self.X = np.arange(-5.12, 5.12, 0.5) 
        self.Y = np.arange(-5.12, 5.12, 0.5) 
        
        self.Xm, self.Ym = np.meshgrid(self.X, self.Y)
        self.Z = self.f(self.Xm, self.Ym)
       
    
class RosenbrockFunction(Function):
    def __init__(self):
        self.lb=-5
        self.ub= 10
        self.X = np.arange(-5, 10, 0.5)
        self.Y = np.arange(-5, 10, 0.5)
        self.Xm, self.Ym = np.meshgrid(self.X, self.Y)
        self.f = lambda x,y: 100*((x-1)**2 )+ (y-x**2)**2
        self.Z = self.f(self.Xm,self.Ym)
        
class SchwefelFunction(Function):
    def __init__(self):
        self.lb=-500
        self.ub= 500
        xaxis = np.arange(-500, 500, 1)
        yaxis = np.arange(-500, 500, 1)
        x, y = np.meshgrid(xaxis, yaxis)
        self.X=xaxis
        self.Y=yaxis
        self.Xm=x
        self.Ym=y
        self.Z =self.fitnessFunc(x,y)
        
    def fitnessFunc(self,x,y):
        return (418.9829 * 2 - (x * (np.sin(np.sqrt(np.abs(x)))) + (y * np.sin(np.sqrt(np.abs(y))))))
    def useF(self,x,y):
            return self.fitnessFunc(x,y)
class SphereFunction(Function):
    def __init__(self):
        self.lb=-5.12
        self.ub= 5.12
        self.X = np.arange(-5.12, 5.12, 0.25)
        self.Y = np.arange(-5.12, 5.12, 0.25)
        self.Xm, self.Ym = np.meshgrid(self.X, self.Y)
        self.Z = self.Xm**2 + self.Ym**2
    def useF(self,x,y):
        return x**2+y**2