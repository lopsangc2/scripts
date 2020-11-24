original_principal = float(input("Enter The Amount " +
                     "you want to deposit.  "))
rate_of_interest = float(input("Enter the rate of "+
                    "interest  "))
time_interval = int(input("How many years would you "+ 
                    "like to deposit your Amount  "))
times = time_interval + 1
interest_yearly = []
principal_yearly = []

def com_interset_calc(original_principal1,rate_of_interest2,time_interval3):
    for time in range(1,times):
        interest = int(original_principal1 * rate_of_interest2)
        original_principal1 = int(original_principal1 + interest)
        interest_yearly.append(interest)
        principal_yearly.append(original_principal1)
    #   print(interest)
    #   print(original_principal)


    year = 0

    while year < time_interval3:    
        print("your interest for " + str(year+1) + 
        " year is " + str (interest_yearly[year])+
         " and principal is "  
         +str(principal_yearly[year]))
        year += 1

com_interset_calc(original_principal,rate_of_interest,time_interval)

#print(interest_yearly)
#print(principal_yearly)