def is_prime(n):
  if(n<0):
    print("n is not a nature number!")
    return False
  for i in range(1,ceil(n/2)+1):
    if (i != n and i != 1 and n%i == 0):
      return False
  return True
print(is_prime(int(input("number>>"))))
