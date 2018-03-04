
cost_of_item = int(input("Enter the cost: "))
cash_provided = int(input("Cash : "))

while cash_provided < cost_of_item:
    print('\n')
    print(cash_provided)
    print("Need More cash ")
    extra_cash = int(input("Give More Cash: "))
    cash_provided = cash_provided + extra_cash

if cash_provided == cost_of_item:
    print('\n')
    print(cost_of_item)
    print(cash_provided)
    print("No Change")

if cash_provided > cost_of_item:
    print('\n')
    print(cost_of_item)
    print(cash_provided)
    print("change: ",(cash_provided-cost_of_item))
