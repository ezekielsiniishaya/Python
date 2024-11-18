#File Handling

#Defining a function that handles all file operations and all errors that may occur

def handle_file(filepath, operation, content = None, mode = None):
    try:
        if operation == 'read':
            #setting mode to read if not specified
            mode = mode if mode else 'r'
            with open(filepath, mode) as file:
                return file.read()
        elif operation == 'write':
            #set mode to write if not specified
            mode = mode if mode else 'w'
            if content is None:
                raise ValueError("Content must be provided for writing.")
            with open(filepath, mode) as file:
                file.write(content)
                print("Content written successfully.")

        elif operation == 'append':
        #setting mode for appending if not specified
            mode = mode if mode else 'a'
            if content is None:
                raise ValueError("Content must be provided for appending.")
            with open(filepath, mode) as file:
                file.write(content)
            print("Content appended sucessfully.")
        else:
            raise ValueError("Invalid operation. Use 'read', 'write', or 'append'. ")

    except FileNotFoundError:
        print(f"Error: The file {filepath} was not found. Please check the file path.")
    except PermissionError:
        print(f"Error: You do not have permission to access the file {filepath}.")
    except ValueError as e:
        #Handles missing content for write/append and invalid operations
        print(f"ValueError: {e}")
    except Exception as e:
        #Catches any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File operation completed.")
#_1 File Creation/writing
#handle_file("my_file.txt", "write", "File handling in Python is pretty straightforward\nI can create, write to and even delete any file I want\nAll I have to do is \n\t1. use the open() function\n\t2. More about this in the future.")

#Displaying content of file to the console.
#print(f"Printing new file\n{handle_file("my_file.txt", "read")}")

#Appending to file
#handle_file("my_file.txt", "append", "\nAs I was saying earlier about file handling in Python.\n\t3. Chose to either open the file for reading, writing, appending or a combination of any\n\t4. Use the goodies that come with the open() function like readline() and write() functions.")

#Displaying content of file to the console after appending
#print(f"Printing file after appending\n{handle_file("my_file.txt", "read")}")