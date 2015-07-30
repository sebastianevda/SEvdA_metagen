import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

#Thanks to Xyz for code basis
#requires canopy from enthought to run

#Input variables
#number of points in x, y or z array needs to be the same

x = np.array([5,5,5,5,5,5,10,10,10,10,10,10,15,15,15,15,15,15,20,20,20,20,20,20,25,25,25,25,25,25])
y = np.array([0,16,32,48,64,80,0,16,32,48,64,80,0,16,32,48,64,80,0,16,32,48,64,80,0,16,32,48,64,80])
#Type 1 z values
z = np.array([0,0,22.79202279,11.6796063,0,0,32.23140496,7.527593819,0,0,21.46261505,0,0,0,6.830107276,23.86746537,0,0,35.93729063,9.703561527,10.46439628,12.67578125,12.55990107,0,0,0,0,17.73700306,14.78687288,0])
#Type 2 z values
#z = np.array([77.17228174,0,77.20797721,88.3203937,100,55.35944899,67.76859504,92.47240618,0,0,61.40713655,0,0,100,93.16989272,15.05054287,82.65347746,100,25.67332172,39.16257909,89.53560372,87.32421875,78.98438708,0,52.97682709,72.9709743,71.18679051,82.26299694,85.21312712,0])
#Type 3 z values
#z = np.array([22.82771826,0,0,0,0,44.64055101,0,0,0,100,17.13024839,100,100,0,0,54.75477349,17.34652254,0,38.38938765,51.13385939,0,0,8.455711857,0,47.02317291,27.0290257,28.81320949,0,0,100])

#Set up a regular grid of interpolation points
xi, yi = np.linspace(x.min(), x.max(), 100), np.linspace(y.min(), y.max(), 100)
xi, yi = np.meshgrid(xi, yi)

#Interpolate
rbf = scipy.interpolate.Rbf(x, y, z, function='linear')
zi = rbf(xi, yi)

#plot
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(xi, yi, zi, rstride=1, cstride=1, cmap=cm.Blues_r,
        linewidth=0, antialiased=True)
ax.set_zlim(0, 100)
plt.gca().invert_yaxis()
ax.view_init(elev=38., azim=-155)
plt.show()
