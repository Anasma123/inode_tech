# Open cheyyunnu oru text file write mode-il ("w")
# "w" mode → file illeenkil create cheyyum, undenkil overwrite cheyyum
f = open("data.txt", "w")

# File-il oru line ezhuthunnu
# \n means newline (pudhiya line)
f.write("Hello students!\n")

# Innum oru text ezhuthunnu
f.write("Welcome anas.")

# File close cheyyunnu – very important!
# Closing ensures all data is properly saved to disk.
f.close()

# Confirmation message print cheyyunnu
print("Data written successfully.")
