from skyfield.api import load, N, W, E, wgs84, EarthSatellite
from astropy import units as u
from skyfield.framelib import ecliptic_frame, galactic_frame
from skyfield.framelib import itrs
import math, numpy
from skyfield.units import Angle

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
mercury, jup, ven, sat = planets['mercury'], planets['jupiter barycenter'], \
                         planets['venus'], planets['saturn barycenter']
uranus, neptune, pluto = planets['uranus barycenter'], planets['neptune barycenter'], planets['pluto barycenter']

planet_list = {'mars': mars, 'mercury': mercury, 'jup': jup, 'ven': ven, 'sat': sat, 'uranus': uranus,
               'neptune': neptune, 'pluto': pluto, 'moon': moon}


def planet_pos(planet_name, planet):
    astrometric = earth.at(t).observe(planet)
    ra, dec, distance = astrometric.radec()

    boston = earth + wgs84.latlon(19.87757 * N, 75.34226 * E,
                                  elevation_m=588)  # 12.932063 * N, 79.333466 * W)  # 12.97194, 77.59369
    # astrometric = boston.at(ts.utc(1995, 11, 4)).observe(moon)
    astrometric = boston.at(t).observe(planet)
    alt, az, d = astrometric.apparent().altaz()

    xyz = astrometric.position.to(u.au)
    right_ascension = ra.to(u.deg)
    declination = dec.to(u.deg)

    print(f"RA, Dec, Dist of {planet_name} in AU")
    print(xyz)
    print('RA : {0:0.03f}'.format(right_ascension))
    print('Dec : {0:0.03f}'.format(declination))
    print('Dist : ', distance)

    xyz = astrometric.position.to(u.au)
    altitude = alt.to(u.deg)
    azimuth = az.to(u.deg)

    print(f"Alt, AZ, dist of {planet_name} in AU")
    print(xyz)
    print('Alt : {0:0.03f}'.format(altitude))
    print('AZ : {0:0.03f}'.format(azimuth))
    print('Dist : ', d)

    print(f"Alt, AZ, dist of {planet_name} using geografical position")
    print(alt.dstr())
    print(az.dstr())
    print(d)

    print('Cartesian ecliptic coordinates:')

    boston = earth + wgs84.latlon(19.53 * N, 75.20 * E,
                                  elevation_m=588)
    # position = earth.at(t).observe(planet)
    position = boston.at(t).observe(planet)

    '''x, y, z = position.frame_xyz(ecliptic_frame).au
    vel1, vel2 = position.frame_xyz_and_velocity(ecliptic_frame)

    print('  x = {:.3f} au'.format(x))
    print('  y = {:.3f} au'.format(y))
    print('  z = {:.3f} au'.format(z))
    print('  vel1 = ', vel1)
    print('  vel2 = ', vel2)'''

    print('Spherical ecliptic coordinates:')

    lat, lon, distance = position.frame_latlon(ecliptic_frame)

    print(' {:.4f} latitude'.format(lat.degrees))
    print(' {:.4f} longitude'.format(lon.degrees))
    print(' {:.3f} au distant'.format(distance.au))

    print(' latitude', lat)
    # print(type(lon.degrees))
    print(' longitude', lon)
    print(' distant', distance)

    print(type(lon))

    lon_deg = lon.degrees - numpy.float64(23.5)

    print(' Longitude', lon_deg)
    # print(' Longitude', Angle(degrees=lon_deg))
    # lon_ang = Angle(degrees=lon_deg)
    # print(' Longitude', lon_ang.dstr(format=u'{0}{1}°{2:02}′{3:02}.{4:0{5}}″'))
    print("\n")


for planet_n in planet_list:
    planet_pos(planet_n, planet_list[planet_n])
