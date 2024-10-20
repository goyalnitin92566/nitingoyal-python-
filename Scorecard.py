# Take user input
name = str(input("Enter Your Name :"))
score = int(input("Enter Your Marks: "))
print(f"Hi,{name}  :")

# Checking Score

if score<=90 or score<=100:
  print("Your Grade is A+")
elif score<=80 or score<=89:
  print("Your Grade is A")
elif score<=70 or score<=79:
  print("Your Grade is B")
elif score<=60 or score<=69:
  print("Your Grade is C")

else:
  ("Your Grade is C")