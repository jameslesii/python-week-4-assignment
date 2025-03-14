def read_modify_write(filename, new_filename, modification_func):
    try:
        # Try to open the file for reading
        with open(filename, 'r') as file:
            content = file.read()
            # Apply the modification function
            modified_content = modification_func(content)
            # Write the modified content to a new file
            with open(new_filename, 'w') as new_file:
                new_file.write(modified_content)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied for file '{filename}'")
    except IsADirectoryError:
        print(f"Error: '{filename}' is a directory, not a file.")
    except UnicodeDecodeError:
        print(f"Error: Cannot decode the file content.")
    except Exception as e:
        print(f"Error: {e}. Unable to read or write the files.")


def uppercase_modification(content):
    # Example modification function: converts the content to uppercase
    return content.upper()



def ask_user_for_filename():
    while True:
        filename = input("Enter the filename (including path if necessary): ")
        if not filename.endswith(('.txt', '')):  # Assume .txt for text files
            print("Error: Please enter a filename with a .txt extension or no extension.")
            continue
        try:
            # Ensure the file exists before attempting to read it
            with open(filename, 'r') as file:
                pass
            break
        except FileNotFoundError:
            print("Error: The file does not exist.")
    return filename



def main():
    filename = ask_user_for_filename()
    new_filename = input("Enter the name of the new file (including path if necessary): ")
    new_filename = new_filename.rstrip('.txt') + '.txt'  # Ensure .txt extension for the new file

    # Example modification function: convert all text to uppercase
    modification_func = uppercase_modification

    read_modify_write(filename, new_filename, modification_func)


if __name__ == "__main__":
    main()
