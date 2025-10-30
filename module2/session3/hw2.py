school_name = "ABC Public School"   # Global variable
x = 100

def demo_function():
    y = 20
    z = "Hello"
    print("\n--- Local Namespace ---")
    print(locals())   # Prints all local variables inside this function

print("--- Global Namespace ---")
print(globals().keys())   # Prints all global names in program

demo_function()
