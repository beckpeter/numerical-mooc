import numpy as np
from matplotlib import pyplot as plt

ms= 50#kg
g=9.81#m/s
rho=1.091 #kg/m^3
r=.5#m
A=np.pi*r**2
ve=325#m/s
Cd=.15#drag Coefficient


dt=.1#s
v0=0
h0=0
mp0=100#kg

h=[h0]
v=[v0]
t=[0]
mp=[mp0]

landed=False
while not landed:
    t.append(t[-1]+dt)
    dh=v[-1]*dt
    h.append(h[-1]+dh)
    
    mass_rocket=ms+mp[-1]
    if mp[-1]>0:
        mdot=20
    else:
        mdot=0
    mp.append(mp[-1]-mdot*dt)
    dv=-g*dt + mdot*ve/(mass_rocket)*dt - .5*rho*v[-1]*abs(v[-1])*A*Cd/(mass_rocket)*dt
    v.append(v[-1]+dv)
    

    if t[-1]>1:
        if h[-1] <= 0:
            landed = True
            
print(max(v))
print(t[v.index(max(v))])
print(h[v.index(max(v))])
print()
print(max(h))
print(t[h.index(max(h))])
print(t[-1])
print(v[-1])
'''
plt.plot(t,h,label='height')
plt.plot(t,v,label='velocity')
plt.legend()
plt.show()
'''





