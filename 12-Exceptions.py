'''try: Put code here that has a risk of failing (network requests, user math inputs, reading file assets).

except: Catches specific errors so your entire application doesn't freeze or drop out to the desktop terminal. Always catch specific exceptions rather than a generic except Exception: whenever possible.

else: Runs code that should only execute if the code inside your try block was 100% successful.

finally: The ultimate shield. No matter what crashes above it, this code runs. It is heavily utilized for structural cleanup (closing file streams, wrapping up network connections, or disconnecting active databases).'''

# ------------------------------------------------------------------------------
# Understanding the Difference (Syntax Error vs. Exception)
# ------------------------------------------------------------------------------
# A SyntaxError happens when Python cannot parse your code (e.g., missing a colon).
# Code with a SyntaxError will NOT even start running.
#
# An Exception happens during RUNTIME. The code is written correctly, but something
# goes wrong while executing (e.g., trying to divide by zero).

print("--- Step 1: Basic Exception Handling (ZeroDivisionError) ---")
try:
    # Code that might cause an issue goes inside the 'try' block
    result = 10 / 0
except ZeroDivisionError as e:
    # This block executes ONLY if a ZeroDivisionError occurs
    print(f"Caught a standard exception: You cannot divide by zero!")
    print(f"Details from Python: {e}")
print()


# ------------------------------------------------------------------------------
# Handling Multiple Specific Exceptions
# ------------------------------------------------------------------------------
print("--- Step 2: Handling Multiple Specific Exceptions ---")

def financial_calculator(value_str):
    try:
        # Might throw ValueError if string isn't a number
        number = float(value_str) 
        # Might throw ZeroDivisionError if number is 0
        return 100 / number 
        
    except ValueError:
        print(f"Error: '{value_str}' is not a valid number!")
    except ZeroDivisionError:
        print("Error: Cannot compute calculation using zero!")
    except Exception as e:
        # Generic fallback block for any other unexpected errors
        print(f"An unexpected error occurred: {e}")

financial_calculator("abc")   # Triggers ValueError
financial_calculator("0")     # Triggers ZeroDivisionError
print()


# ------------------------------------------------------------------------------
# The Complete Lifecycle (try, except, else, finally)
# ------------------------------------------------------------------------------
print("--- Step 3: The Complete Exception Lifecycle ---")

def process_file(filename):
    try:
        print(f"Attempting to open file: {filename}")
        file = open(filename, 'r')
        data = file.read()
    except FileNotFoundError:
        print("Exception Block: File does not exist!")
    else:
        # Runs ONLY if the try block succeeded without any exceptions
        print("Else Block: File read successfully!")
        print(f"Data: {data}")
    finally:
        # ALWAYS runs, regardless of whether an exception occurred or not.
        # Perfect for cleanup tasks like closing database connections or files.
        print("Finally Block: Executing mandatory cleanup.")
        # If 'file' was successfully opened, let's close it safely
        if 'file' in locals() and not file.closed:
            file.close()
            print("File explicitly closed.")

# Scenario A: Triggers the Exception and Finally block
process_file("missing_ghost_file.txt")
print("-" * 30)
# Scenario B: Triggers Try, Else, and Finally block (Creating a temporary file to test)
with open("temp_test.txt", "w") as f:
    f.write("Hello from the temp file!")
process_file("temp_test.txt")
print()


# ------------------------------------------------------------------------------
# Raising Exceptions Manually
# ------------------------------------------------------------------------------
print("--- Step 4: Raising Exceptions Manually ---")

def set_user_age(age):
    if age < 0:
        # You can force an exception to happen using the 'raise' keyword
        raise ValueError("Age cannot be a negative number!")
    print(f"Age successfully set to: {age}")

try:
    set_user_age(-5)
except ValueError as e:
    print(f"Caught manually raised exception: {e}")
print()


# ------------------------------------------------------------------------------
# Creating Custom User-Defined Exceptions
# ------------------------------------------------------------------------------
print("--- Step 5: Custom User-Defined Exceptions ---")

# To create a custom exception, inherit from Python's built-in 'Exception' class
class InsufficientFundsError(Exception):
    """Exception raised when a bank account withdrawal exceeds the balance."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        # Pass a clear message to the parent Exception class
        super().__init__(f"Attempted to withdraw ${amount} but balance is only ${balance}")

def withdraw_money(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    current_balance = 500
    print(f"Current Balance: ${current_balance}. Requesting $600...")
    new_balance = withdraw_money(current_balance, 600)
except InsufficientFundsError as e:
    print(f"Transaction Denied! Custom Exception Triggered.")
    print(f"Message: {e}")
    print(f"Shortfall Amount: ${e.amount - e.balance}")

print("==============================================================================")