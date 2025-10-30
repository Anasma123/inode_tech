count = 0   # global variable

def increment():
    global count
    count += 1
    print("Inside function:", count)

increment()
print("Outside function:", count)
