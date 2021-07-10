def count_upper_case(str):
  uper_case_Count = 0
  for i in range(len(str)):
    if(str[i].isupper()):
      uper_case_Count += 1
  return uper_case_Count
n = input("text>>")
print(count_upper_case(n))
