# Taking User Input

num_1 = float(input("Enter a First Number :"))
num_2 = float(input("Enter a Second Number"))
operations = input('Enter Operations (+,-,*,/):')
print("The Result is :")

# Perform the operations

if operations == "+":
  print(num_1+num_2)
elif operations == "-":
  print(num_1 - num_2)
elif operations == "*":
  print(num_1 * num_2)
elif operations == "/":
  if num_2!=0:
    print(num_1/num_2)
  else:
    print("Error! can't divide by zero ")
else:
  print("Invalid Opeartion")



