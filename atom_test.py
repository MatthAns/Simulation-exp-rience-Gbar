import matplotlib.pyplot as plt
import numpy as np



class Atom():
    """docstring for Atom :
    Define an atome with a mass "m" an initial velicty "v0"
    an initial position "x0" and a gravitational constant "g"."""
    
    def __init__(self, x0, v0, m, g):
        self.m = m
        self.v0 = v0
        self.x0 = x0
        self.g = g

    def __repr__(self):
        return """Atom:

            position x0 = {0} m
            velocity v0 = {1} m/s
            mass = {2} kg
            """.format(self.x0,self.v0,self.m)

class FreeFall():
    """docstring for FreeFall :"""
    
    def __init__(self,TOF):
        self.TOF = TOF
        
    def trajectory(self,Atom):
        
        time = np.arange(0,self.TOF,0.01)
        position = - 1/2*Atom.g*time**2 - Atom.v0 * time + Atom.x0
        tr = np.array([time,position])
        return(tr)
        
H_bar = Atom(0, 10, 1e-29, 9.81)
print(H_bar)
T = FreeFall(1)
traj = T.trajectory(H_bar)

plt.figure(1)
plt.plot(traj[0],traj[1])
