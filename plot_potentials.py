import matplotlib.pyplot as plt
import numpy as np
from fractions import Fraction as frac
from matplotlib.ticker import FuncFormatter, MultipleLocator

plt.rcParams['text.usetex'] = True


def pi_axis_formatter(val, pos, denomlim=10, pi=r'\pi'):
    #format such that we obtain axis in multiples of pi
    #this code is obtained from : https://gist.github.com/vleugelcomplement/aa69e43c3d8b804864ede4a8c056e9cd

    minus = "-" if val < 0 else ""
    val = abs(val)
    ratio = frac(val/np.pi).limit_denominator(denomlim)
    n, d = ratio.numerator, ratio.denominator
    
    fmt2 = "%s" % d 
    if n == 0:
        fmt1 = "0"
    elif n == 1:
        fmt1 = pi
    else:
        fmt1 = r"%s%s" % (n,pi)
        
    fmtstring = "$" + minus + (fmt1 if d == 1 else r"{%s}/{%s}" % (fmt1, fmt2)) + "$"
    
    return fmtstring


ax = plt.gca()
ax.set_aspect('equal')


ticklen = np.pi/3

# setting ticks labels
ax.xaxis.set_major_formatter(FuncFormatter(pi_axis_formatter))
# setting ticks at proper numbers
ax.xaxis.set_major_locator(MultipleLocator(base=ticklen))




def U(x, k):
    return -(k/2*np.sin(x)**2 + np.cos(x))
    
x = np.arange(-np.pi, np.pi, 0.1)
y1 = U(x, 0)
y2 = U(x, 0.5)
y3 = U(x, 1)
y4 = U(x, 1.5)
y5 = U(x, 2)

ax.plot(x, y1, label= "k = 0")
ax.plot(x, y2, label= "k = 0.5")
ax.plot(x, y3, label= "k = 1")
ax.plot(x, y4, label= "k = 1.5")
ax.plot(x, y5, label= "k = 2")
plt.xlabel(r"$\theta$")
plt.ylabel(r"$U(\theta)$")
plt.legend()
plt.show()
