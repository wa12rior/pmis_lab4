import matplotlib.pyplot as plt
import numpy as np
import cmath as cm

# Definiujemy funkcje
def xt(t, d, omega):
  w2=5/8
  o = omega
  c1 = 1
  c2 = 1
  
  return np.exp(t*(-d-cm.sqrt(d**2-w2))) * c1 + np.exp(t*(-d+cm.sqrt(d**2-w2))) * c2 + (2*d*o*np.cos(o*t)+o**2*np.sin(o*t)-w2*np.sin(o*t))/((2*d**2+o**2-w2+2*d*cm.sqrt(d**2-w2))*(-2*d**2-o**2+w2+2*d*cm.sqrt(d**2-w2)))

domain= np.linspace(1, 100, 10000)

d=0

omega1 = 0.5
omega2 = 1
omega3 = 2

fig, ax = plt.subplots()

y1 = []
y2 = []
y3 = []

for i in domain:
  y1.append(xt(i, d, omega1))
  y2.append(xt(i, d, omega2))
  y3.append(xt(i, d, omega3))
  
f = plt.figure()
f.set_figwidth(400)
f.set_figheight(100)

ax.axhline(y=0, color='k')
ax.plot(domain, y1)
ax.plot(domain, y2)
ax.plot(domain, y3)

ax.legend(['omega=0.5', 'omega=1', 'omega=2'], loc="lower right")

plt.show()
