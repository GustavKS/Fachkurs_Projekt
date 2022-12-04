import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# G1 Phase
IVG1 = {'kd1': 0.1, 'kR': 4.75, 'kAD': 0, 'Am': 1, 'mBR': 1, 'mBA': 1, 'mCLN': 0, 'Cln': 0}

# SG2 Phase
IVSG2 = {'kd1': 0.1, 'kR': 4.75, 'kAD': 0, 'Am': 1, 'mBR': 1, 'mBA': 1, 'mCLN': 0, 'Cln': 0}


def dmCLNdt(mCLN, t, kd1=IV['kd1']):
  dmCLNdt = -kd1*(mCLN+1)
  return dmCLNdt

t = np.arange(0,351,1)
sol = odeint(dmCLNdt, 0, t)
print(sol)
plt.plot(t, sol+1)
plt.show()