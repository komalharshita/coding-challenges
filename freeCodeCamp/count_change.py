def count_change(change):
    total_cents = sum(change)  # Calculate the total in cents
    dollars = total_cents // 100  # Get the dollar amount
    cents = total_cents % 100  # Get the remaining cents
    
    return f"${dollars}.{cents:02d}"  


"""
Given an array of integers representing the coins in your pocket, 
with each integer being the value of a coin in cents, return the total amount in the format "$D.CC".

- 100 cents equals 1 dollar.
- In the return value, include a leading zero for amounts less than one dollar 
and always exactly two digits for the cents.
"""