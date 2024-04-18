import json

# Provided classroom data
classrooms_data = [
    {"room_name": "101", "allotted_batch": "S8C", "purpose": "lecture"},
    {"room_name": "102", "allotted_batch": "S8D", "purpose": "lecture"},
    {"room_name": "CC1", "allotted_batch": "S8C", "purpose": "project"},
    {"room_name": "CC2", "allotted_batch": "S8C", "purpose": "project"},
    {"room_name": "412", "allotted_batch": "S8D", "purpose": "project"},
    {"room_name": "SDPK", "allotted_batch": "S8D", "purpose": "project"},
    {"room_name": "103", "allotted_batch": "S6C", "purpose": "lecture"},
    {"room_name": "104", "allotted_batch": "S6D", "purpose": "lecture"},
    {"room_name": "CC1", "allotted_batch": "S6C", "purpose": "mini-project"},
    {"room_name": "CC2", "allotted_batch": "S6C", "purpose": "mini-project"},
    {"room_name": "412", "allotted_batch": "S6D", "purpose": "mini-project"},
    {"room_name": "SDPK", "allotted_batch": "S6D", "purpose": "mini-project"},
    {"room_name": "CL1", "allotted_batch": "S6D", "purpose": "lab"},
    {"room_name": "CL2", "allotted_batch": "S6D", "purpose": "lab"},
    {"room_name": "105", "allotted_batch": "S4C", "purpose": "lecture"},
    {"room_name": "106", "allotted_batch": "S4D", "purpose": "lecture"},
    {"room_name": "CC1", "allotted_batch": "S4C", "purpose": "lab"},
    {"room_name": "CC2", "allotted_batch": "S4C", "purpose": "lab"},
    {"room_name": "CL1", "allotted_batch": "S4D", "purpose": "lab"},
    {"room_name": "CL2", "allotted_batch": "S4D", "purpose": "lab"},
    {"room_name": "107", "allotted_batch": "S2D", "purpose": "lecture"},
    {"room_name": "108", "allotted_batch": "S2C", "purpose": "lecture"}
]

# Function to generate 7-character code for rooms
def generate_code(room_name, allotted_batch, purpose):
    room_code = room_name[:3]  # Extract first three letters of room name
    batch_code = allotted_batch[:3] # Extract first three letters of allotted batch
    purpose_code = 'l' if purpose.lower() == 'lecture' else 'o' # Generate purpose code 'l' for lecture, 'o' for other purposes
    code = f"{room_code}-{batch_code}-{purpose_code}"   # Combine codes to form 7-character code
    return code  # Return the generated code

# Generate codes for each classroom

codes = {}  # Empty dictionary to store the classroom code

for classroom in classrooms_data:
    room_name = classroom["room_name"]
    allotted_batch = classroom["allotted_batch"]
    purpose = classroom["purpose"]
    code = generate_code(room_name, allotted_batch, purpose)  # Function call to generate the code
    codes[code] = [room_name, allotted_batch, purpose]  # Assign code and details to the room_name key in the dictionary

# Save codes to a json file

file_path = "rooms.json"     # Output file to store the output
with open(file_path, "w") as json_file:  # Open the file to write the output
    json.dump(codes, json_file, indent=4)  # Storing the timeslots into json file
