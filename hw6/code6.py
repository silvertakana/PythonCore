def is_pangram(str, alphabet = "abcdefghijklmnopqrstuvwxyz"):
  alphabet = alphabet.lower()
  for char in alphabet:
    if char not in str.lower():
      return False
  
  return True
string = input("text>>")
print(is_pangram(string))
