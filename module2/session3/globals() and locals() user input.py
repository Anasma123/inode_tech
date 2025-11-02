# ============================================================
# Example: Understanding Global & Local Namespaces (User Input)
# Module 2 → Session 3: Python Scopes and Namespaces
# ============================================================

# ---------- Global Namespace ----------
school_name = input("Enter your School Name (Global): ")
# Global variable (accessible anywhere)
# Manglish: Ithu global variable aanu — program muzhuvanil access cheyyam.

x = int(input("Enter a global number (x): "))
# Another global variable (numeric value)

def demo_function():
    # ---------- Local Namespace ----------
    # Variables declared here are LOCAL (exist only during this function call)
    y = int(input("\nEnter a local number (y): "))
    z = input("Enter a local string (z): ")

    print("\n--- Local Namespace ---")
    print(locals())   # Prints all local variables inside this function
    # Manglish: locals() → functioninte ullilulla ella variableum dictionary aayi kaanikkum.

# ---------- Outside Function (Global Level) ----------
print("\n--- Global Namespace Keys ---")
print(globals().keys())   # Shows all names (variables/functions) in the global namespace
# Manglish: globals().keys() → ithu purathulla ella variable perukalum list cheyyum.

# ---------- Function Call ----------
demo_function()  # Executes and prints local namespace
