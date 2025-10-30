x = 10   # global variable

def show():
    y = 5  # local variable
    print("Local Namespace:", locals())

show()
print("Global Namespace:", globals().keys())
