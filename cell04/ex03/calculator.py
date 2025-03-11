a = (input("Give me the First number"))
if '.' in a: 
  number = float(a)
  if number.is_integer():
    print("this number a interger")
  else :
    print("this number is decimal")
else :
  print("this number is interger")


