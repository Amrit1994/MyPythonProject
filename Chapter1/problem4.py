import os

# Get the current working directory
# directory_path = os.getcwd()
directory_path = '/Users/amritnarayanjha/PythonProgram'

# Get the list of all entries in the directory
entries = os.listdir(directory_path)

# Print the entries
for entry in entries:
    print(entry)