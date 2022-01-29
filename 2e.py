import matplotlib.pyplot as plt
import numpy as np
import cmath as cm

# Definiujemy funkcje
def xt(t):
  d=0.1
  w2=5/8
  c1 = 1
  c2 = 1
  return np.exp(t*(-d-cm.sqrt(d**2-w2))) * c1 + np.exp(t*(-d+cm.sqrt(d**2-w2))) * c2

domain=np.linspace(1, 100, 100)

y = []

for i in domain:
  y.append(xt(i).astype('float128'))

fig, ax = plt.subplots()

ax.plot(domain, y)

plt.legend(['oscylacja'])
plt.show()
