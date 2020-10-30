# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 11:38:09 2020

@author: kb424
"""
from scipy.special import erf 


# Define functions:

def KPMO3(Ro, mu1, mu2, sig1, sig2, v1, v2, v3):
    '''
    Tim Pritchard's Three stage kerogen model
    
    Inputs:
    Ro = maturity indicator, typically vitrinite reflectance. Discrete or array
    mu1, mu2 = mean of each normal distribution for state. It is suggested that
    this is calibrated using experimental data or empirical trends. Discrete
    sig1, sig2 = the standard deviation of the normal distribution for each
    state. Discrete
    v1,v2,v3 = the value of the desired property for each state. Discrete
    
    Outputs:
    kpmo_val = the value of the property as a function of Ro. If the input is
    discrete a single value is returned, if an array is supplied an array is 
    output. 
    '''
    cdf2 = 0.5 * (1 + erf((Ro-mu1)/((2**0.5)*sig1)))
    cdf3 = 0.5 * (1 + erf((Ro-mu2)/((2**0.5)*sig2)))
    P1 = 1.0 - cdf2
    P2 = cdf2 * (1.0-cdf3)
    P3 = cdf3
    kpmo_val = (P1*v1)+(P2*v2)+(P3*v3)
    return kpmo_val

def KPMO5(Ro, mu1, mu2, mu3, mu4, mu5, sig1, sig2, sig3, sig4, sig5, v1, v2, v3, v4, v5):
    '''
    As above but for 5 states:
    Immature - Mature - Pyrobitumen - Coke - Graphite
    '''
    cdf1 = .5 * (1. + erf((Ro-mu1)/((2.**.5)*sig1)))
    cdf2 = .5 * (1. + erf((Ro-mu2)/((2.**.5)*sig2)))
    cdf3 = .5 * (1. + erf((Ro-mu3)/((2.**.5)*sig3)))
    cdf4 = .5 * (1. + erf((Ro-mu4)/((2.**.5)*sig4)))
    cdf5 = .5 * (1. + erf((Ro-mu5)/((2.**.5)*sig5)))
    p1 = 1. - cdf1
    p2 = cdf1 * (1. - cdf2) * (1. - cdf3) * (1. - cdf3) * (1. - cdf4) * (1. - cdf5)
    p3 = cdf2 * (1. - cdf3) * (1. - cdf4) * (1. - cdf5)
    p4 = cdf3 * (1. - cdf4) * (1. - cdf5)
    p5 = 1. - (p1+p2+p3+p4)
    kpmo_val = (p1*v1)+(p2*v2)+(p3*v3)+(p4*v4)+(p5*v5)
    return kpmo_val



