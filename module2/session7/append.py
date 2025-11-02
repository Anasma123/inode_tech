# Open cheyyunnu file 'append' mode-il
# 'a' means append mode – puthiya data fileinte avasanathil add cheyyum (old data delete aakilla)
f = open("data.txt", "a")

# Puthiya line add cheyyunnu file-il
# \n → newline character (pudhiya line-il start cheyyan)
f.write("\nThis line is appended.")

# File close cheyyunnu
f.close()

# Confirmation message print cheyyunnu
print("Data appended!")
