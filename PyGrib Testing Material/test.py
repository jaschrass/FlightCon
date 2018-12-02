# from mpl_toolkits.basemap import Basemap  # import Basemap matplotlib toolkit
import numpy as np
import matplotlib.pyplot as plt
import pygrib # import pygrib interface to grib_api

gribs = pygrib.open('test.grb2')

"""
for grb in gribs[0:3]:
    print(grb.keys())
    print('\n\n')"""

# Gribs list starts at 1, not 0
a = gribs.select(name='Temperature')


f = open('keys.txt', 'w')
for grb in gribs:
    f.writelines(str(grb)+'\n')
f.close()




# print a[0].latlons()
gribs.close()

# for key in gribs[1].keys():
#     print key

Y, X = a[10].latlons()

#Y = lat

Z = a[-4].values
plt.figure()
plt.contourf(X, Y, Z)
plt.colorbar()
plt.show()

"""BREAK
gribs.rewind() # rewind the iterator
from datetime import datetime
date_valid = datetime(2014,2,3,0)
t2mens = []
for grb in gribs:
    if grb.validDate == date_valid and grb.parameterName == 'Temperature' and grb.level == 2: 
        t2mens.append(grb.values)
t2mens = np.array(t2mens)
print t2mens.shape, t2mens.min(), t2mens.max()
lats, lons = grb.latlons()  # get the lats and lons for the grid.
print 'min/max lat and lon',lats.min(), lats.max(), lons.min(), lons.max()

fig = plt.figure(figsize=(16,35))
m = Basemap(projection='lcc',lon_0=-74,lat_0=41,width=4.e6,height=4.e6)
x,y = m(lons,lats)
for nens in range(1,51):
    ax = plt.subplot(10,5,nens)
    m.drawcoastlines()
    cs = m.contourf(x,y,t2mens[nens],np.linspace(230,300,41),cmap=plt.cm.jet,extend='both')
    t = plt.title('ens member %s' % nens)

'''
pygrib is installed and working 
Python 2.7 -> Python 3.5
Schedule work session
Works on Linux

'''"""