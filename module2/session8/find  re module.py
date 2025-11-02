# ---------------------------------------------
# Step 1: Import the 're' module
# ---------------------------------------------
# 're' means Regular Expression module in Python
# ith regular expressions (pattern matching) cheyyan upayogikkunna built-in library aanu
import re


# ---------------------------------------------
# Step 2: Create a sample text
# ---------------------------------------------
# text variable-il oru sentence store cheyyunnu
# ithil two mobile numbers undu
text = "My phone numbers are 9876543210 and 9123456789"


# ---------------------------------------------
# Step 3: Find all numbers using re.findall()
# ---------------------------------------------
# re.findall(pattern, string)
# → This function returns all substrings that match the given pattern.
# → ith pattern match cheytha ellaa substringsum list form-il return cheyyum.

# Pattern: r"\d+"
# \d → represents any digit (0–9)
# +  → means "one or more times"
# So together → "\d+" means "one or more digits continuously"
numbers = re.findall(r"\d+", text)


# ---------------------------------------------
# Step 4: Display the result
# ---------------------------------------------
# ithil numbers enna variable-il list aayi numbers store aakum
print(numbers)

# Output example:
# ['9876543210', '9123456789']
