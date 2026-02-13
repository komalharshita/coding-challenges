def get_fastest_speed(times):

    distances = [320, 280, 350, 300, 250]
    
    fastest_speed = 0
    fastest_segment = 0
    
    for i in range(len(times)):
        speed = distances[i] / times[i]  
        if speed > fastest_speed:
            fastest_speed = speed
            fastest_segment = i + 1  
    
    return f"The luger's fastest speed was {fastest_speed:.2f} m/s on segment {fastest_segment}."


"""
The first value in the given array corresponds to the time for segment 1, the second value to segment 2, and so on.
To calculate the speed (in meters per second) for a segment, divide the distance by the time.
Return "The luger's fastest speed was X m/s on segment Y.". 
Where X is the fastest speed, rounded to two decimal places, 
and Y is the segment number where the fastest speed occurred.
"""