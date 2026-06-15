# ------------------------------------------------------------------------------
# STEP 1: Numeric Data Types (int, float, complex)
# ------------------------------------------------------------------------------
print("--- Step 1: Numeric Data Types ---")

my_int = 42          # Integer: Whole numbers, positive or negative
my_float = 3.14159   # Float: Numbers with decimal points
my_complex = 2 + 3j  # Complex: Real part (2) and imaginary part (3)

print(f"Integer: {my_int} | Type: {type(my_int)}")
print(f"Float:   {my_float} | Type: {type(my_float)}")
print(f"Complex: {my_complex} | Type: {type(my_complex)}")
print()


# ------------------------------------------------------------------------------
# STEP 2: Text & Boolean Data Types (str, bool)
# ------------------------------------------------------------------------------
print("--- Step 2: Text & Boolean Data Types ---")

my_str = "Python 2026"  # String: Text wrapped in single, double, or triple quotes
is_active = True        # Boolean: True or False (Case-sensitive!)

print(f"String:  '{my_str}' | Type: {type(my_str)}")
print(f"Boolean: {is_active} | Type: {type(is_active)}")
print()


# ------------------------------------------------------------------------------
# STEP 3: Sequence Data Types (list, tuple, range)
# ------------------------------------------------------------------------------
print("--- Step 3: Sequence Data Types ---")

# List: Ordered, mutable (changeable), allows duplicates
my_list = ["apple", "banana", "apple"]

# Tuple: Ordered, immutable (cannot be changed), allows duplicates
my_tuple = ("gold", "silver", "bronze")

# Range: Generates a sequence of numbers (immutable)
my_range = range(1, 5)  # Generates 1, 2, 3, 4

print(f"List:  {my_list} | Type: {type(my_list)}")
print(f"Tuple: {my_tuple} | Type: {type(my_tuple)}")
print(f"Range: {list(my_range)} | Type: {type(my_range)}")
print()


# ------------------------------------------------------------------------------
# STEP 4: Set & Mapping Data Types (set, dict, None)
# ------------------------------------------------------------------------------
print("--- Step 4: Set & Mapping Data Types ---")

# Set: Unordered, unindexed, no duplicate elements allowed
my_set = {1, 2, 3, 3, 3}  # The extra 3s will be ignored

# Dictionary: Unordered key-value pairs, keys must be unique
my_dict = {"name": "Alex", "age": 28}

# NoneType: Represents the absence of a value
empty_val = None

print(f"Set:  {my_set} | Type: {type(my_set)}")
print(f"Dict: {my_dict} | Type: {type(my_dict)}")
print(f"None: {empty_val} | Type: {type(empty_val)}")
print()


# ------------------------------------------------------------------------------
# STEP 5: Implicit Type Conversion (Automatic)
# ------------------------------------------------------------------------------
print("--- Step 5: Implicit Type Conversion ---")

# Python automatically converts one data type to another to prevent data loss.
num_int = 10
num_float = 5.5

# Adding an int and a float automatically results in a float
result = num_int + num_float
print(f"Result: {result} | Automatically converted to Type: {type(result)}")
print()


# ------------------------------------------------------------------------------
# STEP 6: Explicit Type Conversion / Casting (Manual)
# ------------------------------------------------------------------------------
print("--- Step 6: Explicit Type Conversion (Casting) ---")

# 1. String to Integer/Float
age_str = "25"
price_str = "19.99"
age_int = int(age_str)
price_float = float(price_str)
print(f"Casted Int: {age_int} | Casted Float: {price_float}")

# 2. Number to String (Crucial for concatenation)
score = 100
message = "Your score is " + str(score)
print(message)

# 3. Boolean Conversions (The concept of 'Truthy' and 'Falsy')
# Empty sequences, 0, and None convert to False. Everything else is True.
print(f"bool(0): {bool(0)} | bool(42): {bool(42)}")
print(f"bool(''): {bool('')} | bool('Hello'): {bool('Hello')}")

# 4. Collection Conversions (Converting between List, Tuple, and Set)
original_list = [1, 2, 2, 3, 4, 4]
unique_set = set(original_list)    # Removes duplicates
back_to_tuple = tuple(unique_set)  # Converts to an immutable tuple

print(f"Original List:  {original_list}")
print(f"Casted to Set:  {unique_set} (Duplicates gone!)")
print(f"Casted to Tuple:{back_to_tuple}")
print()

# ------------------------------------------------------------------------------
# STEP 7: Error Handling during Casting (Bonus Exception Handling)
# ------------------------------------------------------------------------------
print("--- Step 7: Handling Conversion Errors ---")

invalid_str = "abc"

try:
    # This will fail because "abc" cannot be parsed as a base-10 integer
    number = int(invalid_str)
except ValueError as e:
    print(f"Caught an expected error: Couldn't convert '{invalid_str}' to an integer!")
    print(f"Error Message: {e}")

print("==============================================================================")