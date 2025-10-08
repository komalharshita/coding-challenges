def goldilocks_zone(mass):
    l = mass ** 3.5
    ls = l**0.5
    start = round(0.95 * ls, 2)
    end = round(1.37 * ls , 2)
    res = [start, end]

    return res


"""
For the fifth day of Space Week, you will calculate the "Goldilocks zone" of a star - the region around a star where conditions are "just right" for liquid water to exist.

Given the mass of a star, return an array with the start and end distances of its Goldilocks Zone in Astronomical Units.

To calculate the Goldilocks Zone:

Find the luminosity of the star by raising its mass to the power of 3.5.
The start of the zone is 0.95 times the square root of its luminosity.
The end of the zone is 1.37 times the square root of its luminosity.
Return the distances rounded to two decimal places.
"""