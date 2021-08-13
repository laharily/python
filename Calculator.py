def add (num1, num2):
    return num1 + num2
def sub (num1, num2):
    return num1 - num2
def mul (num1, num2):
    return num1 * num2
def div (num1, num2):
    return num1/num2

which = input ("Which funtion do you want to use (add, sub, mul, div) ?")
if which == "add" or which == "sub" or which == "mul" or which == "div":
    num1 = int (input("Enter the first number: "))
    num2 = int (input("Enter the second number: "))
    if which == "add":
        add = add (num1, num2)
        print (add)
    elif which == "sub":
        difference = sub (num1, num2)
        print (difference)
    elif which == "mul":
        product = mul (num1, num2)
        print (product)
    elif which == "div":
        quotient = div (num1, num2)
        print (quotient)
else:
    nuprint ("invalid response")


                   
    
    

