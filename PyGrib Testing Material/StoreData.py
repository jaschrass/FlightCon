import numpy as np
import matplotlib.pyplot as plt
import pygrib # import pygrib interface to grib_api

def grab_data(s):
    gribs = pygrib.open(s)

    print 'Grabbing reference to all temperature values'
    tempObj = gribs.select(name='Temperature')

    print 'Grabbing reference to all pressure values'
    pressureObj = gribs.select(name='Pressure')

    print 'Grabbing reference to all relative humidity values'
    humidityObj = gribs.select(name='Relative humidity')

    print 'Grabbing reference to all u-wind components'
    uwindObj = gribs.select(name='U component of wind')

    print 'Grabbing reference to all v-wind components'
    vwindObj = gribs.select(name='V component of wind')

    ylen = len(tempObj[0].values)
    xlen = len(tempObj[0].values[0])

    data = [[[[]]]]
    for h in range(0, len(tempObj)):
        print 'Loading values from height:', h
        types = [[[]]]
        types.append(tempObj[h].values)
        if h < len(pressureObj):
            types.append(pressureObj[h].values)
        else:
            types.append([[0]*xlen]*ylen)

        if h < len(humidityObj):
            types.append(humidityObj[h].values)
        else:
            types.append([[0]*xlen]*ylen)

        if h < len(uwindObj):
            types.append(uwindObj[h].values)
        else:
            types.append([[0]*xlen]*ylen)

        if h < len(vwindObj):
            types.append(vwindObj[h].values)
        else:
            types.append([[0]*xlen]*ylen)
        data.append(types)
    npdata = np.array(data)
    return npdata

if __name__ == '__main__':
    data = grab_data('test.grb2')

    Z = data[-4][1]

    Y = list(range(0, len(data[1][1])))
    X = list(range(0, len(data[1][1][0])))

    X, Y = np.meshgrid(X, Y)

    plt.figure()
    plt.contourf(X, Y, Z)
    plt.colorbar()
    plt.show()
