import matplotlib.pyplot as plt
from numpy import random
from scipy.stats import norm, uniform

from peiplib.mcmc import logpdf, mh_sample, rwmh_sample


delta = 0.5
nsample = 15000
mstart = 1


def loglikelihood(x):
    return logpdf(norm.pdf(x))


def logprior(x):
    return 0.


def proprnd(x):
    return x + random.rand(x.size)*2*delta - delta


def logprop(x, y):
    return logpdf(uniform.pdf(y-x, -delta, delta))


# samples, accrate, _ = mh_sample(
#     mstart, nsample, loglikelihood, logprior, proprnd, symmetric=True)

samples, accrate, mmap = rwmh_sample(
    mstart, nsample, loglikelihood, logprior, delta, proprnd_type='uniform')

print accrate, mmap

(mu, sigma) = norm.fit(samples)

n, bins, patches = plt.hist(
    samples, 50, normed=1, facecolor='green', alpha=0.75, edgecolor='k')

y = norm.pdf(bins, mu, sigma)
plt.plot(bins, y, 'r--', linewidth=3)

plt.show()
