original_principal = 1000000
rate_of_interest = 0.1
time_interval = 10
times = time_interval + 1
interest_yearly = []
principal_yearly = []


for time in range(1,times):
    
    interest = int(original_principal * rate_of_interest)
    original_principal = original_principal + interest
    interest_yearly.append(interest)
    principal_yearly.append(original_principal)
#   print(interest)
#   print(original_principal)

#print(interest_yearly)
#print(principal_yearly)
year = 1 

for interest in interest_yearly:
#    print("your interest for " + str(year) + " year is " + str(interest))
    year += 1

year_for_principal = 1
for amount in principal_yearly:
    for interest in interest_yearly:
        print("your interest for " + str(year) + " year is " + str(interest))
        year += 1
        print("your amount for " + str(year_for_principal) + " year is " + str(amount))
        year_for_principal += 1