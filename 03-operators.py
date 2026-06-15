# ==============================================================================
# THE ULTIMATE PYTHON OPERATORS MASTERCLASS
# ==============================================================================

# ------------------------------------------------------------------------------
# STEP 1: Arithmetic Operators
# ------------------------------------------------------------------------------
print("--- Step 1: Arithmetic Operators ---")
a = 15
b = 4

print(f"Addition (a + b):         {a + b}")       # 19
print(f"Subtraction (a - b):      {a - b}")       # 11
print(f"Multiplication (a * b):   {a * b}")       # 60
print(f"Division (a / b):         {a / b}")       # 3.75 (Always returns a float)
print(f"Floor Division (a // b):  {a // b}")      # 3 (Rounds down to nearest whole number)
print(f"Modulus/Remainder (a % b): {a % b}")      # 3 (15 divided by 4 leaves remainder 3)
print(f"Exponentiation (a ** b):  {a ** b}")     # 50625 (15 to the power of 4)
print()


# ------------------------------------------------------------------------------
# STEP 2: Assignment Operators
# ------------------------------------------------------------------------------
print("--- Step 2: Assignment Operators ---")
x = 10  # Basic assignment
print(f"Initial x: {x}")

x += 5  # Equivalent to: x = x + 5
print(f"After x += 5: {x}")

x *= 2  # Equivalent to: x = x * 2
print(f"After x *= 2: {x}")

x %= 4  # Equivalent to: x = x % 4
print(f"After x %= 4: {x}")
print()


# ------------------------------------------------------------------------------
# STEP 3: Comparison (Relational) Operators
# ------------------------------------------------------------------------------
print("--- Step 3: Comparison Operators (Returns Booleans) ---")
m = 10
n = 20

print(f"Is m equal to n? (m == n):          {m == n}")
print(f"Is m NOT equal to n? (m != n):      {m != n}")
print(f"Is m greater than n? (m > n):       {m > n}")
print(f"Is m less than n? (m < n):          {m < n}")
print(f"Is m greater or equal? (m >= 10):   {m >= 10}")
print()


# ------------------------------------------------------------------------------
# STEP 4: Logical Operators
# ------------------------------------------------------------------------------
print("--- Step 4: Logical Operators ---")
high_income = True
good_credit = False

# AND: Returns True only if BOTH conditions are True
print(f"Eligible for loan (AND): {high_income and good_credit}")

# OR: Returns True if AT LEAST ONE condition is True
print(f"Eligible for loan (OR):  {high_income or good_credit}")

# NOT: Reverses the boolean result
print(f"Inverse of good_credit (NOT): {not good_credit}")
print()


# ------------------------------------------------------------------------------
# STEP 5: Identity and Membership Operators
# ------------------------------------------------------------------------------
print("--- Step 5: Identity & Membership Operators ---")

# Identity (is, is not) -> Checks if variables point to the same memory location
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

print(f"list_a == list_b: {list_a == list_b}")  # True (They have the same content)
print(f"list_a is list_b: {list_a is list_b}")  # False (They are separate objects in memory)
print(f"list_a is list_c: {list_a is list_c}")  # True (They point to the exact same object)

# Membership (in, not in) -> Checks if a value exists within a sequence
fruits = ["apple", "banana", "cherry"]
print(f"Is 'banana' in fruits?: {'banana' in fruits}")
print(f"Is 'orange' not in fruits?: {'orange' not in fruits}")
print()


# ------------------------------------------------------------------------------
# STEP 6: Bitwise Operators (Bonus Intermediate Topic)
# ------------------------------------------------------------------------------
print("--- Step 6: Bitwise Operators (Operating on Binary) ---")
# 5 in binary: 0101
# 3 in binary: 0011
p = 5
q = 3

print(f"Bitwise AND (p & q): {p & q}")  # 0101 & 0011 = 0001 (Decimal 1)
print(f"Bitwise OR  (p | q): {p | q}")  # 0101 | 0011 = 0111 (Decimal 7)
print(f"Bitwise XOR (p ^ q): {p ^ q}")  # 0101 ^ 0011 = 0110 (Decimal 6)
print()


# ------------------------------------------------------------------------------
# STEP 7: Operator Precedence (PEMDAS / Order of Operations)
# ------------------------------------------------------------------------------
print("--- Step 7: Operator Precedence ---")

# Python follows a strict order: Parentheses -> Exponents -> Multiplication/Division -> Addition/Subtraction
calculation_1 = 10 + 3 * 2  # Multiplication happens first (3*2 = 6, then 10+6)
calculation_2 = (10 + 3) * 2  # Parentheses happen first (13 * 2)

print(f"10 + 3 * 2 =   {calculation_1}")
print(f"(10 + 3) * 2 = {calculation_2}")

# Combined Logical Precedence: 'not' comes first, then 'and', then 'or'
logic_check = True or False and False  # False and False runs first -> False. Then True or False -> True.
print(f"True or False and False = {logic_check}")
print("==============================================================================")