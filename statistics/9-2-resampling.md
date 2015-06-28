[Think Stats Chapter 9 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2010.html#toc90) (resampling)

Exercise 9.2: In Section 9.3, we simulated the null hypothesis by permutation; that is, we treated the observed values as if they represented the entire population, and randomly assigned the members of the population to the two groups.<br>
An alternative is to use the sample to estimate the distribution for the population, then draw a random sample from that distribution. This process is called resampling. There are several ways to implement resampling, but one of the simplest is to draw a sample with replacement from the observed values, as in Section 9.10.<br>
Write a class named DiffMeansResample that inherits from DiffMeansPermute and overrides RunModel to implement resampling, rather than permutation.<br>
Use this model to test the differences in pregnancy length and birth weight. How much does the model affect the results?<br>

Import modules and data:

```python
import hypothesis
import thinkstats2
import first
import random
import numpy as np

live, firsts, others = first.MakeFrames()
```

Create new class, <tt>DiffMeansResample</tt> which inherits from <tt>DiffMeansPermute</tt>:

```python
class DiffMeansResample(hypothesis.DiffMeansPermute):
    def RunModel(self):
        group1 = np.random.choice(self.pool, self.n, replace = True)
        group2 = np.random.choice(self.pool, self.m, replace = True)
        return group1, group2
```

Run resampling model:

```python
data_prg = (firsts.prglngth.dropna().values, 
            others.prglngth.dropna().values)
ht = DiffMeansResample(data_prg)
pvalue_prg = ht.PValue(iters=10000)

data_wgt = (firsts.totalwgt_lb.dropna().values, 
            others.totalwgt_lb.dropna().values)
ht2 = DiffMeansResample(data_wgt)
pvalue_wgt = ht2.PValue(iters=10000)

print 'means resampling'
print 'p-value prglngth:', pvalue_prg
print 'p-value totalwgt_lb:', pvalue_wgt
```

> OUTPUT:<br>
means resampling<br>
p-value prglngth: 0.1708<br>
p-value totalwgt_lb: 0.0

Run permutation model for comparison:

```python
ht = hypothesis.DiffMeansPermute(data_prg)
pvalue_prg = ht.PValue(iters=10000)

ht2 = hypothesis.DiffMeansPermute(data_wgt)
pvalue_wgt = ht2.PValue(iters=10000)

print 'means permutation'
print 'p-value prglngth:', pvalue_prg
print 'p-value totalwgt_lb:', pvalue_wgt
```

> OUTPUT:<br>
means permutation<br>
p-value prglngth: 0.1657<br>
p-value totalwgt_lb: 0.0

For pregnency length, both models yielded a p-value of about 0.17, indicating that differences in pregnency length between first babies and others are not statistically significant. However, for total weight, both models yielded a p-value of 0, indicating that the difference in weights between first babies and others is statistically significant.
