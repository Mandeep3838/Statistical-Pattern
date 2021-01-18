# Importing Libraries
import numpy
import matplotlib.pyplot as plt
import seaborn as sns 

## Taking samples from distribution

# Uniform sampling 
rand_unif_100 = numpy.random.uniform(0,1,100)
rand_unif_1000 = numpy.random.uniform(0,1,1000)
rand_unif_10000 = numpy.random.uniform(0,1,10000)

# Normal Sampling
rand_gauss_100 = numpy.random.normal(0,1,100)
rand_gauss_1000 = numpy.random.normal(0,1,1000)
rand_gauss_10000 = numpy.random.normal(0,1,10000)

# Exponential Sampling
rand_exp_100 = numpy.random.exponential(1,100)
rand_exp_1000 = numpy.random.exponential(1,1000)
rand_exp_10000 = numpy.random.exponential(1,10000)

# Making Graph
fig, axs = plt.subplots(3,3, figsize=(10,20), constrained_layout=True)
fig.suptitle("Random Sampling")

# plot 1
bins = numpy.arange(0,1.1,0.1)
hist, edges = numpy.histogram(rand_unif_100, bins)
freq = hist/float(hist.sum())
axs[0,0].bar(bins[:-1], freq, width=0.1, align="edge", ec="k")
axs[0,0].set_title("Uniform ~ (0,1), 100 samples")
axs[0,0].set_xlabel("X-axis")
axs[0,0].set_ylabel("Rel. Frequency")

# plot 2
bins = numpy.arange(0,1.1,0.1)
hist, edges = numpy.histogram(rand_unif_1000, bins)
freq = hist/float(hist.sum())
axs[0,1].bar(bins[:-1], freq, width=0.1, align="edge", ec="k")
axs[0,1].set_title("Uniform ~ (0,1), 1000 samples")
axs[0,1].set_xlabel("X-axis")
axs[0,1].set_ylabel("Rel. Frequency")

# plot 3
bins = numpy.arange(0,1.1,0.1)
hist, edges = numpy.histogram(rand_unif_10000, bins)
freq = hist/float(hist.sum())
axs[0,2].bar(bins[:-1], freq, width=0.1, align="edge", ec="k")
axs[0,2].set_title("Uniform ~ (0,1), 10000 samples")
axs[0,2].set_xlabel("X-axis")
axs[0,2].set_ylabel("Rel. Frequency")

# plot 4

bins = numpy.arange(-4,4,0.2)
hist, edges = numpy.histogram(rand_gauss_100, bins)
freq = hist/float(hist.sum())
axs[1,0].bar(bins[:-1], freq, width=0.1, align="edge", ec="k")
axs[1,0].set_title("Normal ~ mu=0, sg=1, 100 samples")
axs[1,0].set_xlabel("X-axis")
axs[1,0].set_ylabel("Rel. Frequency")

# plot 5

bins = numpy.arange(-4,4,0.2)
hist, edges = numpy.histogram(rand_gauss_1000, bins)
freq = hist/float(hist.sum())
axs[1,1].bar(bins[:-1], freq, width=0.1, align="edge", ec="k")
axs[1,1].set_title("Normal ~ mu=0, sg=1, 1000 samples")
axs[1,1].set_xlabel("X-axis")
axs[1,1].set_ylabel("Rel. Frequency")

# plot 6

bins = numpy.arange(-4,4,0.2)
hist, edges = numpy.histogram(rand_gauss_10000, bins)
freq = hist/float(hist.sum())
axs[1,2].bar(bins[:-1], freq, width=0.1, align="edge", ec="k")
axs[1,2].set_title("Normal ~ mu=0, sg=1, 10000 samples")
axs[1,2].set_xlabel("X-axis")
axs[1,2].set_ylabel("Rel. Frequency")

# plot 7

bins = numpy.arange(-2,10,0.5)
hist, edges = numpy.histogram(rand_exp_100, bins)
freq = hist/float(hist.sum())
axs[2,0].bar(bins[:-1], freq, width=0.1, align="edge", ec="k")
axs[2,0].set_title("Exp lambda=1, 100 samples")
axs[2,0].set_xlabel("X-axis")
axs[2,0].set_ylabel("Rel. Frequency")

# plot 8

bins = numpy.arange(-2,10,0.5)
hist, edges = numpy.histogram(rand_exp_1000, bins)
freq = hist/float(hist.sum())
axs[2,1].bar(bins[:-1], freq, width=0.1, align="edge", ec="k")
axs[2,1].set_title("Exp lambda=1, 1000 samples")
axs[2,1].set_xlabel("X-axis")
axs[2,1].set_ylabel("Rel. Frequency")

# plot 9

bins = numpy.arange(-2,10,0.5)
hist, edges = numpy.histogram(rand_exp_10000, bins)
freq = hist/float(hist.sum())
axs[2,2].bar(bins[:-1], freq, width=0.1, align="edge", ec="k")
axs[2,2].set_title("Exp lambda=1, 10000 samples")
axs[2,2].set_xlabel("X-axis")
axs[2,2].set_ylabel("Rel. Frequency")

plt.show()
