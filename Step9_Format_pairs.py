import json

#create an empty list to store the data
valid = []

# Load data from pairs.json into a Python object
with open('pairs.json', 'r') as pair_file:
    pairs = json.load(pair_file)

    for pair in pairs:
        timeslot = pair[0][0]
        room = pair[0][1]
        course = pair[1][1]
        room_batch = room.split('-')[1]
        course_batch = course.split('-')[2]

        if (room_batch == course_batch):
            valid.append(pair)  # Store valid lines

#Save all combinations to a new file
file_path = "valid_pairs.json"     # Output file to store the output
with open(file_path, "w") as json_file:  # Open the file to write the output
    json.dump(valid, json_file, indent=4)  # Storing the timeslots into json file
