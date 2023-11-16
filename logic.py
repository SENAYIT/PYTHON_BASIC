
#logical operator

has_water=True
is_buy=False

if has_water and not is_buy:
    print("ok well")
elif has_water or is_buy:
    print("ok I will buy water")
else:
    print("well have anice day with water")


#exercise

name='se'


if len(name)<3:
    print('your name is less than 3 characters please write the correct name...')
elif len(name)>50:
    print('your name is greater than 50 character write again Please...')
else:
    print('it is good !')


