def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as input_file:
            # Read the content of the file
            content = input_file.read()

            # Modify the content (for example, converting to uppercase)
            modified_content = content.upper()

        # Open the output file in write mode and write the modified content
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)

        print(f"File successfully modified and saved as {output_filename}")
    except FileNotFoundError:
        print(f"The file {input_filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# File names based on your request
input_filename = 'input.txt'
output_filename = 'output.txt'

# Call the function to read, modify, and write the file
read_and_modify_file(input_filename, output_filename)

def read_file_and_handle_errors():
    try:
        # Ask the user for the filename
        filename = input("Enter the filename: ")

        # Try to open the file in read mode
        with open(filename, 'r') as file:
            # Read the content of the file
            content = file.read()
            print(f"Content of {filename}:\n")
            print(content)  # Display the content of the file

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function to prompt the user and handle errors
read_file_and_handle_errors()