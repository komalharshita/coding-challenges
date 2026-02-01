from datetime import datetime, timedelta
from collections import defaultdict

def digital_detox(logs):
    log_times = [datetime.strptime(log, "%Y-%m-%d %H:%M:%S") for log in logs]
    
    log_times.sort()
    
    daily_count = defaultdict(int)
    for log in log_times:
        daily_count[log.date()] += 1
        if daily_count[log.date()] > 2:
            return False
    
    for i in range(len(log_times)):
        for j in range(i + 1, len(log_times)):
            if (log_times[j] - log_times[i]) <= timedelta(hours=4):
                return False
            if log_times[j] - log_times[i] > timedelta(hours=4):
                break
    
    return True


"""
Given an array of your login logs, determine whether you have met your digital detox goal.

Each log is a string in the format "YYYY-MM-DD HH:mm:ss".

You have met your digital detox goal if both of the following statements are true:

You logged in no more than once within any four-hour period.
You logged in no more than 2 times on any single day.

"""