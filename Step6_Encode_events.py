import json
import itertools


# Read encoded lecturers data from file
with open('lecturers.json', 'r') as lecturers_file:
    lecturers_data = json.load(lecturers_file)


# Read encoded courses data from file
with open('courses.json', 'r') as courses_file:
    courses_data = json.load(courses_file)

#taking only the keys
lecturers = lecturers_data.keys()
courses = courses_data.keys()

# Generate all possible combinations using itertools.product
all_combinations = list(itertools.product(lecturers, courses))

#Save all combinations to a new file
file_path = "events.json"     # Output file to store the output
with open(file_path, "w") as json_file:  # Open the file to write the output
    json.dump(all_combinations, json_file, indent=4)  # Storing the timeslots into json file
