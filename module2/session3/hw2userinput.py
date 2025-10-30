# ---------- Global Namespace ----------
school_name = input("Enter your School Name (Global): ")
x = int(input("Enter a global number (x): "))

def demo_function():
    # ---------- Local Namespace ----------
    y = int(input("\nEnter a local number (y): "))
    z = input("Enter a local string (z): ")

    print("\n--- Local Namespace ---")
    print(locals())   # shows all local variables inside this function

print("\n--- Global Namespace Keys ---")
print(globals().keys())   # shows all global variable names

demo_function()
