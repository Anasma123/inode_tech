# ============================================================
# Example: Object Reference Sharing in Lists
# Module 2 → Session 3: Names, Objects and References
# ============================================================

a = [1, 2, 3]   
# Ithu oru list aanu, memoryil oru object create cheyyum
# Variable 'a' ee listine point cheyyunnu (reference aayi store cheyyunnu)

b = a      
# Ivide 'b' um athae list object ne refer cheyyunnu
# Oru puthiya copy alla, randum same memory address share cheyyunnu

b.append(4)
# append() function listinte avasanathil 4 add cheyyum
# 'b' um 'a' um same list ne refer cheyyunnath kond, 
# ithinte impact randumilum kaanikkum

print("a =", a)
print("b =", b)
# Ividethe randum same list print cheyyum
# Result: [1, 2, 3, 4]
