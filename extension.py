#task2 to print extenssion of a file

# Input the filename from the user
filename = input("Input the Filename: ")

# Split the filename into its base name and extension
base_name, extension = filename.rsplit('.', 1)

# Display the file extension
print(f"The extension of the file is: '{extension}'")
