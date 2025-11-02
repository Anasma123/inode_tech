# ---------------------------------------------
# Function Name: count_up_to(n)
# Purpose: Generate numbers from 1 up to n one-by-one using yield
# ---------------------------------------------
def count_up_to(n):
    x = 1   # Variable x start cheyyunnu 1 ninn
    
    # Loop run cheyyum x <= n vare
    while x <= n:
        # yield → ithu normal return alla.
        # yield value return cheyyum but function stop cheyyilla.
        # Function "pause" cheyyum and next callil athine continue cheyyum.
        yield x

        # Next value kittan x increment cheyyunnu
        x += 1


# ---------------------------------------------
# Using the Generator
# ---------------------------------------------
# for loop use cheythu count_up_to(5) generator call cheyyunnu
# Python automatically next() call cheyyum oru oru value kittan
for num in count_up_to(5):
    print(num)   # Oru thavana oru value print cheyyum (1,2,3,4,5)

# Ithu one-by-one value return cheyyum (not all at once)

#yield x → oru thavana value return cheyyum,
#but function “pause” cheyyum, stop alla.
