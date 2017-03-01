# find the future value of money
#formula is FV = PV * (1 + r ) ^ t
# FV is future value
fv = 0.0

# PV is present value, how much you have now
pv = 0.0

# r is the rate of interest
r = 0.0 

# t is the time in periods of time that the interest is renewed
# for example, if the total time of compounding is 5 years but the number
# of compounding periods is monthly so that would mean t = 60

t = 0.0

print("What is the present value of your money?"),
pv = float(raw_input())

print("What is the rate of interest?"),
r = float(raw_input()) / 100

print("What is the number of compound periods"),
t = float(raw_input())

fv = pv + (1 + r) ** t


fv = str(round(float(fv)))

print("$" + fv)