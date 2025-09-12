from datetime import date

x = [int(e) for e in input().split(" ")]
return_date = date(x[2], x[1], x[0])

y = [int(e) for e in input().split(" ")]
expreturn_date = date(y[2], y[1], y[0])

fine = 0

if return_date > expreturn_date:
    if return_date.year != expreturn_date.year:
        fine = 10000
    elif return_date.month != expreturn_date.month:
        fine = 500 * (return_date.month - expreturn_date.month)
    else:
        fine = 15 * (return_date.day - expreturn_date.day)

print(str(fine))