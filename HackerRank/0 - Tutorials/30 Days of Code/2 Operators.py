def solve(meal_cost, tip_per, tax_per):
    tip = meal_cost * ( tip_per / 100)
    tax = meal_cost * ( tax_per / 100)

    total = meal_cost + tip + tax 
    print(round(total))

if __name__ == '__main__':
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)