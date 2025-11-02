# ---------------------------------------------
# Step 1: Import the 're' module
# ---------------------------------------------
# 're' module means Regular Expressions — Python’s pattern matching library
# ith textil ninn specific patterns search cheyyan upayogikkunnu
import re


# ---------------------------------------------
# Step 2: Create a text to search
# ---------------------------------------------
# txt variableil oru sentence store cheyyunnu
txt = "My name is Anas and I love Python"


# ---------------------------------------------
# Step 3: Define the pattern to search for
# ---------------------------------------------
# pattern enna variableil "python" enn word store cheyyunnu
# ithil case sensitivity undu (Python != python)
pattern = "python"


# ---------------------------------------------
# Step 4: Search for the pattern inside the text
# ---------------------------------------------
# re.search(pattern, txt)
# → ithu pattern textil undenkil first match return cheyyum,
# → illenkil None return cheyyum.
if re.search(pattern, txt):
    print("Match found!")   # Pattern found aayal ith print aakum
else:
    print("No match.")      # Pattern illenkil ith print aakum
