def too_much_screen_time(hours):
    for hour in hours:
        if hour >= 10:
            return True
    for i in range(len(hours) - 2):
        if sum(hours[i:i+3]) / 3 >= 8:
            return True
    if sum(hours) / len(hours) >= 6:
        return True
    return False




# Given an input array of seven integers, representing a week's time, where each integer is the amount of hours spent on your phone that day, determine if it is too much screen time based on these constraints:

#If any single day has 10 hours or more, it's too much.
#If the average of any three days in a row is greater than or equal to 8 hours, it’s too much.
#If the average of the seven days is greater than or equal to 6 hours, it's too much.

