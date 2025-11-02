# ============================================================
# Example: Local and Global Scope
# Module 2 → Session 3: Python Scopes and Namespaces
# ============================================================

x = 10   # global scope variable
# This variable is defined outside any function, so it can be accessed anywhere in the program.
# Ithu functioninte purath aanu define cheythath, program muzhuvanil access cheyyam.

def func():
    y = 5   # local scope variable
    # This variable belongs only to func() and exists only while the function is running.
    # Ithu function ullil define cheythath kond, function kazhinjal ith destroy aavum.

    print("Inside function:", y)
    # Printing the local variable y (works fine here).
    # Ivide y visible aanu, karanam ith function ullil aanu.

func()   # function call
# Executes the function. Inside it, y is accessible.
# Function call cheyyunnu, ivide y print cheyyum.

print("Outside function:", x)
# Global variable x can be accessed outside because it's defined globally.
# x global variable aanu, function purathum ith available aanu.

print("Trying y outside:", y)
# ❌ This will cause an error, because y is a local variable — it doesn’t exist outside func().
# ❌ Ithu error kodukkum, karanam y function ullil mathram aanu undayirunnath.
