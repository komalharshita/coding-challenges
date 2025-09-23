def lowestTriangle(trianglebase, area):
        h = 0
        while True:
                temp_area = 0.5*trianglebase*h
                if temp_area >= area:
                        return h
                h+= 1