
import json
import os

# ------------------------------------------------------------------------------
# STEP 1: The Old Way vs. The Modern Way (Context Managers)
# ------------------------------------------------------------------------------
print("--- Step 1: Writing to a File (The Modern Way) ---")

# Traditional Way (Avoid this if possible):
# file = open("sample.txt", "w")
# file.write("Hello")
# file.close() # If an error happens before this line, the file remains locked!

# The Modern Way: Using the 'with' statement (Context Manager)
# It automatically closes the file for you, even if the code crashes inside.
# Mode 'w' = Write mode. It creates the file, or OVERWRITES it if it already exists.

with open("demo_notebook.txt", "w") as file:
    file.write("Line 1: Welcome to Python File Handling.\n")
    file.write("Line 2: Learning to persist data on your hard drive.\n")
    file.write("Line 3: This line will be read later.\n")

print("File 'demo_notebook.txt' created and written to successfully.\n")


# ------------------------------------------------------------------------------
# STEP 2: Reading Files (Three Different Methods)
# ------------------------------------------------------------------------------
print("--- Step 2: Reading Files ---")

# Mode 'r' = Read mode (Default mode if you don't specify one)
print("Method A: Reading the ENTIRE file at once (.read())")
with open("demo_notebook.txt", "r") as file:
    content = file.read()
    print(content)

print("Method B: Reading LINE BY LINE using a loop (Memory Efficient)")
# Highly recommended for massive files so you don't load gigabytes into RAM at once.
with open("demo_notebook.txt", "r") as file:
    for line in file:
        print(f"-> {line.strip()}")  # .strip() removes extra newlines '\n'
print()

print("Method C: Reading all lines into a LIST (.readlines())")
with open("demo_notebook.txt", "r") as file:
    lines_list = file.readlines()
    print(f"As a Python List: {lines_list}")
print()


# ------------------------------------------------------------------------------
# STEP 3: Appending Data (Preserving existing content)
# ------------------------------------------------------------------------------
print("--- Step 3: Appending Data ---")

# Mode 'a' = Append mode. It adds new data to the END of the file without deleting anything.
with open("demo_notebook.txt", "a") as file:
    file.write("Line 4 (Appended): This was added after the file was made!\n")

# Let's verify the change
with open("demo_notebook.txt", "r") as file:
    print(file.read())


# ------------------------------------------------------------------------------
# STEP 4: File Pointer Manipulation (tell and seek)
# ------------------------------------------------------------------------------
print("--- Step 4: Moving the File Pointer (seek/tell) ---")

with open("demo_notebook.txt", "r") as file:
    print(f"Initial cursor position: {file.tell()}")  # tell() tracks where the cursor is
    
    first_chunk = file.read(14)  # Read just the first 14 characters
    print(f"Read Chunk: '{first_chunk}'")
    print(f"Cursor position after reading: {file.tell()}")
    
    # What if we want to reread from the beginning? We must reset the cursor.
    file.seek(0)  # seek(0) moves the cursor back to the very first byte
    print(f"Cursor position after seek(0): {file.tell()}")
    print(f"Rereading first line: {file.readline().strip()}")
print()


# ------------------------------------------------------------------------------
# STEP 5: Working with Structured Data (JSON Files)
# ------------------------------------------------------------------------------
print("--- Step 5: Working with JSON Files ---")

config_data = {
    "app_name": "TaskMaster",
    "version": 2.5,
    "features": ["Cloud Sync", "Dark Mode", "Offline Access"]
}

# Writing Python dictionary to a .json file (Serialization/Dumping)
with open("config.json", "w") as json_file:
    json.dump(config_data, json_file, indent=4)  # indent=4 makes it pretty-printed
print("Saved dictionary config into 'config.json'.")

# Reading a .json file back into a Python dictionary (Deserialization/Loading)
with open("config.json", "r") as json_file:
    loaded_data = json.load(json_file)
    print(f"Loaded JSON back as type: {type(loaded_data)}")
    print(f"App Name: {loaded_data['app_name']}")
print()


# ------------------------------------------------------------------------------
# STEP 6: Clean up / File System Operations (OS Module)
# ------------------------------------------------------------------------------
print("--- Step 6: File Management Operations ---")

# Checking if a file exists before doing operations on it
if os.path.exists("demo_notebook.txt"):
    print("File 'demo_notebook.txt' exists. Cleaning up by deleting it...")
    os.remove("demo_notebook.txt")  # Deletes the file from disk
    os.remove("config.json")
    print("Temporary test files deleted cleanly.")
else:
    print("File not found.")

print("==============================================================================")