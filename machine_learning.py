# -*- coding: utf-8 -*-
"""machine_learning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15-iVZuwEJtnuqRqiKG8uCsx0tl0oRTtC

# Active Contours

## Active Contours using Parametric Curves
"""

from __future__ import division
from nt_toolbox.general import *
from nt_toolbox.signal import *
# %pylab inline
# %matplotlib inline
# %load_ext autoreload

"""#### Polygone initial"""

gamma0 = array([.78, .14, .42, .18, .32, .16, .75, .83, .57, .68, .46, .40, .72, .79, .91, .90]) + 1j*array([.87, .82, .75, .63, .34, .17, .08, .46, .50, .25, .27, .57, .73, .57, .75, .79])

"""#### Visualisation courbe initiale"""

periodize = lambda gamma: concatenate((gamma, [gamma[0]]))
def cplot(gamma,s='b',lw=1): 
    plot(real(periodize(gamma)), imag(periodize(gamma)), s, linewidth=lw)
    axis('equal')
    axis('off')
cplot(gamma0,'b.-');

"""## Active Contours using Level Sets"""