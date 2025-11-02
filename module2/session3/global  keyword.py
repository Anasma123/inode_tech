# ============================================================
# Example: Using the 'global' keyword in Python
# Module 2 → Session 3: Python Scopes and Namespaces
# ============================================================

count = 0    # GLOBAL VARIABLE
# This variable is defined outside any function, so it's stored in the global namespace.

def increment():
    global count     # 'global' keyword declares that we are using the global variable 'count'
    #  "ente functionil use cheyyunna count, ath global aanu local alla"
    
    count += 2        # modifies the global variable directly (not creating a local one)
    print("Inside function:", count)   # prints updated global value

# calling the function
increment()

# printing from outside the function
print("Outside function:", count)
