# ==============================================================================
# THE ULTIMATE PYTHON DICTIONARY (DICT) MASTERCLASS
# ==============================================================================

# ------------------------------------------------------------------------------
# STEP 1: Dictionary Creation
# ------------------------------------------------------------------------------
print("--- Step 1: Creating Dictionaries ---")

# Method A: Using curly braces {} with key: value pairs
# Keys must be immutable (strings, numbers, tuples). Values can be anything!
user_profile = {
    "username": "coder_99",
    "email": "alex@example.com",
    "login_count": 12,
    "is_admin": False,
    "skills": ["Python", "SQL"]  # Values can be lists or even other dicts
}

# Method B: Using the dict() constructor
empty_dict = dict()  # Creates an empty dictionary {}
constructed_dict = dict(name="John", age=30, city="New York")

print(f"User Profile: {user_profile}")
print(f"Constructed Dict: {constructed_dict}")
print()


# ------------------------------------------------------------------------------
# STEP 2: Accessing and Extracting Values
# ------------------------------------------------------------------------------
print("--- Step 2: Accessing Values ---")

# Method A: Using square brackets []
# Note: If the key doesn't exist, this throws a KeyError!
print(f"Username is: {user_profile['username']}")

# Method B: Using the .get() method (Safer!)
# If the key doesn't exist, it returns None (or a default value you specify) instead of crashing.
print(f"Email is: {user_profile.get('email')}")
print(f"Phone (missing key): {user_profile.get('phone_number')}") 
print(f"Role (with custom default): {user_profile.get('role', 'Standard User')}")
print()


# ------------------------------------------------------------------------------
# STEP 3: Modifying, Adding, and Deleting Items
# ------------------------------------------------------------------------------
print("--- Step 3: Modifying, Adding, and Deleting ---")

# Adding a new key-value pair or updating an existing one
user_profile["location"] = "Hyderabad"  # Adds a new key
user_profile["login_count"] = 13         # Updates an existing value
print(f"After addition & update: {user_profile}")

# Removing items
# 1. pop(key): Removes the key and returns its value
removed_email = user_profile.pop("email")
print(f"Removed Email: {removed_email}")

# 2. popitem(): Removes and returns the LAST inserted key-value pair as a tuple
last_item = user_profile.popitem()
print(f"Removed Last Item: {last_item}")

# 3. del keyword: Deletes an entry directly
del user_profile["is_admin"]

print(f"Final state after deletions: {user_profile}")
print()


# ------------------------------------------------------------------------------
# STEP 4: Essential Dictionary Methods
# ------------------------------------------------------------------------------
print("--- Step 4: Essential Dictionary Methods ---")

employee = {"id": 101, "name": "Diana", "department": "HR"}

# .keys() -> Returns a view object of all keys
print(f"Keys:   {list(employee.keys())}")

# .values() -> Returns a view object of all values
print(f"Values: {list(employee.values())}")

# .items() -> Returns a view object of key-value tuples (crucial for looping)
print(f"Items:  {list(employee.items())}")

# .update() -> Merges another dictionary or iterable into this one
employee.update({"department": "Engineering", "salary": 85000})
print(f"After .update(): {employee}")
print()


# ------------------------------------------------------------------------------
# STEP 5: Looping / Iterating through Dictionaries
# ------------------------------------------------------------------------------
print("--- Step 5: Iterating Through Dictionaries ---")

inventory = {"apples": 50, "bananas": 30, "oranges": 25}

print("Looping over KEYS only (default behavior):")
for key in inventory:
    print(f"- {key}")

print("\nLooping over KEYS and VALUES simultaneously using .items():")
for fruit, quantity in inventory.items():
    print(f"We have {quantity} units of {fruit}.")
print()


# ------------------------------------------------------------------------------
# STEP 6: Dictionary Comprehension (Intermediate Bonus)
# ------------------------------------------------------------------------------
print("--- Step 6: Dictionary Comprehension ---")

# A sleek way to create new dictionaries from existing data in one line
numbers = [1, 2, 3, 4, 5]

# Create a dictionary where keys are numbers and values are their squares
squares_dict = {num: num**2 for num in numbers}
print(f"Squares Dictionary: {squares_dict}")

print("==============================================================================")