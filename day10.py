import art
def add(n1,n2):
    return n1+ n2 
def sub(n3,n4):
    return n3 -n4
def mul(n5,n6):
    return n5 *n6
def div(n7, n8):
    return n7/n8

oprt = {"+": add,
         "-":sub, 
         "*":mul,
         "/":div,
    }

# print(oprt["*"](4,8))


def calculator():
    print(art.clac)
    
    num1= float(input("enter your first number:  "))
    should_continue = True

    while should_continue:

        for symbol in oprt:
            print(symbol)
        operation = input("entyer operation: ")
        # operation= input("+\n" \
        # "-\n" \
        # "*\n" \
        # "/\n" \
        # "enter your desire opeation:  ")
        num2= float(input("enter your next number: "))
        answer=oprt[operation](num1,num2)

        print(f"{num1} {operation} {num2} = {answer}")

        choice = input(f"type 'y' to contunue with {answer}," \
            "or type 'n to start a nwe claculation: ").lower()

        if choice == "y":
            num1 = answer
        else:
            should_continue=False
            print("\n*20")
            calculator()

calculator()
