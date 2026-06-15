#Strings
#1. Creation of the string
s="ABCD"
s='ABCD'
message='''
Hello, 
How are you
'''
print(s)
print(message)
#2.Immutability (why strings are immutable?)
'''1. Memory Efficiency (String Interning)

Python saves memory using a technique called string interning.

If two variables contain the same string, Python may store only one copy of that string in memory and let both variables point to it.

a = "hello"
b = "hello"

print(a is b)   # True

Here, both a and b refer to the same string object.

What if strings were mutable?

Suppose we change a:

a[0] = "y"

Then the shared string "hello" would become "yello".

Since b also points to the same object, b would unexpectedly become "yello" too.

a = "yello"
b = "yello"   # Changed automatically!

This would create confusion and bugs.

Because strings are immutable, Python can safely share the same string object among multiple variables, saving memory.

2. Dictionary Keys and Sets (Hashability)

Strings are commonly used as dictionary keys and set elements.

user_data = {
    "username": "coder_123"
}

Python stores dictionary keys using a value called a hash.

A hash is calculated based on the string's content.

For example:

hash("username")
Problem if strings were mutable

Imagine:

key = "username"

Python calculates a hash for "username" and stores data using that hash.

Now suppose the string changes to:

key = "user"

The hash value would also change.

Python would no longer know where the original data is stored, making dictionary lookups unreliable.

Because strings cannot change, their hash value never changes, making them perfect dictionary keys.

3. Security and Predictability

Strings are often used to store important information such as:

File paths
Database URLs
Usernames
Passwords
Network addresses
Environment variables

Example:

file_path = "/home/data/report.txt"

Suppose your program checks whether this path is valid.

If strings were mutable, another piece of code could change the path after validation:

"/home/data/report.txt"

could become

"/home/data/secret.txt"

This could cause security problems or unexpected behavior.

Since strings are immutable, once a string is validated, Python guarantees that its contents will remain the same.

This makes programs more predictable and secure.

4. Thread Safety

In multi-threaded programs, multiple threads may access the same data simultaneously.

Example:

Thread A reads a string.
Thread B reads the same string.

Because strings cannot be modified, both threads can safely read the same string at the same time.

message = "Welcome"

No thread can accidentally change "Welcome" while another thread is reading it.

If strings were mutable, programmers would need extra synchronization (locks) to prevent data corruption.

Immutability makes concurrent programming simpler and safer.

How Do We "Modify" a String?

Since strings cannot be changed directly, Python creates a new string whenever you modify one.

Example:

text = "Python 3"

text = text.replace("3", "4")

print(text)

Output:

Python 4

What actually happens:

Original string: "Python 3"
Python creates a new string: "Python 4"
The variable text is updated to refer to the new string.

The old string remains unchanged.'''


text="ABCD"
#text[1]="a" #Type Error

# 3.Indexing
word="python"
print(word[1])
#4.Iterable
for i in word:
    print(i)
    
#String Operations
#1. Slicing -- String[Start:End:Step]
t="Python"
print(t[0:6:2])
print(t[0:4])
print(t[2:])
print(t[:4])
print(t[::1])
print(t[::-1]) #reversing a string

#2.Repition
print("A"*5)
#3.Concatenation
s1='A'
s2='b'
print(s1+s2)

#String inbuilt functions

t1='pyTHon'
t2='python is a programming language'
print(t1.upper())
print(t1.lower())
print(t1.capitalize())
print(t2.title())
print(t1.swapcase())

#Searching
print(t1.find("T"))
print(t1.index("H"))

#replace and split
t3="Hello World"
print(t3.replace("World","Python"))
print(t3.split())

#Checking Methods
t4="abc123"
print(t4.isalpha())
print(t4.isdigit())
print(t4.isalnum())
print(t4.startswith("H"))
print(t4.endswith("3"))

#join
t5=["Hello ","hello "]
print("world".join(t5))

#Strip
t6="  Hello "
print(t6.strip())