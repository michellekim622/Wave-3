# shipping calculator

def wrong_input_handling(data, variable=''):
    while True:
        try:
            data = float(data)
        except ValueError:
            print("Entered unrecognizable as a number %s" % variable )
            data = input("Enter a positive number: ")
            continue
        if data <= 0:
            print("Entered zero or negative number are not accepted %s" % variable)
            data = input("Enter a positive number: ")
            continue
        elif data != int(data):
            print("Entered decimal as a number is not accepted %s" % variable )
            data = input("Enter a positive integer: ")
            continue
        else:
            data = int(data)
            break
        
    return data

def sendingCost(amountItems, costItem=2.95, costFirst=10.95):
    
    amountItems = wrong_input_handling(amountItems, '(Cantidad de Elementos)')    
    
    totalCost = costFirst + costItem*(amountItems-1)
    
    return totalCost

cost = input("Enter the quantity of items purchased: ")

print("Shipping cost: %f" %sendingCost(cost))
