import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Initial conditions
mBR = 1
mBA = 1
mCLN = 0
Cln = 0
BR = 25
BAm = 8.5
BAd = 0
A0 = 25**(2/3)

y0 = [mCLN, Cln, BR, BAm, BAd]

# Parameters
kd1_G = 0.1
kd2_G = 0.1
kp_G = 0.35
kR_G = 4.75
kAd_G = 0
kAm_G = 1
kgrowth_G = 0.02 
kR_M = 2
kAd_M =  1
kAm_M =  0
kx = 1
kd2_M = 10


# Model
def A(BAm2):
    f = A0 + kx*BAm2
    return f

def model_G(t, y):
    mCLNi, Clni, BRi, BAmi, BAdi = y
    f0 = -kd1_G*(mCLNi + np.random.randint(0,2))
    f1 = kp_G*mCLNi*BRi*A(BAmi)-kd2_G*Clni
    f2 = kgrowth_G*(kR_G/(kR_G+kAm_G+kAd_G))*mBR*BRi*A(BAmi)
    f3 = kgrowth_G*(kAm_G/(kR_G+kAm_G+kAd_G))*mBA*BRi*A(BAmi)
    f4 = kgrowth_G*(kAd_G/(kR_G+kAm_G+kAd_G))*mBR*BRi*A(BAmi)
    return [f0,f1,f2,f3,f4]

# Area


# Simulation time
t0 = 0
t_end = 100
dt = 1000
t = np.linspace(t0, t_end, dt)

# Solving ODE
sol = solve_ivp(model_G,  [t0, t_end], y0)
mCLN, Cln, BR, BAm, BAd = sol.y


# Plotting
plt.plot(sol.t, mCLN, label = 'BR')
#plt.plot(t, BR, label = 'BAm')
plt.legend()
plt.show()