# ============================================================
# Example: Local vs Global Variable in Python
# Module 2 → Session 3: Python Scopes and Namespaces
# ============================================================

x = 10   # GLOBAL VARIABLE (defined outside any function)
# This variable is accessible anywhere in this file unless shadowed (overwritten) by a local variable.

def display():
    x = 5   # LOCAL VARIABLE (defined inside the function)
    # This variable exists only inside this function and hides the global 'x' temporarily.
    print("Inside function, x =", x)  # prints the local variable value (5)

# Calling the function
display()

# Now we are outside the function
print("Outside function, x =", x)  # prints the global variable value (10)
