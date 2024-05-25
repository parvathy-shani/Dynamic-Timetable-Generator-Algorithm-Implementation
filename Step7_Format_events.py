import json

# Load data from data.json
with open('combined_data.json', 'r') as json_file:
    data = json.load(json_file)

# Load teacher-course mapping from events.json
with open('events.json', 'r') as event_file:
    teacher_course_mapping = json.load(event_file)


valid_events = []
#invalid_events = []

for mapping in teacher_course_mapping:
    teacher_code, course_info = mapping[0], mapping[1]
    found = False
    for course in data:
         if course_info.startswith(course['Course code']):
             sem_code = course_info.split('-')[1]
             batch = course_info.split('-')[2]
             if any(teacher['teacher_code'] == teacher_code for teacher in course['lecturers']):
                 valid_event = mapping
                 valid_events.append(valid_event)
                 found = True
                 break


#Save all combinations to a new file
file_path = "valid_events.json"     # Output file to store the output
with open(file_path, "w") as json_file:  # Open the file to write the output
    json.dump(valid_events, json_file, indent=4)  # Storing the timeslots into json file

