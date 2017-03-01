import math

# P is principal, starting amount
p = 10000
# i is interest rate
r = 3/(100*12)

# n is the number of (time periods) that take place
n = 12
# Y is the loan term in number of years
Y = 10 *n 
#simple compunded interest while in college: P * [ (1 + i)^n - 1 ]
# You subtract the "P" (showed here as 1) at the end so that you are only left with the interest amount. 
# i gets divided by 12 since we're compounding monthly
# ci = 'compound interest'



#Calculates monthly payments for college loans. Adds interest accumulated and multiplies by P(1+i/n)^nt
#n is the number of time period, out of a year, that the interest is applied. EX: for quarterly, n = 4
# payment = 'monthly payment'

payment = p * (r/(1-math.pow((1+r), (-Y))))
print(payment)