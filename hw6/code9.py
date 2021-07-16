def count_odds(text,index = 0):
    txt = str(text)
    letter = txt[index]
    num = int(letter)
    i = index+1
    if(i == len(txt)): return (num%2)
    return count_odds(text,i) + (num%2)

n = int(input("n>>"))
print(f"the amount of odd digits in your number is: {count_odds(n)}")
