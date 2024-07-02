
print("Welcome to the Tip Calculator app!\n")
subtotal = float(input("What was the subtotal of your bill? $"))
percent = float(input("What percentage would you like to tip? "))
numDiners = int(input("How many people are splitting the bill? "))

eachPay = round(subtotal / numDiners, 2)
# converts the percent for the tip into a multipliable decimal
eachTip = round((subtotal * (percent / 100)) / numDiners, 2)
eachPnT = round(eachPay + eachTip, 2)

# print result
print(f"\n****\nEach person will tip ${eachTip} and pay ${eachPay}, totaling ${eachPnT} needed from each person.\n****")