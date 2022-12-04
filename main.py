import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Initial conditions
Am = 1
mBR = 1
mBA = 1
mCLN = 1
Cln = 0
BR = 25
BAm = 8.5
BAd = 0
A0 = 25**(2/3)

y0 = [mCLN, Cln, BR, BAm, BAd]

# Parameters
kd1_G = 0.1
kd2_G = 0.1
kR_G = 4.75 
kR_M = 2
kAd_G = 0
kAd_M =  1
kAm_G = 1
kAm_M =  0
kp_G = 0.35
kgrowth_G = 0.02
kx = 1
kd2_M = 10


# Model
def model_G(y, t):
  mCLNi = y[0]
  Clni = y[1]
  BRi = y[2]
  BAmi = y[3]
  BAdi = y[4]
  f0 = -kd1_G*(mCLNi)
  f1 = kp_G*mCLNi*BRi*np.sqrt(A0 + kx*BAm)-kd2_G*Clni
  f2 = kgrowth_G*(kR_G/(kR_G+kAm_G+kAd_G))*mBR*BRi*np.sqrt(A0 + kx*BAm)
  f3 = kgrowth_G*(kAm_G/(kR_G+kAm_G+kAd_G))+mBA*BRi*np.sqrt(A0 + kx*BAm)
  f4 = kgrowth_G*(kAd_G/(kR_G+kAm_G+kAd_G))*mBR*BRi*np.sqrt(A0 + kx*BAm)
  return [f0,f1,f2,f3,f4]

# Area


# Simulation time
t0 = 0
t_end = 100
dt = 1
t = np.arange(t0, t_end, dt)

# Solving ODE
sol = odeint(model_G, y0, t, rtol = 10**(-5), atol = 10**(-6), mxstep = 10**4)
mCLN = sol[:, 0]
Cln = sol[:,1]
BR = sol[:, 2]
BAm = sol[:, 3]
BAd = sol[:, 4]

# Plotting
plt.plot(t, mCLN, label = 'BR')
#plt.plot(t, BR, label = 'BAm')
plt.legend()
plt.show()