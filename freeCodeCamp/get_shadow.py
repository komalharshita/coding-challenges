def get_shadow(time):
    hours, minutes = map(int, time.split(':'))
    total_minutes = hours * 60 + minutes
    
    sunrise = 6 * 60  
    sunset = 18 * 60   
    noon = 12 * 60     
    
    if total_minutes < sunrise or total_minutes >= sunset:
        return "No shadow"
    elif total_minutes == noon:
        return "No shadow"
    
    distance_from_noon = abs(noon - total_minutes) / 60
    shadow_length = distance_from_noon ** 3
    
    if total_minutes < noon:
        direction = "west"
    else:
        direction = "east"
    
    if shadow_length.is_integer():
        shadow_str = f"{int(shadow_length)}ft"
    else:
        shadow_str = f"{shadow_length:.3f}ft"
    
    return f"{shadow_str} {direction}"

"""
Today is the equinox, when the sun is directly above the equator and perfectly overhead at noon. Given a time, determine the shadow cast by a 4-foot vertical pole.

The time will be a string in "HH:MM" 24-hour format (for example, "15:00" is 3pm).
You will only be given a time in 30 minute increments.
Rules:

The sun rises at 6am directly "east", and sets at 6pm directly "west".
A shadow always points opposite the sun.
The shadow's length (in feet) is the number of hours away from noon, cubed.
There is no shadow before sunrise (before 6am), after sunset (6pm or later), or at noon.
Return:

If a shadow exists, return "(length)ft (direction)". For example, "8ft west".
Otherwise, return "No shadow".
For example, given "10:00", return "8ft west" because 10am is 2 hours from noon, so 23 = 8 feet, and the shadow points west because the sun is in the east at 10am.
"""