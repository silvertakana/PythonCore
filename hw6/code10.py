def Tribonacci(n):
    if(n == 1):
        return 1
    if(n == 2):
        return 1
    if(n == 3):
        return 2
    return Tribonacci(n-1) + Tribonacci(n-2) + Tribonacci(n-3)

n = float(input("n>> "))

print(f"Tribonacci of n = {Tribonacci(n)}")
