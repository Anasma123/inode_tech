# 'data.txt' file open cheyyunnu read mode-il
# 'r' → read only mode
f = open("data.txt", "r")

# File-il ninn each line read cheyyunnu one by one
# 'for line in f' → loop runs through every line in the file
for line in f:
    # strip() → remove cheyyum extra spaces and newline characters (\n)
    print(line.strip())

# File close cheyyunnu — must for releasing resources
f.close()
