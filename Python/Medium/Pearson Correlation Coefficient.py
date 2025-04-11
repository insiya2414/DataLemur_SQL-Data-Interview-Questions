from math import sqrt

def corr(x, y):
  #Helper function to calculate the mean of a list
  def mean(u):
    return sum(u) / len(u)
  
    #Helper function to calculate the covariance of two lists
  def covar(u, v):
    p = [u[i] * v[i] for i in range(len(u))]
    return mean(p) - mean(u) * mean(v)
  
    #Helper function to calculate the Pearson Correlation Coefficient
  return covar(x, y) / sqrt(covar(x, x)) / sqrt(covar(y, y))