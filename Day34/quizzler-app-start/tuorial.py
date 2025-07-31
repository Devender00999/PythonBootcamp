# defining types in python 

# defining types for variables 
a: int = 5
b: bool = False

# defining types in function parameters
def fun(a: int, b: str):
   return str(a.bit_count()) + b.title()

# defining return type of funtion 
def fun(a: int, b: str) -> str:
   return str(a.bit_count()) + " " +  b.title()

print(fun(4, 'adsf'))
