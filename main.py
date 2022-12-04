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

y0 = [Am, mBR, mBA, mCLN, Cln, BR, BAm]

# Parameters
kd1_G = 0.1
kd2_G = 0.1
kR_G = 4.75
kAd_G = 0
kAm_G = 1
kp_G = 0.35
kgrowth_G = 0.02

# Model
def model_G(y, t):
  mCLNi = y[3]
  BRi = 
  


  f0 = -kd1_G*mCLNi
  f1 = kp_G*mCLNi*BR*A/V-kd2_G*Cln
  f2 = kgrowth_G*(kR_G/(kR_G+kAm_G+kAd_G))*mBR*BR*A/V
  f3 = kgrowth_G*(kAm_G/(kR_G+kAm_G+kAd_G))+mBA*BR*A/V
  f4 = kgrowth_G*(kAd_G/(kR_G+kAm_G+kAd_G))*mBR*BR*A/V
  return [f0,f1,f2,f3,f4]


# Simulation
t0 = 0
t_end = 351
dt = 1
t = np.arange(t0, t_end, dt)
sol = odeint(model_G, 0, t)
plt.plot(t, sol)
plt.show()