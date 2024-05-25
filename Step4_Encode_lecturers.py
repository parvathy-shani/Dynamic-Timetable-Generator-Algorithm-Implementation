import json

# Sample input data
lecturer_data = [
    {"lecturer": "Gopakumar G", "position": "Associate Professor", "preferred_timeslot": "NIL"},
    {"lecturer": "Ameena A", "position": "Assistant Professor", "preferred_timeslot": "NIL"},
    {"lecturer": "Manju S Nair", "position": "Associate Professor", "preferred_timeslot": "Forenoon"},
    {"lecturer": "Alka Vijay", "position": "Assistant Professor", "preferred_timeslot": "NIL"},
    {"lecturer": "Shyama Das", "position": "Professor", "preferred_timeslot": "Forenoon"},
    {"lecturer": "Shiny B", "position": "Assistant Professor", "preferred_timeslot": "NIL"},
    {"lecturer": "Sreelekshmi K R", "position": "Assistant Professor", "preferred_timeslot": "NIL"},
    {"lecturer": "Arathy U P", "position": "Assistant Professor", "preferred_timeslot": "NIL"},
    {"lecturer": "Angel Thankam Thomas", "position": "Assistant Professor", "preferred_timeslot": "NIL"},
    {"lecturer": "Rosy K Philp", "position": "Assistant Professor", "preferred_timeslot": "NIL"},
    {"lecturer": "Jithy John", "position": "Assistant Professor", "preferred_timeslot": "Forenoon"},
    {"lecturer": "Sabhana Mol S", "position": "Assistant Professor", "preferred_timeslot": "NIL"},
    {"lecturer": "Jyothirmayi Devi", "position": "Assistant Professor", "preferred_timeslot": "Forenoon"},
    {"lecturer": "Vishnu S Kumar", "position": "Assistant Professor", "preferred_timeslot": "NIL"},
    {"lecturer": "Leya G", "position": "Assistant Professor", "preferred_timeslot": "NIL"},
    {"lecturer": "Betty James", "position": "Assistant Professor", "preferred_timeslot": "NIL"},
    {"lecturer": "Sulaja Sanal", "position": "Assistant Professor", "preferred_timeslot": "NIL"},
    {"lecturer": "Nasseena N", "position": "Assistant Professor", "preferred_timeslot": "NIL"},
    {"lecturer": "Ajoy Thomas", "position": "Assistant Professor", "preferred_timeslot": "NIL"},
    {"lecturer": "Anjitha P", "position": "Assistant Professor", "preferred_timeslot": "NIL"},
    {"lecturer": "Neethu Treesa Jacob", "position": "Assistant Professor", "preferred_timeslot": "NIL"},
    {"lecturer": "Syeatha Merlin Thampy", "position": "Assistant Professor", "preferred_timeslot": "NIL"},
    {"lecturer": "Sheerna Thampi", "position": "Assistant Professor", "preferred_timeslot": "NIL"},
    {"lecturer": "Chinchu M Pillai", "position": "Assistant Professor", "preferred_timeslot": "NIL"},
    {"lecturer": "Sushitha Susan Jacob", "position": "Assistant Professor", "preferred_timeslot": "NIL"},
    {"lecturer": "Ahammed Siraj K K", "position": "Associate Professor", "preferred_timeslot": "NIL"},
]

lecturer_codes = {}  # dict to store the lecturer codes

# Generate codes based on the given rules, the rules
department_code = 'CS'
position_mapping = {
    'Professor': 'PP',
    'Associate Professor': 'AP',
    'Assistant Professor': 'AA'
}

for idx, lecturer_info in enumerate(lecturer_data):
    lecturer = lecturer_info['lecturer']
    position = lecturer_info['position']
    position_code = position_mapping.get(position, 'AA')  # Default to Assistant Professor if position not found
    order_code = str(idx + 1).zfill(2)  # Adding 1 to index since index starts from 0, and then zero padding
    preference = lecturer_info['preferred_timeslot']
    preference_code = 'n' if preference == 'NIL' else 'f'  # Assuming 'n' for NIL preference, 'f' for Forenoon
    code = f"{department_code}{position_code}{order_code}{preference_code}"
    lecturer_codes[code] = [[lecturer], [position], [preference]]

# Save codes to a json file
file_path = "lecturers.json"  # Output file to store the output
with open(file_path, "w") as json_file:  # Open the file to write the output
    json.dump(lecturer_codes, json_file, indent=4)  # Storing the timeslots into json file
