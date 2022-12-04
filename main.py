import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# G1 Phase
IVG1 = {'kd1': 0.1, 'kR': 4.75, 'kAD': 0, 'Am': 1, 'mBR': 1, 'mBA': 1, 'mCLN': 0, 'Cln': 0}

# Initial conditions
Am = 1
mBR = 1
mBA = 1
mCLN = 0
Cln = 0
BR = 25
BAm = 8.5
BAd = 0

y0 = [mCLN, Cln, BR, BAm, BAd]

# Parameters
kd1_G = 0.1
kd2_G = 0.1
kR_G = 4.75
kAd_G = 0
kAm_G = 1
kp_G = 0.35
kgrowth_G = 0.02
kx = 1

A = 100

# Model
def model_G(y, t):
  mCLNi = y[0]
  Clni = y[1]
  BRi = y[2]
  BAmi = y[3]
  BAdi = y[4]



  f0 = -kd1_G*(mCLNi+1)
  f1 = kp_G*mCLNi*BRi*np.sqrt(A)-kd2_G*Clni
  f2 = kgrowth_G*(kR_G/(kR_G+kAm_G+kAd_G))*mBR*BRi*np.sqrt(A)
  f3 = kgrowth_G*(kAm_G/(kR_G+kAm_G+kAd_G))*mBA*BRi*np.sqrt(A)
  f4 = kgrowth_G*(kAd_G/(kR_G+kAm_G+kAd_G))*mBR*BRi*np.sqrt(A)
  return [f0,f1,f2,f3,f4]

# Area


# Simulation time
t0 = 0
t_end = 101
dt = 1
t = np.arange(t0, t_end, dt)

# Solving ODE
sol = odeint(model_G, y0, t)
mCLN = sol[:, 0]
Cln = sol[:,1]
BR = sol[:, 2]
BAm = sol[:, 3]
BAd = sol[:, 4]


# Plotting
plt.plot(t, Cln)
plt.show()