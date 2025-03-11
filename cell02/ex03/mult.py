number1 = int(input("Enter your First number  number")) 
number2 = int(input("enter your Second number"))
result = number1 * number2
print(f"{number1} x {number2} = {result}")

if result > 0 :
    print("The result is positive ")
elif result < 0 :
    print("the result is negative ")
else:
    print("the result is positive and negative")