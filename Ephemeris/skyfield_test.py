from skyfield.api import load, N, W, E, wgs84, EarthSatellite
from astropy import units as u
from skyfield.framelib import itrs
from skyfield.framelib import ecliptic_frame
from skyfield.framelib import galactic_frame

# Create a timescale and ask the current time.
ts = load.timescale()
# t = ts.now()
# t = ts.utc(1971, 10, 5, 13, 10, 00)
t = ts.utc(1995, 11, 4, 4, 20, 7)


# print(ts)
print(t.utc_datetime())
print("\n")

# Load the JPL ephemeris DE421 (covers 1900-2050).
planets = load('de421.bsp')
# print(planets)
earth, moon, mars = planets['earth'], planets['moon'], planets['mars']
mercury, jup, ven, sat = planets['mercury'], planets['jupiter barycenter'], planets['venus'], planets['saturn barycenter']
uranus, neptune, pluto = planets['uranus barycenter'], planets['neptune barycenter'], planets['pluto barycenter']

# What's the position of Mars, viewed from Earth?
astrometric = earth.at(t).observe(moon)
astrometric_m = earth.at(t).observe(mars)
ra, dec, distance = astrometric.radec()
ra_m, dec_m, distance_m = astrometric_m.radec()

print("RA, Dec, Dist of Moon")
print(ra)
print(dec)
print(distance)
print("\n")

print("RA, Dec, Dist of Mars")
print(ra_m)
print(dec_m)
print(distance_m)
print("\n")

boston = earth + wgs84.latlon(19.87757 * N, 75.34226 * E, elevation_m=588)  # 12.932063 * N, 79.333466 * W)  # 12.97194, 77.59369
# astrometric = boston.at(ts.utc(1995, 11, 4)).observe(moon)
astrometric = boston.at(t).observe(moon)
alt, az, d = astrometric.apparent().altaz()

print("Alt, AZ, dist of Moon")
print(alt)
print(az)
print(d)
print("\n")

boston_m = earth + wgs84.latlon(19.87757 * N, 75.34226 * E, elevation_m=588)  # 12.932063 * N, 79.333466 * W)  # 12.97194, 77.59369
# astrometric = boston.at(ts.utc(1995, 11, 4)).observe(moon)
astrometric_m = boston_m.at(t).observe(mars)
alt_m, az_m, d_m = astrometric_m.apparent().altaz()

print("Alt, AZ, dist of Mars")
print(alt_m)
print(az_m)
print(d_m)
print("\n")

xyz = astrometric.position.to(u.au)
right_ascension = ra.to(u.deg)
declination = dec.to(u.deg)

print("RA, Dec, Dist of Moon in AU")
print(xyz)
print('{0:0.03f}'.format(right_ascension))
print('{0:0.03f}'.format(declination))

xyz = astrometric.position.to(u.au)
altitude = alt.to(u.deg)
azimuth = az.to(u.deg)

print("Alt, AZ, dist of Moon in AU")
print(xyz)
print('{0:0.03f}'.format(altitude))
print('{0:0.03f}'.format(azimuth))

xyz = astrometric_m.position.to(u.au)
right_ascension_m = ra_m.to(u.deg)
declination_m = dec_m.to(u.deg)

print("RA, Dec, Dist of Mars in AU")
print(xyz)
print('{0:0.03f}'.format(right_ascension_m))
print('{0:0.03f}'.format(declination_m))

xyz = astrometric_m.position.to(u.au)
altitude_m = alt_m.to(u.deg)
azimuth_m = az_m.to(u.deg)

print("Alt, AZ, dist of Mars in AU")
print(xyz)
print('{0:0.03f}'.format(altitude_m))
print('{0:0.03f}'.format(azimuth_m))

# Important: must start with a position
# measured from the Earth’s center.
position = earth.at(t).observe(mars)

print('Cartesian:')

x, y, z = position.frame_xyz(itrs).au

print('  x = {:.3f} au'.format(x))
print('  y = {:.3f} au'.format(y))
print('  z = {:.3f} au'.format(z))
print()

print('Geographic:')

lat, lon = wgs84.latlon_of(position)
height = wgs84.height_of(position)

print(' {:.4f}° latitude'.format(lat.degrees))
print(' {:.4f}° longitude'.format(lon.degrees))
print(' {:.0f} km above sea level'.format(distance.km))
print("\n")

print('Cartesian ecliptic coordinates:')

x, y, z = position.frame_xyz(ecliptic_frame).au

print('  x = {:.3f} au'.format(x))
print('  y = {:.3f} au'.format(y))
print('  z = {:.3f} au'.format(z))
print()

print('Spherical ecliptic coordinates:')

lat, lon, distance = position.frame_latlon(ecliptic_frame)

print(' {:.4f} latitude'.format(lat.degrees))
print(' {:.4f} longitude'.format(lon.degrees))
print(' {:.3f} au distant'.format(distance.au))
print("\n")

print('Cartesian galactic coordinates:')

x, y, z = position.frame_xyz(galactic_frame).au

print('  x = {:.3f} au'.format(x))
print('  y = {:.3f} au'.format(y))
print('  z = {:.3f} au'.format(z))
print()

print('Spherical galactic coordinates:')

lat, lon, distance = position.frame_latlon(galactic_frame)

print(' {:.4f} latitude'.format(lat.degrees))
print(' {:.4f} longitude'.format(lon.degrees))
print(' {:.3f} au distant'.format(distance.au))


'''t1 = ts.utc(1995, 11, 4, 10, 30)
t2 = ts.utc(1995, 11, 4, 10, 30)

moon = planets['moon']
p1 = moon.at(t1)
p2 = moon.at(t2)

# km = (p2 - p1).distance().km
km = p1.distance().km
print('In one minute the Moon moved %d km' % km)'''

'''line1 = '1 25544U 98067A   14020.93268519  .00009878  00000-0  18200-3 0  5082'
line2 = '2 25544  51.6498 109.4756 0003572  55.9686 274.8005 15.49815350868473'
satellite = EarthSatellite(line1, line2, 'ISS (ZARYA)', ts)
print(satellite)

geocentric = satellite.at(t)
print(geocentric.position.km)

lat, lon = wgs84.latlon_of(geocentric)
print('Latitude:', lat)
print('Longitude:', lon)

bluffton = wgs84.latlon(19.87757 * N, 75.34226 * E)

difference = satellite - bluffton

topocentric = difference.at(t)
print(topocentric.position.km)

alt, az, distance = topocentric.altaz()

if alt.degrees > 0:
    print('The ISS is above the horizon')

print('Altitude:', alt)
print('Azimuth:', az)
print('Distance: {:.1f} km'.format(distance.km))

ra, dec, distance = topocentric.radec(epoch='1995, 11, 4')  # ICRF ("J2000")

print(ra)
print(dec)'''
