
#exercise
#conditions.py

price_house=1000000 
price_in='$'

is_goodcredit=False
is_none=True

if is_goodcredit:
    print('they need to pay 10 % of price_house: ' ,0.1*int (price_house) ,price_in)
elif is_none:
    print('they need to pay full of price_house: ' ,price_house ,price_in)
else:
    print('they need to pay 20 %  price_house: ' ,0.2*int (price_house) ,price_in)
    


#or using

price=1000000

has_good_credit =True
is_none=True

if has_good_credit:
    down_payment= 0.1*int(price)
elif is_none:
    down_payment=price
else:
    down_payment=0.2*int(price)

print(f"down payment is ${down_payment}")
    
