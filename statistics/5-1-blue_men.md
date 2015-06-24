[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters µ = 178 cm and σ = 7.7 cm for men, and µ = 163 cm and σ = 7.3 cm for women.
In order to join Blue Man Group, you have to be male between 5’10” and 6’1” (see http://bluemancasting.com). What percentage of the U.S. male population is in this range? Hint: use scipy.stats.norm.cdf.

```python
import thinkstats2
import scipy.stats
```

Create a representation of the normal distribution with <tt>scipy.stats.norm</tt>

```python
mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
```

Convert heights from feet and inches to centimeters

```python
cm = 0.39370
minHeight = (5 * 12 + 10) / cm
maxHeight = (6 * 12 + 1) / cm

print maxHeight, minHeight
```

The maximum height is 185.4 cm, the minimum height is 177.8 cm.

Next, evaluate the the top limit for the distribution, the bottom limit for the distribution, and take the difference between the two.

```python
top = scipy.stats.norm.cdf(maxHeight, loc=mu, scale=sigma)
bottom = scipy.stats.norm.cdf(minHeight, loc=mu, scale=sigma)

print top, bottom, top - bottom
```

About 83% of the male poplutaion in the US are under 6'1" and about 49% are under 5'10". About 34% of men are between these heights, meaning that a little more than a third of the male population is eligable to become a Blue Man, at least from a height standpoint.
