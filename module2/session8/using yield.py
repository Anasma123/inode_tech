# ---------------------------------------------
# Function Name: even_numbers(limit)
# Purpose: Generate even numbers up to the given limit one by one using yield
# ---------------------------------------------
def even_numbers(limit):
    # range(2, limit + 1, 2)
    # → This creates a sequence of numbers starting from 2 up to limit (inclusive), increasing by 2 each time.
    # → Ithu oru number series aanu start 2 ninn limit vare step 2 aayi.
    # For example: limit = 10 → range will generate 2, 4, 6, 8, 10.
    
    # for i in range(...) 
    # → For loop takes each value from range one by one and assigns it to 'i'.
    # → For loop range-il ninn oru oru value eduthu 'i'-il assign cheyyum.
    for i in range(2, limit + 1, 2):

        # yield i → returns the current value of i but does not end the function.
        # Next time the loop continues, function resumes from here.
        # yield i enna statement i value return cheyyum, function pause cheyyum stop alla.
        yield i


# ---------------------------------------------
# Using the Generator Function
# ---------------------------------------------
print("Even numbers:")

# even_numbers(10) → This calls the generator function and returns a generator object, not a list.
# for loop automatically calls next() each time to get the next yielded value.
# even_numbers(10) call cheyyumbol ith generator object return cheyyum (not list)
# for loop automatically next() call cheyyum each iteration-il.
for num in even_numbers(10):
    # print(num, end=" ") → prints all even numbers on the same line separated by space.
    # print(num, end=" ") → ella numbersum oru line-il space use cheythu print cheyyum.
    print(num, end=" ")
