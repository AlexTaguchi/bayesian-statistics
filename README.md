# bayesian-statistics
Overview of Bayesian statistics and its applications in machine learning

*References:*
- https://www.quantstart.com/articles/Bayesian-Statistics-A-Beginners-Guide
- https://en.wikipedia.org/wiki/Bayes%27_theorem

### Comparison of Frequentist and Bayesian statistics
- Frequentist statistics: The probability of observing a particular event is calculated by considering only how often it has happened in the past.
- Bayesian statistics: The probability of observing a particuluar event considers both how often it has happened in the past and the conditions associated with it happening (or not happening).

### Flipping a Coin
#### Interpretation of the Problem
- Frequentist interpretation:
  - No initial assumption is made about the system
  - The more we flip the coin, the more the ratio of heads to tails will trend towards the true distribution
- Bayesian interpretation:
  - An initial assumption is made about the coin (that it is fair)
  - The more we flip the coin, the more our posterior belief (current belief) is updated from our prior belief (that the coin is fair) in the presence of new information

#### Bayes' Theorem
