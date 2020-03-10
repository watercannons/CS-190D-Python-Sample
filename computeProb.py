import numpy as np
from scipy.special import comb

def compute_prob(nTrials, numObserved):
  res = comb(nTrials, numObserved) * (0.5**numObserved) * (0.5**(nTrials - numObserved))
  return res

print(compute_prob(30,22))
