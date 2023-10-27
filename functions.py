def most_frequent(input_string):
    # Create an empty dictionary to store letter frequencies
    letter_count = {}

    # Convert the input string to lowercase to make it case-insensitive
    input_string = input_string.lower()

    # Iterate through the characters in the input string
    for char in input_string:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    # Sort the dictionary by values in decreasing order
    sorted_letter_count = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)

    # Print the letters and their frequencies
    for item in sorted_letter_count:
        print(f"{item[0]}={item[1]:02d}")

# Get input from the user
user_input = input("Please enter a string: ")

# Call the most_frequent function with the user's input
most_frequent(user_input)
