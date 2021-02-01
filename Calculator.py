num1 = float(input("please enter the first num: "))

operator = input("please enter the operator: ")

num2 = float(input("please enter the second num: "))

if operator == '+':
 print(num1 + num2)

elif operator == '-':
 print(num1 - num2)

elif operator == '*':
 print(num1 * num2)

elif operator == '/':
 print(num1 / num2)

else:
  print("wrong operator please try again")

