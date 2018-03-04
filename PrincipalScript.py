import random
import string

terms = 200
interest  = 6
principal = 200000
Minimum_pay = 1000

cumulative_interest = 0
while principal > 0:
    cumulative_interest = principal * (1+((interest/100)/(240/12)))
    monthly_interest = cumulative_interest-principal
    monthly_Payment = (monthly_interest +1000)
    print(round(monthly_Payment,2),round(monthly_interest))
    principal = principal - 1000

