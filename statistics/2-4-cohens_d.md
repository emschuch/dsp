[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

Below is my code for solving the problem. I ran the code in an ipython notebook and investigated some summary statistics.

```python
import nsfg
import thinkstats2

df = nsfg.ReadFemPreg()

first = df[df.birthord == 1]
other = df[df.birthord > 1]

first.totalwgt_lb.mean(), other.totalwgt_lb.mean()

first.totalwgt_lb.var(), other.totalwgt_lb.var()

first.totalwgt_lb.std(), other.totalwgt_lb.std()

max(other.birthord)

effect = thinkstats2.CohenEffectSize(first.totalwgt_lb, other.totalwgt_lb
effect
```

The average birth weight of first babies was 7.201 lbs and the mean for other babies was 7.326 lbs, an absolute difference of 0.125 lbs. If we only look at the mean, first babies are lighter than others. 

To calculate the effect, the Cohen's d formula is the difference between the mean of each group over the pooled standard deviation. The effect size of first versus other babies was small, only -0.089 standard deviations. This doesn't seem very significant.

It is also worth noting that this may not be representative of the population as whole, since, as the author noted in the first chapter, some groups of women were deliberately oversampled for the NSFG study. It is possible that the effect size would change if we account for this oversampling.
