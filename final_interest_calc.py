original_principal = 1000000
rate_of_interest = 0.1
time_interval = 25
times = time_interval + 1
interest_yearly = []
principal_yearly = []

def com_interset_calc(original_principal1,rate_of_interest2,time_interval3):
    for time in range(1,times):
        interest = int(original_principal1 * rate_of_interest2)
        original_principal1 = original_principal1 + interest
        interest_yearly.append(interest)
        principal_yearly.append(original_principal1)
    #   print(interest)
    #   print(original_principal)


    year = 0

    while year < time_interval3:    
        print("your interest for " + str(year+1) + " year is " + str (interest_yearly[year])+ " and principal is "  +str(principal_yearly[year]))
        year += 1

#com_interset_calc(original_principal,rate_of_interest,time_interval)
com_interset_calc(1000000,0.2,10)

#print(interest_yearly)
#print(principal_yearly)