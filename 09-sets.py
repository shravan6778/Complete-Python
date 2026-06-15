# ==============================================================================
# THE ULTIMATE PYTHON SET DATA STRUCTURE MASTERCLASS
# ==============================================================================

# ------------------------------------------------------------------------------
# STEP 1: Set Creation
# ------------------------------------------------------------------------------
print("--- Step 1: Creating Sets ---")

# Method A: Using curly braces {} with comma-separated values
# Notice that duplicate elements are automatically filtered out!
fruits_set = {"apple", "banana", "cherry", "apple", "banana"}
print(f"Fruits Set (Notice no duplicates): {fruits_set}")

# Method B: Creating an EMPTY set
# CRITICAL WARNING: You CANNOT use empty braces '{}' to make an empty set. 
# Doing so creates an empty dictionary! You must use set().
wrong_empty = {}
true_empty = set()
print(f"Type of {{}}: {type(wrong_empty)} | Type of set(): {type(true_empty)}")

# Method C: Converting another collection (like a list) into a set to remove duplicates
numbers_list = [1, 2, 2, 3, 4, 4, 4, 5]
unique_numbers = set(numbers_list)
print(f"List converted to Set: {unique_numbers}")
print()


# ------------------------------------------------------------------------------
# STEP 2: Accessing Set Elements
# ------------------------------------------------------------------------------
print("--- Step 2: Accessing Elements ---")

# Because sets are unordered, elements do not have a fixed position or index.
# You CANNOT access elements using brackets like fruits_set[0] -> (Throws TypeError)

# Method A: Checking membership using the 'in' keyword (Highly optimized / fast)
print(f"Is 'banana' in our set?: {'banana' in fruits_set}")
print(f"Is 'mango' in our set?:  {'mango' in fruits_set}")

# Method B: Iterating through a set using a loop
print("Looping through set items:")
for fruit in fruits_set:
    print(f" - {fruit}")
print()


# ------------------------------------------------------------------------------
# STEP 3: Modifying and Basic Methods
# ------------------------------------------------------------------------------
print("--- Step 3: Set Methods (Add / Remove) ---")

colors = {"red", "green"}

# 1. .add() -> Adds a single element
colors.add("blue")
colors.add("red")  # Adding an existing element does nothing
print(f"After .add(): {colors}")

# 2. .update() -> Adds multiple elements from another set, list, or tuple
colors.update(["yellow", "orange", "green"])
print(f"After .update(): {colors}")

# 3. Removing elements (.remove() vs .discard())
# .remove() throws a KeyError if the element does not exist.
colors.remove("yellow") 

# .discard() is safe! It removes the item, but does nothing if it's missing.
colors.discard("purple")  # "purple" isn't there, but no error is raised.
print(f"After removal operations: {colors}")

# 4. .pop() -> Removes and returns a RANDOM element (since sets are unordered)
popped_item = colors.pop()
print(f"Popped item: {popped_item} | Remaining set: {colors}")
print()


# ------------------------------------------------------------------------------
# STEP 4: Mathematical Set Operations
# ------------------------------------------------------------------------------
print("--- Step 4: Mathematical Set Operations ---")

set_A = {1, 2, 3, 4}
set_B = {3, 4, 5, 6}

print(f"Set A: {set_A}")
print(f"Set B: {set_B}\n")

# 1. UNION: All elements from both sets (Removes duplicates)
# Can use the .union() method or the '|' operator
print(f"Union (A | B):               {set_A | set_B}")

# 2. INTERSECTION: Elements present in BOTH sets
# Can use the .intersection() method or the '&' operator
print(f"Intersection (A & B):        {set_A & set_B}")

# 3. DIFFERENCE: Elements in A that are NOT in B
# Can use the .difference() method or the '-' operator
print(f"Difference (A - B):          {set_A - set_B}")

# 4. SYMMETRIC DIFFERENCE: Elements in A or B, but NOT in both
# Can use the .symmetric_difference() method or the '^' operator
print(f"Symmetric Difference (A ^ B): {set_A ^ set_B}")
print()


# ------------------------------------------------------------------------------
# STEP 5: Set Relationships (Subsets and Supersets)
# ------------------------------------------------------------------------------
print("--- Step 5: Set Relationships ---")

small_set = {1, 2}
large_set = {1, 2, 3, 4}
other_set = {5, 6}

# Check if a set is entirely contained within another set
print(f"Is small_set a subset of large_set?:       {small_set.issubset(large_set)}")

# Check if a set contains all elements of another set
print(f"Is large_set a superset of small_set?:     {large_set.issuperset(small_set)}")

# Check if two sets have completely zero elements in common
print(f"Are large_set and other_set disjoint?:     {large_set.isdisjoint(other_set)}")
print()


# ------------------------------------------------------------------------------
# STEP 6: Set Comprehension (Bonus Intermediate Topic)
# ------------------------------------------------------------------------------
print("--- Step 6: Set Comprehension ---")

# Much like list comprehensions, you can dynamically build sets in one line
# Create a unique set of even numbers squared, filtering out any duplicates automatically
raw_numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6]
even_squares = {x**2 for x in raw_numbers if x % 2 == 0}

print(f"Even Squares Set: {even_squares}")
print("==============================================================================")