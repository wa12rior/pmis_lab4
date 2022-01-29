import matplotlib.pyplot as plt
import numpy as np
import cmath as cm

# Definiujemy funkcje
def xt(t, d):
  w2=5/8
  c1 = 1
  c2 = 1
  return np.exp(t*(-d-cm.sqrt(d**2-w2))) * c1 + np.exp(t*(-d+cm.sqrt(d**2-w2))) * c2

domain=np.linspace(1, 100, 100)

y1 = []
y2 = []

d1=0.1
d2=0.2

for i in domain:
  y1.append(xt(i, d1).astype('float128'))
  y2.append(xt(i, d2).astype('float128'))

fig, ax = plt.subplots()

ax.plot(domain, y1)
ax.plot(domain, y2)

plt.legend(['d=0.1', 'd=0.2'])
plt.show()
