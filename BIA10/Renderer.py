import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3



class Render:
        running=True
        def on_close(self,ev):
            self.running = False
        def runanim(self,draw,vysl):
            vysledek=vysl
            minima=draw
            self.running=True
            
            fig = plt.figure()
            fig.canvas.mpl_connect('close_event', self.on_close)
 
            ax = plt.axes(projection='3d')
            plt.ion()
            ax.plot_surface(vysledek.Ym, vysledek.Xm, vysledek.Z, alpha=0.8, cmap='RdGy')
            while(self.running):
                points = []
                for min in minima: 
                        if (len(points)>0):
                            for i in range(0,len(points)):
                                points[i].remove()
                            points=[]
                        for j in min:
                           point = ax.scatter(j[1], j[0], vysledek.useF(j[0],j[1]), color="blue", alpha=0.9,marker='o', s=50)
                           points.append(point)
                        plt.pause(0.0000001) 
                        if(not self.running):
                            break
                if (len(points)>0):
                            for i in range(0,len(points)):
                                points[i].remove()
                            points=[]
                            
            plt.show(block=True)
        def show(self,cities,best_paths):
            self.running=True
            fig = plt.figure()
            fig.canvas.mpl_connect('close_event', self.on_close)
            x=[]
            y=[]
            for z in cities:
                x.append(z.pos_x)
                y.append(z.pos_y)
            start_pos=[]
            end_pos=[]
            ax = plt.plot(x,y,'ro')
            plt.ion()
            ptt=None
            pt=None
            while(self.running):
                ct=0
                for i in best_paths:
                    if(not self.running):
                        break
                    if(pt):
                        start_pos=[]
                        end_pos=[]
                        pt.remove()
                    for j in i.cities:
                        start_pos.append(j.pos_x)
                        end_pos.append(j.pos_y)
                        
                    print("gen"+str(ct)+":"+str(i.route))  
                    fig.suptitle("gen"+str(ct)+":"+str(i.route))
                    pt,=plt.plot(start_pos,end_pos)
                    
                    plt.pause(0.001)
                    ct+=1
