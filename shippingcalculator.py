# shipping calculator

def shippingCalculator(num_items):
    return (num_items - 1) * 2.95 + 10.95

print("Total: $", shippingCalculator(10))
