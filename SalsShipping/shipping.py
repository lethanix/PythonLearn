weight = 1.5

# Ground Shipping
if weight <= 2:
    print(20.00 + 1.50 * weight)
elif (weight > 2) and (weight <= 6):
    print(20.00 + 3 * weight)
elif (weight > 6) and (weight <= 10):
    print(20.00 + 4 * weight)
elif weight > 10:
    print(20.00 + 4.75 * weight)

# Ground Shipping Premium
cost = 125.00
print(cost)

# Drone Shipping
if weight <= 2:
    print( 4.50 * weight)
elif (weight > 2) and (weight <= 6):
    print( 9 * weight)
elif (weight > 6) and (weight <= 10):
    print( 12 * weight)
elif weight > 10:
    print( 14.25 * weight)
