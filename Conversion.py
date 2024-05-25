import json

# Read the JSON data from the file
with open('child_data1.json', 'r') as file:
    data = json.load(file)


with open('timeslots.json', 'r') as file:
    output_timeslot = json.load(file)

with open('rooms.json', 'r') as file:
    output_room = json.load(file)    #"102-S8D-l": ["102","S8D","lecture"]

with open('lecturers.json', 'r') as file:
    output_lecturer = json.load(file) #"CSAA10n": [["Rosy K Philp"],["Assistant Professor"],["NIL"]],

with open('courses.json', 'r') as file:
    output_course = json.load(file) #"EST102-F-S2C": ["EST102","F","S2C"],




# Function to replace keys with values
#def replace_keys_with_values(data, keys_dict_list):
timetable_batch = 0
generation = {}
for timetables in data.values():
    for timetable in timetables:
        TimeTable = []
        for gene in timetable:
            if gene[0][0] in output_timeslot.keys():
                timeslot = output_timeslot[gene[0][0]]
            if gene[0][1] in output_room.keys():
                room = output_room[gene[0][1]][0]
                batch = output_room[gene[0][1]][1]
            if gene[1][0] in output_lecturer.keys():
                lecturer = output_lecturer[gene[1][0]][0][0]
            if gene[1][1] in output_course.keys():
                course = output_course[gene[1][1]][0]
            slot = f"{timeslot}-{batch}-{room}-{lecturer}-{course}"
            TimeTable.append(slot)
        generation[timetable_batch] = TimeTable
        timetable_batch = timetable_batch + 1

print(generation)




#    for item in sublist:
#        for i in range(len(item)):
#            item[i] = keys_dict_list[i][item[i]] if item[i] in keys_dict_list[i] else item[i]
'''
keys_dict_list = [output_timeslot, output_room, output_lecturer, output_course]

# Replace keys with values in data
replace_keys_with_values(data, keys_dict_list)

# Now data contains values instead of keys
print(data)
'''
