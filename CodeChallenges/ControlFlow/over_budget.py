def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    total = food_bill + electricity_bill + internet_bill + rent
    if budget < total:
        return True
    else:
        return False
