def add (x:int , y:int) -> int:
    return x+y


total = add(1.5,2)
print(type(total))


# type hints says the type of parameter it doesnt matter 



def greet(name :str) -> None:
    print('hello')
    return None