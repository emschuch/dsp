[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (sampling distribution)

Suppose you draw a sample with size n=10 from an exponential distribution with λ=2. Simulate this experiment 1000 times and plot the sampling distribution of the estimate L. Compute the standard error of the estimate and the 90% confidence interval.

Repeat the experiment with a few different values of n and make a plot of standard error versus n.

Import modules:

```python
%matplotlib inline

import thinkstats2
import thinkplot
import math
import random
import numpy as np
import estimation
```

I created a mashup function combining <tt>Estimate3</tt> and <tt>SimulateSample</tt> to compute the confidence interval and RMSE and to plot the distribution:

```python
def PlotEstimate(n=10, m=1000):    
    def VertLine(x, y=1):
        thinkplot.Plot([x, x], [0, y], color='0.8', linewidth=3)

    lam = 2
    means = []
    for _ in range(m):
        xs = np.random.exponential(1.0/lam, n)
        L = 1 / np.mean(xs)
        means.append(L)

    cdf = thinkstats2.Cdf(means)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    VertLine(ci[0])
    VertLine(ci[1])
    print "Confidence Interval: %f, %f" % ci
    print 'RMSE L:', estimation.RMSE(means, lam)
    print 'Mean error L:', estimation.MeanError(means, lam)

    # plot the CDF
    thinkplot.Cdf(cdf)
    thinkplot.Show(root='estimation1',
                   xlabel='sample mean',
                   ylabel='CDF',
                   title='Sampling distribution', 
                   axis=[0, 8, 0, 1])

PlotEstimate()
```

> OUTPUT:<br>
Confidence Interval: 1.260047, 3.648992<br>
RMSE L: 0.816290000105<br>
Mean error L: 0.202643535225

![png](../img/ex8-2_01b.png)

The output is slightly different than when initially running <tt>estimation.Estimate3</tt> because <tt>random</tt> has created a different sample.

Now run the estimation again with a few different values for n:

```python
PlotEstimate(25)
```

> OUTPUT:<br>
Confidence Interval: 1.504487, 2.920092<br>
RMSE L: 0.456487646874<br>
Mean error L: 0.106193760384

![png](../img/ex8-2_02b.png)

```python
PlotEstimate(50)
```

> OUTPUT:<br>
Confidence Interval: 1.579438, 2.550010<br>
RMSE L: 0.290646902054<br>
Mean error L: 0.0261784221271

![png](../img/ex8-2_03b.png)

```python
PlotEstimate(100)
```

> OUTPUT:<br>
Confidence Interval: 1.716304, 2.375090<br>
RMSE L: 0.202077456126<br>
Mean error L: 0.0200191074379

![png](../img/ex8-2_04b.png)

```python
PlotEstimate(500)
```

> OUTPUT:<br>
Confidence Interval: 1.856731, 2.161175<br>
RMSE L: 0.0907252606581<br>
Mean error L: 0.00632567242885

![png](../img/ex8-2_05b.png)

I constrained the axis in <tt>PlotEstimate</tt> so that all plots would be comparable. We can see the 90% confidence interval becoming more narrow and slope of the graph getting steeper as the value of n increases. This means that the accuracy of estimation is increasing as we increase the sample size, as one would expect.

We can see that this holds true when plotting the sample size, n, versus the RMSE of L. As the sample size increases, the RMSE decreases:

```python
RMSEs = [0.748889560039, 0.456487646874, 0.290646902054, 0.202077456126, 0.0907252606581, 0.0649204394161]
Ns = [10, 25, 50, 100, 500, 1000]

thinkplot.Plot(Ns, RMSEs)
thinkplot.Show(xlabel = 'n value', 
               ylabel = 'RMSE of L', 
               axis = [0, 1010, 0, 1.0])
```

![png](../img/ex8-2_06b.png)
