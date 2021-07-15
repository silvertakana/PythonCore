width = int(input("width>> "))
height = int(input("height>> "))

def create_Matrix(width,height):
  return [[x*y for x in range(width)] for y in range(height)] 

print(create_Matrix(width,height))
