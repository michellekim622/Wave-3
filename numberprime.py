# Determine a number prime
def isPrime(n):
  if n <= 1:
      return False

  for i in range(2, n):
      if not n % i:
          return False

  return True

value = int(input("Enter the Integer:"))
if isPrime(value):
    print(value,"is Prime number")
else:
    print(value,"is Not Prime number")
