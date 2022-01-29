import matplotlib.pyplot as plt
import numpy as np
import cmath as cm

# Definiujemy funkcje
def xt(t, d):
  w2=5/8
  c1 = 1
  c2 = 1
  return np.exp(t*(-d-cm.sqrt(d**2-w2))) * c1 + np.exp(t*(-d+cm.sqrt(d**2-w2))) * c2

def dxt(t, d):
  w2=5/8
  c1 = 1
  c2 = 1
  return np.exp(t*(-d-cm.sqrt(d**2-w2))) * (-d-cm.sqrt(d**2-w2)) * c1 + np.exp(t*(-d+cm.sqrt(d**2-w2))) * (-d+cm.sqrt(d**2-w2)) * c2

domain= np.arange(0, 8*np.pi, np.pi/4)

d=0.1

fig, ax = plt.subplots()

x = []
dx = []

for i in domain:
  x.append(xt(i, d))
  dx.append(dxt(i, d))
  
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.plot(x, dx)

plt.show()
