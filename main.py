for number in range (1,101):
  if number % 15 == 0:
    print("fizz-buzz")
  elif number % 5 == 0: 
    print("Buzz")
  elif number % 3 == 0:
    print("fizz")
  else:
    print(number)
