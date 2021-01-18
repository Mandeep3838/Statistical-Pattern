import numpy
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.integrate import quad
import math

'''
    Normal Distribution Function
'''

def pdf_fun(feet, mu, sig):
    return (1/(sig*numpy.sqrt(2*numpy.pi)))*numpy.exp((-1/2)*((feet-mu)/sig)**2)


'''
    Using Bayesian Method find point of split
    i.e, P_0 * f_0 = P_1 * f_1 (Using standard notations)
    sig_0 = sig_1 = 1 (given)
''' 
def split_point(mu_1, mu_0, p_1, p_0):
    return (((mu_1**2 - mu_0**2)/2) + numpy.log(p_0/p_1)) / (mu_1 - mu_0) 

'''
    Find posterior Probability
'''
def posterior(feet, mu_1, mu_0, sig_1, sig_0, p_1, p_0):
    return (p_1 * pdf_fun(feet, mu_1, sig_1)) / ((p_0 * pdf_fun(feet, mu_0, sig_0)) + (p_1 * pdf_fun(feet, mu_1, sig_1)))

'''
    Integrable function for calculating error
'''
def integrable(x, mu, sig):
    return pdf_fun(x, mu, sig)


## Ist case

'''
    Given Data part a
'''
prior_male_a = 0.5
prior_female_a = 0.5
dist_mu_male_a = 5.8 
dist_sg_male_a = 1
dist_mu_female_a = 5.0
dist_sg_female_a = 1

# Prior Probabilities
print("Prior Probability of male_a", prior_male_a)
print("Prior Probability of Female_a", prior_female_a)

fig, axs = plt.subplots(2,3, figsize=(12,10), constrained_layout=True)
fig.suptitle("Plots")

# Plot for Conditional Densities

x_male_a = numpy.linspace(1, 10, 100)
axs[0,0].plot(x_male_a, pdf_fun(x_male_a, dist_mu_male_a, dist_sg_male_a), label="male_a")

x_female_a = numpy.linspace(1, 10, 100)
axs[0,0].plot(x_female_a, pdf_fun(x_female_a, dist_mu_female_a, dist_sg_female_a), label="female_a")

axs[0,0].set_xlabel("height")
axs[0,0].set_ylabel("Densities")
axs[0,0].set_title("Density Distribution part a")

bayesian_classification_point_a = split_point(dist_mu_male_a, dist_mu_female_a, prior_male_a, prior_female_a)

axs[0,1].plot(x_male_a, posterior(x_male_a, dist_mu_male_a, dist_mu_female_a, dist_sg_male_a, dist_sg_female_a, prior_male_a, prior_female_a), label="male_a_posterior")

'''
    Interchanging values to use the same function
'''
axs[0,1].plot(x_female_a, posterior(x_female_a, dist_mu_female_a, dist_mu_male_a, dist_sg_female_a, dist_sg_male_a, prior_female_a, prior_male_a), label="female_a_posterior")

axs[0,1].axvline(x=bayesian_classification_point_a, label="decision boundary", color="olive")

axs[0,1].set_xlabel("height")
axs[0,1].set_ylabel("probability")
axs[0,1].set_title("Posterior Probability part a")

'''
    Misclassification Error
'''

error_a =  prior_female_a * quad(integrable, bayesian_classification_point_a, numpy.inf, args=(dist_mu_female_a, dist_sg_female_a))[0] \
            + prior_male_a * quad(integrable, -numpy.inf, bayesian_classification_point_a, args=(dist_mu_male_a, dist_sg_female_a))[0]

print("Misclassification Error in part a ", error_a)

# Combine plots

axs[0,2].plot(x_male_a, pdf_fun(x_male_a, dist_mu_male_a, dist_sg_male_a), label="male_a")
axs[0,2].plot(x_female_a, pdf_fun(x_female_a, dist_mu_female_a, dist_sg_female_a), label="female_a")

