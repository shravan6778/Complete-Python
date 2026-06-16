
#Declaration & Basic Parameters

'''A function is just a reusable block of code. You **declare** it using the `def` keyword, give it a name, and pass it **parameters** (placeholders for data).'''

def greet_user(username):  # 'username' is a parameter
    print(f"Hello, {username}! Welcome back.")


# Calling the function with an 'argument'
greet_user("Alice")  # "Alice" is the actual argument



#Types of Arguments
'''
Python gives you massive flexibility in how you feed data into functions.

* **Positional Arguments:** Matched based on the order you provide them.
* **Keyword Arguments:** Explicitly named, meaning order doesn't matter.
* **Default Arguments:** Pre-assigned values used if no argument is passed.'''

def describe_pet(pet_name, animal_type="Dog"):  # animal_type has a default value
    print(f"I have a {animal_type} named {pet_name}.")


# Positional (Order matters: "Buddy" goes to pet_name, "Cat" goes to animal_type)
describe_pet("Buddy", "Cat")

# Keyword (Order doesn't matter)
describe_pet(animal_type="Parrot", pet_name="Polly")

# Using the Default Value (Only providing pet_name)
describe_pet("Max")  # Outputs: I have a Dog named Max.


#Arbitrary Functions (`*args` and `kwargs`)

'''What if you don't know how many arguments someone will pass? Python uses magic asterisks to pack inputs into tuples or dictionaries.

* **`*args` (Arbitrary Positional Arguments):** Receives arguments as a **Tuple**.
* **`kwargs` (Arbitrary Keyword Arguments):** Receives arguments as a **Dictionary**.
'''
def make_pizza(size, *toppings):  # *toppings packs extra items into a tuple
    print(f"\nMaking a {size}-inch pizza with:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(12, "mushrooms", "peppers", "extra cheese")


def build_profile(first, last, **user_info):  # **user_info packs items into a dict
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_profile = build_profile("Shahrukh", "Khan", job="Actor", location="Mumbai")
print(user_profile)


# Pass by Value vs. Pass by Reference

'''A common point of confusion: *Does Python pass variables by value or by reference?* The answer is: **Neither.** Python uses a mechanism called **Pass-by-Assignment** (or Object Reference).

* If you pass an **immutable** object (like an integer, string, or tuple), it acts like *Pass-by-Value*. The original variable cannot be changed inside the function.
* If you pass a **mutable** object (like a list or dictionary), it acts like *Pass-by-Reference*. Modifying it inside the function alters the original object outside.
'''
def modify_data(num, my_list):
    num = 100  # Changes locally, original remains untouched
    my_list.append(99)  # Alters the original list in memory!


n = 5
lst = [1, 2, 3]
modify_data(n, lst)

print(f"n: {n}")  # Still 5 (Immutable object)
print(f"lst: {lst}")  # Now [1, 2, 3, 99] (Mutable object)


## Step 5: Recursive Functions

'''A recursive function is simply a function that **calls itself**. To prevent it from looping forever and crashing your system (Stack Overflow), it *must* have a **Base Case** (the exit condition).

Let's look at a classic example: calculating a factorial ($5! = 5 \times 4 \times 3 \times 2 \times 1$).
'''
def factorial(x):
    # 1. Base Case
    if x == 1:
        return 1
    # 2. Recursive Case
    else:
        return x * factorial(x - 1)


print(f"Factorial of 5: {factorial(5)}")


## Step 6: Lambda Functions & Their Common Methods

'''Lambdas are small, anonymous (nameless) one-liner functions. They are used for quick operations where writing a full `def` function would be overkill.

> **Syntax:** `lambda arguments: expression`

Lambdas are almost always paired with built-in functions like `map()` and `filter()`.
'''
# A simple lambda that adds 10 to a number
add_ten = lambda x: x + 10
print(add_ten(5))  # 15

# --- Methods / Use Cases ---
numbers = [1, 2, 3, 4, 5, 6]

# 1. map(function, iterable): Transforms every item in a collection
squared_nums = list(map(lambda x: x**2, numbers))
print(f"Squared: {squared_nums}")  # [1, 4, 9, 16, 25, 36]

# 2. filter(function, iterable): Filters items based on a True/False condition
even_nums = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens:   {even_nums}")  # [2, 4, 6]


##Generators (Clear Breakdown)

### The Concept

'''Imagine you want a million numbers. If you use a normal function with `return`, Python has to calculate all one million numbers, build a massive list in your computer's RAM, and give it to you all at once. If your memory fills up, your program crashes.

A **Generator** is like a chef who hands you one fresh donut at a time only when you say "Next!". It doesn't store a million numbers; it just remembers *where it left off* and calculates the next number on demand. This is incredibly memory-efficient.'''

# Instead of `return`, a generator uses the **`yield`** keyword.

def count_up_to(max_num):
    count = 1
    while count <= max_num:
        yield count  # 'yield' pauses the function and returns the value
        count += 1  # When called again, the function resumes right here!


# Creating the generator object
counter = count_up_to(3)

print(next(counter))  # 1 (Function pauses)
print(next(counter))  # 2 (Function resumes, then pauses again)
print(next(counter))  # 3

# Calling next() again would raise a 'StopIteration' error because the loop ended.
# Alternatively, you can use a clean for-loop, which handles 'next()' automatically:
for num in count_up_to(5):
    print(f"Generator Loop: {num}")

#Decorators (Clear Breakdown)

### The Concept

'''Think of a decorator like a **smartphone case**. Your phone works perfectly fine on its own. However, when you put a case around it, you add extra functionality (like a kickstand or drop protection) without opening up the phone and modifying its internal circuitry.

In Python, a decorator is a function that takes *another function* as an input, wraps some extra behavior around it, and returns the modified function—all without altering the original code.'''

### Why do we need it?
'''
Imagine you have 20 different functions in your program, and you want to measure how much time each one takes to run, or check if a user is logged in before letting them execute that function. Instead of pasting timing/login code into all 20 functions, you write *one* decorator and slap it on top of them.'''

### Step-by-Step Code Construction

# Before understanding the `@` syntax, you must realize that in Python, **functions can be passed around like regular variables.**
# 1. Define the Decorator
def my_decorator(original_function):
    # This wrapper function acts like the phone case
    def wrapper():
        print("Something to do BEFORE the original function runs.")

        original_function()  # Executing your actual function

        print("Something to do AFTER the original function runs.")

    return wrapper  # Return the case, ready to be used


# 2. The Old-School Way to apply it:
def simple_greet():
    print("Hello World!")


# Wrap it manually
decorated_greet = my_decorator(simple_greet)
decorated_greet()
print("\n" + "-" * 40 + "\n")

# 3. The Modern Pythonic Way (Using the '@' symbol syntax)
@my_decorator  # This automatically wraps 'elegant_greet' inside 'my_decorator'
def elegant_greet():
    print("Hello from the decorated world!")


elegant_greet()
### Decorating Functions that Accept Arguments

# If your original function takes arguments (like a name or age), your decorator's internal `wrapper` must be able to accept them too. We use `*args` and `kwargs` inside the wrapper to make it universal:

def universal_decorator(original_func):
    def wrapper(*args, **kwargs):
        print("[LOG]: Function is about to start execution...")
        result = original_func(*args, **kwargs)
        print("[LOG]: Function completed successfully.")
        return result

    return wrapper


@universal_decorator
def greet_with_name(name, age):
    print(f"Hey {name}, you are {age} years old.")


greet_with_name("Rahul", 24)
