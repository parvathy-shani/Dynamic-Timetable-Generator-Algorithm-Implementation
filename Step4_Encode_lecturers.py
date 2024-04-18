import json

# Sample input data
lecturer_data = {
    'lecturer': ['Gopakumar G', 'Ameena A', 'Manju S Nair', 'Alka Vijay', 'Shyama Das', 'Shiny B', 'Sreelekshmi K R',
                 'Arathy U P', 'Angel Thankam Thomas', 'Rosy K Philp', 'Jithy John', 'Sabhana Mol S', 'Jyothirmayi Devi',
                 'Vishnu S Kumar', 'Leya G', 'Betty James', 'Sulaja Sanal', 'Nasseena N', 'Ajoy Thomas', 'Anjitha P',
                 'Neethu Treesa Jacob', 'Syeatha Merlin Thampy', 'Sheerna Thampi', 'Chinchu M Pillai', 'Sushitha Susan Jacob',
                 'Ahammed Siraj K K'],
    'position': ['Associate Professor', 'Assistant Professor', 'Associate Professor & Head Of the Department',
                 'Assistant Professor', 'Professor', 'Assistant Professor', 'Assistant Professor', 'Assistant Professor',
                 'Assistant Professor', 'Assistant Professor', 'Assistant Professor', 'Assistant Professor', 'Assistant Professor',
                 'Assistant Professor', 'Assistant Professor', 'Assistant Professor', 'Assistant Professor', 'Assistant Professor',
                 'Assistant Professor', 'Assistant Professor', 'Assistant Professor', 'Assistant Professor', 'Assistant Professor',
                 'Assistant Professor', 'Assistant Professor', 'Associate Professor'],
    'preferred_timeslot': ['NIL', 'NIL', 'Forenoon', 'NIL', 'Forenoon', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'Forenoon', 'NIL',
                           'Forenoon', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL', 'NIL']
}

# Encode lecturer positions
lecturer_codes = {}  # dict to store the lecturer codes

# Generate codes based on the given rules, the rules
department_code = 'CS'
position_mapping = {
    'Professor': 'PP',
    'Associate Professor': 'AP',
    'Assistant Professor': 'AA'
}

for idx, lecturer in enumerate(lecturer_data['lecturer']):  #idx = index position lecturer= data
    position = lecturer_data['position'][idx] 
    position_code = position_mapping.get(position, 'AA')  # Default to Assistant Professor if position not found
    order_code = str(idx + 1).zfill(2)  # Adding 1 to index since index starts from 0, and then zero padding
    preference = lecturer_data['preferred_timeslot'][idx]
    preference_code = 'n' if preference == 'NIL' else 'f'  # Assuming 'n' for NIL preference, 'f' for Forenoon
    code = f"{department_code}{position_code}{order_code}{preference_code}"
    lecturer_codes[code] = [[lecturer],[position],[preference]]


# Save codes to a json file

file_path = "lecturers.json"     # Output file to store the output
with open(file_path, "w") as json_file:  # Open the file to write the output
    json.dump(lecturer_codes, json_file, indent=4)  # Storing the timeslots into json file