axs[0,2].plot(x_male_a, posterior(x_male_a, dist_mu_male_a, dist_mu_female_a, dist_sg_male_a, dist_sg_female_a, prior_male_a, prior_female_a), label="male_a_posterior")
axs[0,2].plot(x_female_a, posterior(x_female_a, dist_mu_female_a, dist_mu_male_a, dist_sg_female_a, dist_sg_male_a, prior_female_a, prior_male_a), label="female_a_posterior")
axs[0,2].axvline(x=bayesian_classification_point_a, label="decision boundary", color="olive")
axs[0,2].set_title("Combine Plots part a")

## IInd case

'''
    Given Data part b
'''
prior_male_b = 0.1
prior_female_b = 0.9
dist_mu_male_b = 5.8 
dist_sg_male_b = 1
dist_mu_female_b = 5.0
dist_sg_female_b = 1

# Prior Probabilities
print("Prior Probability of male_b", prior_male_b)
print("Prior Probability of Female_b", prior_female_b)

# Plot for Conditional Densities

x_male_b = numpy.linspace(1, 10, 100)
axs[1,0].plot(x_male_b, pdf_fun(x_male_b, dist_mu_male_b, dist_sg_male_b), label="male_b")

x_female_b = numpy.linspace(1, 10, 100)
axs[1,0].plot(x_female_b, pdf_fun(x_female_b, dist_mu_female_b, dist_sg_female_b), label="female_b")

axs[1,0].set_xlabel("height")
axs[1,0].set_ylabel("Densities")
axs[1,0].set_title("Density Distribution part b")
axs[1,1]
bayesian_classification_point_b = split_point(dist_mu_male_b, dist_mu_female_b, prior_male_b, prior_female_b)

axs[1,1].plot(x_male_b, posterior(x_male_b, dist_mu_male_b, dist_mu_female_b, dist_sg_male_b, dist_sg_female_b, prior_male_b, prior_female_b), label="male_b_posterior")

'''
    Interchanging values to use the same function
'''
axs[1,1].plot(x_female_b, posterior(x_female_b, dist_mu_female_b, dist_mu_male_b, dist_sg_female_b, dist_sg_male_b, prior_female_b, prior_male_b), label="female_b_posterior")
axs[1,1].axvline(x=bayesian_classification_point_b, label="decision boundary", color="olive")

axs[1,1].set_xlabel("height")
axs[1,1].set_ylabel("probability")
axs[1,1].set_title("Posterior Probability part b")

'''
    Misclassification Error
'''

error_b =  prior_female_b * quad(integrable, bayesian_classification_point_b, numpy.inf, args=(dist_mu_female_b, dist_sg_female_b))[0] \
            + prior_male_b * quad(integrable, -numpy.inf, bayesian_classification_point_b, args=(dist_mu_male_b, dist_sg_female_b))[0]

print("Misclassification Error in part b ", error_b)

# Combine plots

axs[1,2].plot(x_male_b, pdf_fun(x_male_b, dist_mu_male_b, dist_sg_male_b), label="male_b")
axs[1,2].plot(x_female_b, pdf_fun(x_female_b, dist_mu_female_b, dist_sg_female_b), label="female_b")

axs[1,2].plot(x_male_b, posterior(x_male_b, dist_mu_male_b, dist_mu_female_b, dist_sg_male_b, dist_sg_female_b, prior_male_b, prior_female_b), label="male_b_posterior")
axs[1,2].plot(x_female_b, posterior(x_female_b, dist_mu_female_b, dist_mu_male_b, dist_sg_female_b, dist_sg_male_b, prior_female_b, prior_male_b), label="female_b_posterior")
axs[1,2].axvline(x=bayesian_classification_point_b, label="decision boundary", color="olive")

axs[1,2].set_title("Combine Plots part b")

axs[0,0].legend()
axs[0,1].legend()
axs[0,2].legend()
axs[1,0].legend()
axs[1,1].legend()
axs[1,2].legend()

plt.show()