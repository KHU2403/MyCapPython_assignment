#task1 to find area of a circle for a given radiu
import math

# Input the radius of the circle from the user
radius = float(input("Input the radius of the circle: "))

# Calculate the area of the circle
area = math.pi * (radius ** 2)

# Display the result
print(f"The area of the circle with radius {radius} is: {area}")

#task2 to print extenssion of a file

# Input the filename from the user
filename = input("Input the Filename: ")

# Split the filename into its base name and extension
base_name, extension = filename.rsplit('.', 1)

# Display the file extension
print(f"The extension of the file is: '{extension}'")
