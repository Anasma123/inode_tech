# ============================================================
# Example: globals() and locals() in Python
# Module 2 → Session 3: Python Scopes and Namespaces
# ============================================================

school_name = "ABC Public School"   # Global variable
x = 100                             # Another global variable

def demo_function():
    # Local variables (only exist while the function runs)
    y = 20
    z = "Hello"

    print("\n--- Local Namespace ---")
    print(locals())   # Prints all local variables of this function
    # Manglish: locals() → ithu functioninte ullilulla ella variableum (y, z) print cheyyum.

print("--- Global Namespace ---")
print(globals().keys())   # Prints all global names (functions, variables, classes, modules, etc.)
# Manglish: globals().keys() → ithu programinte purath declare cheytha ella perukalum list cheyyum.

demo_function()   # Function call
