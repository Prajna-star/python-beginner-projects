def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

calci = {
    '+' : add, 
    '-' : subtract,
    '*' : multiply,
    '/' : divide
    }

def calculator():
    numa = float(input("Your no. "))
    while True:
        operation = input(''' '+' for add \n '-' for subtract \n '*' for multiply \n '/' for divide \n''')
        numb = float(input("Your no. "))

        value = calci[operation](numa, numb)
        print(f"your {value}")
        again = input("Yes again and No not again: ")
        if again == 'y':
            numa = value
        else:
            print(value)
            break

calculator()