# ============================================================
# Example: Local and Global Namespace in Python
# Module 2 → Session 3: Scopes and Namespaces
# ============================================================

x = 10   # Global variable
# Ithu global variable aanu – program muzhuvanil access cheyyam
# Ee variable functioninte purath aanu define cheythath

def show():
    y = 5   # Local variable
    # Ithu local variable aanu – ee function ullil mathram access cheyyam
    # Function kazhinjal ithinte scope avasanikkum

    print("Local Namespace:", locals())
    # locals() → ee functioninte ullil define cheytha ella variableum
    # oru dictionary aayi print cheyyum
    # Example: {'y': 5}

# Function call cheyyunnu
show()

# Global namespace print cheyyunnu
print("Global Namespace:", globals().keys())
# globals().keys() → program muzhuvanil define cheytha variable,
# function, class okke list cheyyum
# Ee dictionaryil global variables ellam store cheyyappettirikkum
