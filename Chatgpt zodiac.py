# Define a list of animals in the Chinese zodiac
animals = ['Dragon', 'Snake', 'Horse', 'Sheep', 'Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox', 'Tiger', 'Hare']

# Ask the user for a year
year = int(input("Enter a year: "))

# Calculate the index of the corresponding animal in the list
animal_index = (year - 2000) % 12

# Display the corresponding animal
print("The animal for the year", year, "is", animals[animal_index])
