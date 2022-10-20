import ephem

moon = ephem.Moon()
moon.compute('1995/11/04 04:20:00')
print(moon.ra, moon.dec)

boston = ephem.Observer()
boston.lat = '19.87757'
boston.lon = '75.34226'
boston.date = '1995/11/4'
moon.compute(boston)
print(moon.alt + 0.0, moon.az + 0.0)
print(moon.alt, moon.az)
