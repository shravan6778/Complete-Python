# ------------------------------------------------------------------------------
# STEP 1: Conditional Statements (if, elif, else)
# ------------------------------------------------------------------------------
print("--- Step 1: Conditional Statements ---")

score = 85

# Python uses indentation (4 spaces) to define blocks of code
if score >= 90:
    print("Grade: A")
elif score >= 80:  # Short for "else if". Checked only if the previous conditions failed.
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:  # Caught if all above conditions are False
    print("Grade: F")

# Short-hand If (Ternary Operator) - Great for quick assignments
status = "Passed" if score >= 70 else "Failed"
print(f"Exam Result Status: {status}\n")


# ------------------------------------------------------------------------------
# STEP 2: The 'while' Loop (Condition-Controlled Iteration)
# ------------------------------------------------------------------------------
print("--- Step 2: While Loops ---")

# A while loop repeats as long as a specified condition remains True
countdown = 3
while countdown > 0:
    print(f"T-minus {countdown}...")
    countdown -= 1  # Crucial: changing the variable to avoid an infinite loop!

print("Blast off!\n")


# ------------------------------------------------------------------------------
# STEP 3: The 'for' Loop (Sequence-Controlled Iteration)
# ------------------------------------------------------------------------------
print("--- Step 3: For Loops & range() ---")

# For loops are used to iterate over a sequence (list, tuple, string, or range)
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like eating {fruit}")

print("\nLooping over a specific range numbers:")
# range(start, stop, step) -> goes up to, but does not include, the 'stop' value
for i in range(1, 10, 2):  # Counts from 1 to 9, skipping by 2s
    print(f"Number: {i}")
print()


# ------------------------------------------------------------------------------
# STEP 4: Loop Control Keywords (break, continue, pass)
# ------------------------------------------------------------------------------
print("--- Step 4: Break, Continue, and Pass ---")

print("Demonstrating 'break' (Exits the loop entirely when a condition is met):")
for number in range(1, 10):
    if number == 5:
        break  # Stops the entire loop immediately
    print(number, end=" ")  # Prints on the same line
print("\n")

print("Demonstrating 'continue' (Skips the current iteration and moves to the next):")
for number in range(1, 6):
    if number == 3:
        continue  # Skips printing 3
    print(number, end=" ")
print("\n\n")

print("Demonstrating 'pass' (A null statement acting as a placeholder):")


def upcoming_feature():
    # 'pass' prevents Python from throwing an IndentationError for an empty block
    pass


print("The 'pass' statement executed successfully without doing anything.\n")


# ------------------------------------------------------------------------------
# STEP 5: Else Clauses in Loops (A Unique Python Feature)
# ------------------------------------------------------------------------------
print("--- Step 5: Loop 'else' Blocks ---")

# An 'else' block after a loop runs ONLY if the loop finished normally
# (i.e., it did NOT hit a 'break' statement).

search_target = "cherry"
items = ["apple", "banana", "orange"]

print(f"Searching for '{search_target}' in items...")
for item in items:
    if item == search_target:
        print("Found it!")
        break
else:
    # This runs because the loop finished without finding 'cherry' and never hit 'break'
    print(f"Sorry, '{search_target}' was not found in the inventory.")
print()


# ------------------------------------------------------------------------------
# STEP 6: Structural Pattern Matching (match-case) (Intermediate Bonus)
# ------------------------------------------------------------------------------
print("--- Step 6: Structural Pattern Matching ---")

# Introduced in Python 3.10+, this is Python's cleaner alternative to switch-case statements
day = "Saturday"

match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("It's a weekday. Time to work!")
    case "Saturday" | "Sunday":
        print("It's the weekend! Relax!")
    case _:  # The underscore acts as a wildcard/default case
        print("That is not a valid day.")

print("==============================================================================")