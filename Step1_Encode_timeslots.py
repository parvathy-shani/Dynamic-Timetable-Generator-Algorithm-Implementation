import json

timeslots = [
    {"day": "Monday", "startTime": "09:00", "endTime": "10:00"},
    {"day": "Monday", "startTime": "10:00", "endTime": "11:00"},
    {"day": "Monday", "startTime": "11:00", "endTime": "12:00"},
    {"day": "Monday", "startTime": "01:00", "endTime": "02:00"},
    {"day": "Monday", "startTime": "02:00", "endTime": "03:00"},
    {"day": "Monday", "startTime": "03:00", "endTime": "04:00"},
    {"day": "Tuesday", "startTime": "09:00", "endTime": "10:00"},
    {"day": "Tuesday", "startTime": "10:00", "endTime": "11:00"},
    {"day": "Tuesday", "startTime": "11:00", "endTime": "12:00"},
    {"day": "Tuesday", "startTime": "01:00", "endTime": "02:00"},
    {"day": "Tuesday", "startTime": "02:00", "endTime": "03:00"},
    {"day": "Tuesday", "startTime": "03:00", "endTime": "04:00"},
    {"day": "Wednesday", "startTime": "09:00", "endTime": "10:00"},
    {"day": "Wednesday", "startTime": "10:00", "endTime": "11:00"},
    {"day": "Wednesday", "startTime": "11:00", "endTime": "12:00"},
    {"day": "Wednesday", "startTime": "01:00", "endTime": "02:00"},
    {"day": "Wednesday", "startTime": "02:00", "endTime": "03:00"},
    {"day": "Wednesday", "startTime": "03:00", "endTime": "04:00"},
    {"day": "Thursday", "startTime": "09:00", "endTime": "10:00"},
    {"day": "Thursday", "startTime": "10:00", "endTime": "11:00"},
    {"day": "Thursday", "startTime": "11:00", "endTime": "12:00"},
    {"day": "Thursday", "startTime": "01:00", "endTime": "02:00"},
    {"day": "Thursday", "startTime": "02:00", "endTime": "03:00"},
    {"day": "Thursday", "startTime": "03:00", "endTime": "04:00"},
    {"day": "Friday", "startTime": "09:00", "endTime": "09:50"},
    {"day": "Friday", "startTime": "09:50", "endTime": "10:40"},
    {"day": "Friday", "startTime": "10:40", "endTime": "11:30"},
    {"day": "Friday", "startTime": "11:40", "endTime": "12:30"},
    {"day": "Friday", "startTime": "02:00", "endTime": "03:00"},
    {"day": "Friday", "startTime": "03:00", "endTime": "04:00"}
]


time_slots = {}  # empty dictionary to store the timeslot with its code sample:'Monday 09:00am - 10:00am': 'G1'
gene_count = 1  # start the gene_count from 1

for slot in timeslots:
    day = slot["day"]
    start_time = slot["startTime"]
    end_time = slot["endTime"]
    time_slots[f'G{gene_count}'] = f'{day} {start_time} - {end_time}'  # stores into dictionary
    gene_count += 1  # increment the gene_count

# Storing the output
file_path = "timeslots.json"  # output file to store the output

with open(file_path, "w") as json_file:  # open the file to write the output
    json.dump(time_slots, json_file, indent=4)  # storing the timeslots into json file
