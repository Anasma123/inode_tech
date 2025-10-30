x = 10   # global scope

def func():
    y = 5  # local scope
    print("Inside function:", y)

func()
print("Outside function:", x)
print("Trying y outside:", y)   # ❌ error
