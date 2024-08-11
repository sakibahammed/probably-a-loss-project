def pay_bill(balance:int , bill:int)->int:
    if balance >= bill:
        newBalance = balance - bill
        return str(newBalance) + " you can proceed"
    else :return "not enough balance"



print(pay_bill(10,500))
print(pay_bill(10000 , 32))
