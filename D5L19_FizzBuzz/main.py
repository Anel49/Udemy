'''
Write a program that automatically prints the solution to the FizzBuzz game.
These are the rules of the FizzBuzz game:

(1) Your program should print each number from 1 to 100 in turn and include number 100.

(2) When the number is divisible by 3 then instead of printing the number it should print "Fizz".

(3) When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

(4) And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
'''
# Write your code here 👇

for x in range(1, 101):
  if x % 3 == 0:
    if x % 5 == 0:
      print("FizzBuzz")
    else:
      print("Fizz")
  elif x % 5 == 0:
    print("Buzz")
  else:
    print(x)