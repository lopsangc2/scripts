number_of_years = 11
time_periods = list(range(1,number_of_years))
interest = []
total_amount = []
principle = 500000
rate = 0.1

for period in time_periods:
    byaj = (principle * period * rate)
    principle = int(principle + byaj)
    total_amount.append(principle)
    interest.append(byaj)     
#    print(byaj)
print(interest)
print((total_amount))


    