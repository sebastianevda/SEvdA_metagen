import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

#requires canopy from enthought to run.

#Input variables
#number of points in x, y or z array needs to be the same

x = np.array([0,0,0,0,0,0,0,0,0,0,15,15,15,15,15,15,15,15,15,15,30,30,30,30,30,30,30,30,30,30,45,45,45,45,45,45,45,45,45,45])
y = np.array([0,10,20,30,40,50,60,70,80,90,0,10,20,30,40,50,60,70,80,90,0,10,20,30,40,50,60,70,80,90,0,10,20,30,40,50,60,70,80,90])
#Type 1 z values
z = np.array([0,28.03372478,0,12.97811187,17.44186047,0,100,0,18.62083078,14.12378822,0,100,24.81629225,0,0,0,26.82977834,33.54618239,21.5680246,56.63374839,0,0,45.85839634,100,0,16.35283893,0,27.16259299,0,0,100,10.42135406,0,0,0,0,0,0,50.82325059,0])
#Type 2 z values
#z = np.array([0,0,0,0,20.36301758,0,0,0,0,0,0,0,51.14423683,0,13.75376768,0,0,6.949814489,26.5641814,10.87376556,25.48227081,0,0,0,0,30.76477404,0,0,32.51041749,0,0,13.79627736,0,0,100,0,0,0,16.6708245,0])
#Type 3 z values
#z = np.array([100,71.96627522,100,87.02188813,62.19512195,100,0,0,74.87210968,85.87621178,100,0,24.03947092,0,86.24623232,100,73.17022166,52.5659051,51.867794,32.49248605,74.51772919,0,54.14160366,0,0,52.88238702,100,72.83740701,67.48958251,0,0,66.74166496,100,100,0,100,0,0,32.50592491,0])


# Set up a regular grid of interpolation points
xi, yi = np.linspace(x.min(), x.max(), 100), np.linspace(y.min(), y.max(), 100)
xi, yi = np.meshgrid(xi, yi)

# Interpolate
rbf = scipy.interpolate.Rbf(x, y, z, function='linear')
zi = rbf(xi, yi)

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(xi, yi, zi, rstride=1, cstride=1, cmap=cm.Reds_r,
        linewidth=0, antialiased=True)
ax.set_zlim(0, 100)   
plt.gca().invert_yaxis()
ax.view_init(elev=38., azim=-155)
plt.show()
