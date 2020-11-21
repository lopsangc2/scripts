
initial_principle = 400000
total_amt = []
com_interest = []
deposit_time = 10
rate_of_interest = 0.1

for time in range(1,deposit_time+1):
    interest = int(initial_principle * time * rate_of_interest)    
    total_amount = int(interest + initial_principle)
    initial_principle = total_amount
    total_amt.append(total_amount)
    com_interest.append(interest)
#    print(interest)

#print(com_interest)
#print(total_amt)

for amount in total_amt:
    print("Amount is "+ str(amount) )
   
        
    
