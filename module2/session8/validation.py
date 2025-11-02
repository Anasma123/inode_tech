# ---------------------------------------------
# Step 1: Import the re module
# ---------------------------------------------
# 're' module → Regular Expression library in Python
# ith textil specific pattern match cheyyan use cheyyunnu
import re


# ---------------------------------------------
# Step 2: Get user input
# ---------------------------------------------
# User ninn email input edukkunnu
email = input("Enter your email: ")


# ---------------------------------------------
# Step 3: Define the Regular Expression pattern
# ---------------------------------------------
# Pattern explain cheyyam 👇
# ^            → string start
# [a-zA-Z0-9_.]+ → alphabets, numbers, underscore or dot (username part)
# @            → must contain '@' symbol
# [a-zA-Z]+     → domain name (like gmail, yahoo)
# \.           → literal dot '.' (escape cheythu kodukkunnu)
# [a-zA-Z]+     → domain extension (like com, org, in)
# $            → string end
pattern = r"^[a-zA-Z0-9_.]+@[a-zA-Z]+\.[a-zA-Z]+$"


# ---------------------------------------------
# Step 4: Validate the email
# ---------------------------------------------
# re.match() → checks if the whole string matches the pattern from start to end
# re.match() full string check cheyyum pattern match cheyyunnundoo enn
if re.match(pattern, email):
    print("✅ Valid Email!")   # Email format correct aanel ith print cheyyum
else:
    print("❌ Invalid Email!") # Format wrong aanel ith print cheyyum
