class ODE():
  def __init__(self, kd1, kR, kAd, Am, mBR, mBA, mCLN, Cln, A):
    # Values in G1 Phase
    self.kd1 = kd1
    self.kR = kR
    self.kAd = kAd
    self.Am = Am
    self.mBR = mBR
    self.mBA = mBA
    self.mCLN = mCLN
    self.Cln = Cln
    self.A = 2.0

  def fmCLN():
    fmCLN = 2
    return fmCLN

  def dmCLN(self):
    -self.kd1G*2*2
  
  def V(self):
    V = self.A**(3/2)
    return V