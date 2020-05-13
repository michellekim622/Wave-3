def wrong_input_handling(data):
    while True:
        try:
            data = float(data)
        except ValueError:
            print("Entered something unrecongnizable as a number")
            data = input("Enter a positive integer: ")
            continue
        if data < 0:
            print("Negative number is not accepted")
            data = input("Enter a positive integer: ")
            continue
        elif data != int(data):
            print("Negative number is not accepted")
            data = input("Enter a positive integer: ")
            continue
        else:
            data = int(data)
            break
        
    return data

def prime_factorization(n):
    n = wrong_input_handling(n)
    factor = 2
    
    while factor <= n: 
        if n%factor == 0:
            print(factor)
            n = n//factor
        else: 
            factor = factor +1

number = input("Enter an integer (2 or greater): ")

print(prime_factorization(number))
