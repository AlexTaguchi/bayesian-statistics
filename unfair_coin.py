# Modules
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

# Parameters
coin_flips = 10000
heads_bias = 0.3

# Discretize possible biases of coin to heads
heads_biases = np.arange(0, 1, 0.01)

# Uniform probability density function prior
prior = np.ones(len(heads_biases)) / len(heads_biases)
pdfs = np.zeros((coin_flips, len(heads_biases)))
pdfs[0] = prior

# Flip coins and update priors
for flip in range(1, coin_flips):

    # P(B|A): Likelihood of flipped coin result for all possible biases of coin to heads
    likelihood = heads_biases if np.random.rand() < heads_bias else 1 - heads_biases

    # P(B): Evidence or overall probability of observing heads
    evidence = sum(likelihood * pdfs[flip - 1])

    # P(A|B): Posterior probability distribution after observing the coin flip
    pdfs[flip] = (likelihood * pdfs[flip - 1]) / evidence

# Set up figure to be animated
fig, ax = plt.subplots()
ax.set_xlabel('Bias of Coin to Heads')
ax.set_ylim(0, 1)
line, = ax.plot(heads_biases, pdfs[0], 'r-', linewidth=2)

# Update plot for animation
def update(i):
    ax.set_title(f'Coin Flip {i}')
    line.set_ydata(pdfs[i])

# Save animated evolution of coin bias for heads probability density function
anim = FuncAnimation(fig, update, frames=[x**2 for x in range(100)], interval=100)
anim.save('bayes_coin_flipping.gif', dpi=80, writer='imagemagick')