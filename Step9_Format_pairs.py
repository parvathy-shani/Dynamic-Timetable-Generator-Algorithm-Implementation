import json

# Create an empty list to store the valid pairs
valid = []

# Load data from data.json
with open('combined_data.json', 'r') as json_file:
    data = json.load(json_file)

# Load data from pairs.json into a Python object
with open('pairs.json', 'r') as pair_file:
    pairs = json.load(pair_file)

# Iterate over each pair in pairs
for pair in pairs:
    room = pair[0][1]
    course = pair[1][1]
    room_batch = room.split('-')[1]
    course_batch = course.split('-')[2]
    room_purpose = room.split('-')[2]
    purpose = False

    # Check each item in data for a match
    for item in data:
        course_code = item["Course code"]
        sem_code = item["Sem code"]
        batch = item["batches"]
        code = f'{course_code}-{sem_code}-{batch}'

        if course == code:
            if item["practical/week"] > 0 and room_purpose == 'o':
                purpose = True
            elif item["lecture/week"] > 0 and room_purpose == 'l':
                purpose = True

    # Check if the room batch matches the course batch and purpose is True
    if room_batch == course_batch and purpose:
        valid.append(pair)

# Save valid pairs to a new file
file_path = "valid_pairs.json"
with open(file_path, "w") as json_file:
    json.dump(valid, json_file, indent=4)
