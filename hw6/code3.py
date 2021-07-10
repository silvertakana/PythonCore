def is_perfect(n):
  if(n<0):
    print("n is not a nature number!")
    return
  numbers = []
  for i in range(1,round(n)):
    if(n%i == 0):
      numbers.append(i)
  if sum(numbers) == n:
    return True
  else:
    return False
n = int(input("your number:"))
print(is_perfect(n))
