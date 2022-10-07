__author__ = 'Rick'
loanAmount = input("How much do you want to borrow? \n")
interestRate = input("What is the interest rate on your loan? \n")
repaymentLength = input("How many years to repay your loan? \n")
loanAmount = float(loanAmount)
interestRate = float(interestRate)
repaymentLength = float(repaymentLength)
interestCalculation = interestRate / 100
print(interestRate)
print(interestCalculation)
numberOfPayments = repaymentLength*12
monthlyRepaymentCost = loanAmount * interestCalculation * (1+interestCalculation) * numberOfPayments / ((1+interestCalculation) * numberOfPayments - 1)
totalCharge = (monthlyRepaymentCost * numberOfPayments) - loanAmount
print("You want to borrow $" + str(loanAmount) + " over " + str(repaymentLength) + " years, at an interest rate of " + str(interestRate) + "%")
print("Your monthly repayment will be $%.2f " % monthlyRepaymentCost)
print("The total charge on this loan will be $%.2f")
