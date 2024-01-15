import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# example data
mu = 90  # mean of distribution
sigma = 25  # standard deviation of distribution
x = mu + sigma * np.random.randn(5000)
num_bins = 25

fig, ax = plt.subplots()

# the histogram of the data
n, bins, patches = ax.hist(x, num_bins, density=1)

# add a 'best fit' line using stats.norm.pdf
y = stats.norm.pdf(bins, mu, sigma)
ax.plot(bins, y, '--')

ax.set_xlabel('Example Data')
ax.set_ylabel('Probability density')
sTitle = r'Histogram ' + str(len(x)) + ' entries into ' + str(num_bins) + ' Bins: $\mu=' + str(mu) + '$, $\sigma=' + str(sigma) + '$'
ax.set_title(sTitle)

fig.tight_layout()

sPathFig = 'D:\\Datascience\\Datascience\\vkhcggit\\practical-data-science\\VKHCG\\05-DS\\4000-UL\\0200-DUDU-Histogram.png'
fig.savefig(sPathFig)
plt.show()
