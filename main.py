import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# G1 Phase
IV = {'kd1': 0.1, 'kR': 4.75, 'kAD': 0, 'Am': 1, 'mBR': 1, 'mBA': 1, 'mCLN': 0, 'Cln': 0}

def dmCLNdt(kd1, mCLN):
  f = -kd1*(mCLN+np.random.randint(0,2))
  return f