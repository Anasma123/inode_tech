x = 10   # global variable

def display():
    x = 5   # local variable
    print("Inside function, x =", x)

display()
print("Outside function, x =", x)
