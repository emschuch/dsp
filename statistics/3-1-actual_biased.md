[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

First, read in the file:

```python
%matplotlib inline

import chap01soln
resp = chap01soln.ReadFemResp()
```

Make a PMF of <tt>numkdhh</tt>, the number of children under 18 in the respondent's household.

```python
import thinkstats2
pmf = thinkstats2.Pmf(resp.numkdhh, label = 'actual')
print 'mean:' pmf.Mean())
```

mean: 1.0242051550438309

```python
import thinkplot

thinkplot.Pmfs([pmf])
thinkplot.Show(xlabel = 'num kids in household', ylabel = 'probability')
```

![png](/../img/output_5_0.png)

Define <tt>BiasPmf</tt>.

```python
def BiasPmf(pmf, label=''):
    """Returns the Pmf with oversampling proportional to value.

    If pmf is the distribution of true values, the result is the
    distribution that would be seen if values are oversampled in
    proportion to their values; for example, if you ask students
    how big their classes are, large classes are oversampled in
    proportion to their size.

    Args:
      pmf: Pmf object.
      label: string label for the new Pmf.

     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf
```

Make a the biased Pmf of children in the household, as observed if you surveyed the children instead of the respondents.

```python
biased = BiasPmf(pmf, label = 'biased')
```

Display the actual Pmf and the biased Pmf on the same axes.

```python
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased])
thinkplot.Show(xlabel = 'num kids in household', ylabel = 'probability')
```

![png](/../img/output_11_0.png)

Compute the means of the two Pmfs.

```python
print 'actual mean:', pmf.Mean()
print 'biased mean:', biased.Mean()
```

actual mean: 1.02420515504

biased mean: 2.40367910066
