import math
from math import sqrt, pi
import scipy
from scipy.stats import norm
import numpy as np


""" Defining the Normal Cumulative Density Function.
    The function N(z) returns the the cumulative density
    at the point z, under a normal curve """


def N(z):
    return norm.cdf(z)


""" For the functions defined below, we have:
    S : underlying price
    K : Strike Price
    r : rate
    t : time to expiration (in days)
    vol : volatility 
"""


def call_value(S, K, r, t, vol):

    d1 = (1.0/(vol * np.sqrt(t))) * (np.log(S/K) + (r + 0.5 * vol**2.0) * t)
    d2 = d1 - (vol * np.sqrt(t))

    return N(d1) * S - N(d2) * K * np.exp(-r * t)


def put_value(S, K, r, t, vol):

    d1 = (1.0/(vol * np.sqrt(t))) * (np.log(S/K) + (r + 0.5 * vol**2.0) * t)
    d2 = d1 - (vol * np.sqrt(t))

    return N(-d2) * K * np.exp(-r * t) - N(-d1) * S


""" Functions for Option Greeks """


def phi(x):
    """ Phi function (used for greeks)

    """
    return np.exp(-0.5 * x * x) / (sqrt(2.0 * pi))


def delta_call(S, K, r, t, vol):
    d1 = (1.0/(vol * np.sqrt(t))) * (np.log(S/K) + (r + 0.5 * vol**2.0) * t)

    return N(d1)


def delta_put(S, K, r, t, vol):
    d1 = (1.0/(vol * np.sqrt(t))) * (np.log(S/K) + (r + 0.5 * vol**2.0) * t)

    return N(d1) - 1.0


def gamma(S, K, r, t, vol):
    d1 = (1.0/(vol * np.sqrt(t))) * (np.log(S/K) + (r + 0.5 * vol**2.0) * t)

    return phi(d1) / (S * vol * sqrt(t))


def vega(S, K, r, t, vol):
    d1 = (1.0/(vol * np.sqrt(t))) * (np.log(S/K) + (r + 0.5 * vol**2.0) * t)

    return (S * phi(d1) * sqrt(t)) / 100.0


def theta_call(S, K, r, t, vol):
    d1 = (1.0/(vol * np.sqrt(t))) * (np.log(S/K) + (r + 0.5 * vol**2.0) * t)
    d2 = d1 - (vol * np.sqrt(t))

    theta = -((S * phi(d1) * vol) / (2.0 * np.sqrt(t))) - \
        (r * K * np.exp(-r * t) * N(d2))
    return theta / 365.0


def theta_put(S, K, r, t, vol):
    d1 = (1.0/(vol * np.sqrt(t))) * (np.log(S/K) + (r + 0.5 * vol**2.0) * t)
    d2 = d1 - (vol * np.sqrt(t))

    theta = -((S * phi(d1) * vol) / (2.0 * np.sqrt(t))) + \
        (r * K * np.exp(-r * t) * N(-d2))
    return theta / 365.0


def rho_call(S, K, r, t, vol):
    d1 = (1.0/(vol * np.sqrt(t))) * (np.log(S/K) + (r + 0.5 * vol**2.0) * t)
    d2 = d1 - (vol * np.sqrt(t))

    rho = K * t * np.exp(-r * t) * N(d2)
    return rho / 100.0


def rho_put(S, K, r, t, vol):
    d1 = (1.0/(vol * np.sqrt(t))) * (np.log(S/K) + (r + 0.5 * vol**2.0) * t)
    d2 = d1 - (vol * np.sqrt(t))

    rho = -K * t * np.exp(-r * t) * N(-d2)
    return rho / 100.0
