# Open cheyyunnu 'data.txt' file read mode-il
# 'r' means read only mode – file must already exist
f = open("data.txt", "r")

# Entire file content one shot-il read cheyyunnu
# f.read() returns the whole text as a single string
print(f.read())

# File close cheyyunnu – good practice
f.close()
