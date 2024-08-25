def bank(X, Y):
    annual_interest_rate = 0.10
    
    amount = X
    
    for _ in range(Y):
        amount += amount * annual_interest_rate
    
    return amount

initial_deposit = 1000  
years = 5  

final_amount = bank(initial_deposit, years)
print(f"Сумма на счету спустя {years} лет: {final_amount:.2f} рублей")