# Import necessary modules
#import os                      # Provides functions for interacting with the operating system
from PLP_Ass_Week4 import Person  # Imports the Person class from the PLP_Ass_Week4 module
from file_handling_assignment import handle_file  # Imports the handle_file function for file operations

# Create an instance of the Person class with name, age, and gender attributes
person_two = Person("Eree", 20, "female")

# Call the introduce method to return a description of person_two
# (assuming introduce() returns a string describing the person)
person_two.introduce()

# Read the contents of the "PLP_Ass_Week4.py" file
file_1 = handle_file("PLP_Ass_Week4.py", "read")
# Append text to "file_write.txt" (creates the file if it doesn't exist)
file_2 = handle_file("file_write.txt", "append")

# Print the contents read from "PLP_Ass_Week4.py"
print(file_1)

# Call introduce() again for person_two
person_two.introduce()

# Write the output of introduce() to "about_Eree.txt"
# This saves the person's introduction in a separate file
file_3 = handle_file("about_Eree.txt", "write", person_two.introduce())

# Optional: Delete the "file_write.txt" file after usage (uncomment to use)
# os.remove("file_write.txt")
