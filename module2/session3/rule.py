# ============================================================
# Example: LEGB Rule Demonstration (Local, Enclosing, Global, Built-in)
# Module 2 → Session 3: Scopes and Namespaces
# ============================================================

x = "Global"  
# Ithu global variable aanu – program muzhuvanil access cheyyam

def outer():
    x = "Enclosing"  
    # Ithu outer() functioninte ullil define cheythathukond
    # Enclosing scope aanu (matulla function ullil aanu next inner())

    def inner():
        x = "Local"
        # Ithu innermost functioninte ullil define cheythathukond
        # Local scope aanu (functioninte private variable)

    inner()   # inner() call cheyyumbol x = "Local" create aavum,
              # function kazhinju ath destroy aavum

outer()       # outer() call cheythappol Enclosing scope x = "Enclosing" use aayi,
              # but ath global ne affect cheyyilla

print("Outside:", x)
# Global scopeil x still "Global" thanne aanu
