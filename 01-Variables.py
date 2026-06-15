# ------------------------------------------------------------------------------
# STEP 1: Basic Assignment & Naming Rules
# ------------------------------------------------------------------------------
print("--- Step 1: Basic Assignment & Naming Rules ---")

# Variables are created the moment you assign a value to them. No declaration needed!
x = 5
user_name = "Alice"  # Snake_case is the standard convention for Python variables

print(f"x: {x}")
print(f"user_name: {user_name}")

# Naming Rules Quick Summary:
# - Must start with a letter or an underscore (e.g., _secret)
# - Cannot start with a number or keyword (e.g., 2vars is invalid)
# - Can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# - Case-sensitive (age, Age, and AGE are three different variables)
print()


# ------------------------------------------------------------------------------
# STEP 2: Python Data Types (Dynamic Typing)
# ------------------------------------------------------------------------------
print("--- Step 2: Data Types & Dynamic Typing ---")

# Python is dynamically typed. You don't need to specify the type, and it can change.
my_variable = 42  # Automatically an Integer (int)
print(f"Value: {my_variable} | Type: {type(my_variable)}")

my_variable = 3.14  # Now it's a Floating Point number (float)
print(f"Value: {my_variable} | Type: {type(my_variable)}")

my_variable = "Hello, World!"  # Now it's a String (str)
print(f"Value: '{my_variable}' | Type: {type(my_variable)}")

my_variable = True  # Boolean (bool)
print(f"Value: {my_variable} | Type: {type(my_variable)}")
print()


# ------------------------------------------------------------------------------
# STEP 3: Multiple Assignment Tricks
# ------------------------------------------------------------------------------
print("--- Step 3: Multiple Assignment ---")

# Assigning many values to multiple variables in one line
a, b, c = 1, 2, "three"
print(f"a: {a}, b: {b}, c: {c}")

# Assigning the same value to multiple variables at once
x = y = z = 100
print(f"x: {x}, y: {y}, z: {z}")

# The Classic Pythonic Swap (No temporary third variable needed!)
first = "Apple"
second = "Banana"
first, second = second, first
print(f"After swap -> first: {first}, second: {second}")
print()


# ------------------------------------------------------------------------------
# STEP 4: Variable Output & Type Casting
# ------------------------------------------------------------------------------
print("--- Step 4: Casting (Changing Types) ---")

# Sometimes you need to explicitly change a variable's type
age_string = "25"
actual_age = int(age_string)  # Converts string to integer
print(f"Next year you will be: {actual_age + 1}")

# Converting number to string for concatenation (though f-strings are preferred)
score = 98
print("Your score is " + str(score) + "%")
print()


# ------------------------------------------------------------------------------
# STEP 5: Variable Scope (Global vs. Local)
# ------------------------------------------------------------------------------
print("--- Step 5: Variable Scope ---")

# A variable created outside of a function is GLOBAL. Anyone can access it.
global_var = "I am everywhere!"


def my_function():
    # A variable created inside a function is LOCAL. Only accessible here.
    local_var = "I belong only to this function!"
    print(f"Inside function: {global_var}")
    print(f"Inside function: {local_var}")


my_function()

# Uncommenting the line below will cause a NameError because local_var isn't accessible here:
# print(local_var)


# Modifying a global variable inside a function requires the 'global' keyword
counter = 0


def increment():
    global counter  # Points Python to the global variable
    counter += 1


increment()
print(f"Global counter after function call: {counter}")
print()


# ------------------------------------------------------------------------------
# STEP 6: Object References & Mutability (Advanced Bonus)
# ------------------------------------------------------------------------------
print("--- Step 6: Object References ---")

# In Python, variables point to objects in memory.
list_one = [1, 2, 3]
list_two = list_one  # list_two doesn't copy the data; it points to the *same* list

list_two.append(4)

print(f"list_one: {list_one}")  # It changed too!
print(f"Are they the same object? {list_one is list_two}")
print("==============================================================================")


a=10
b=a
print(f"a:{a}\nb:{b}")
a=20
print(f"a:{a}\nb:{b}")
