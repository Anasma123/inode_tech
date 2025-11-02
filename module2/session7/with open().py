# 'with open()' → safest method to handle files
# File automatically close aakum block kazhinjal (even if error varunna samayathum)
# 'r' means read mode
with open("data.txt", "r") as f:
    # Entire file content read cheythu print cheyyunnu
    print(f.read())

# with block automatic aayi close cheyyum. Safe method aanu.
