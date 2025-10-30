x = "Global"

def outer():
    x = "Enclosing"
    def inner():
        x = "Local"
    inner()

outer()
print("Outside:", x)
