# You need to write a function that checks whether if the number passed into
# it is a prime number or not.

def prime_checker(number):
  count = 0
  for x in range(2, number + 1):
    if number % x == 0:
      count += 1
  if count == 1:
    print(f"{num} is a prime number.")
  else:
    print(f"{num} is not a prime number.")

######################################

num = input("Enter a number to check if it's prime or not: ")

if num.isnumeric():
    num = int(num)
    prime_checker(num)
else:
    print("Input must be a number. Try again.")
