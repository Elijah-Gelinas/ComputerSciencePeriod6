# get two numbers from user
num1 = int(input("Input first number: "))
num2 = int(input("Input second number: "))

# loop whle the numbers are not divisible (the remainder is 0)
while (num1 % num2 != 0):
  # inform user of result 
  print("{} and {} are not divisible.".format(num1, num2))
  print("To end program, please enter two values that are divisible.")
  # gather user input again
  num1 = int(input("Input first number: "))
  num2 = int(input("Input second number: "))
# inform user of result
print("Your numbers are divisible.")
print("{} is divisible by {}".format(num1, num2))
print(num1, "/", num2, "=", num1 / num2)