 #Task 1: File Creation
try:
    # Open file in write mode to create it or clear it if it already exists
    with open("my_file.txt", "w") as file:
        # Write at least three lines of text, including a mix of strings and numbers
        file.write("Hello, world!\n")
        file.write("Today is a great day to learn Python.\n")
        file.write("The current count is: 3\n")

    # Task 2: File Reading and Display
    # Open file in read mode to read its contents
    with open("my_file.txt", "r") as file:
        # Read the entire content of the file
        content = file.read()
        # Display the content on the console
        print("File Contents:\n", content)

    # Task 3: File Appending
    # Open file in append mode to add new content
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text
        file.write("Let's append some new lines.\n")
        file.write("Python makes file handling straightforward.\n")
        file.write("Final line of text: 42\n")

    # Re-read and display the updated content
    with open("my_file.txt", "r") as file:
        # Read and print the updated content
        updated_content = file.read()
        print("Updated File Contents:\n", updated_content)

except FileNotFoundError:
    # This block executes if the file does not exist
    print("Error: The file was not found.")
except PermissionError:
    # This block executes if there is a permission error
    print("Error: Permission denied.")
except Exception as e:
    # This block catches other exceptions
    print(f"An unexpected error occurred: {e}")
finally:
    print("Operation complete.")  # This will execute whether or not an exception occurred
