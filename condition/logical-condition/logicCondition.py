def discount_applies(age :int)-> bool:
    if(age <18 or age>=65):
        return True
    else : return False


print(discount_applies(14))
print(discount_applies(41))



def discount_given(age:int)->bool:
    if(age>=21 and age<=56):
        return True
    else : return False
    
print(discount_given(29))