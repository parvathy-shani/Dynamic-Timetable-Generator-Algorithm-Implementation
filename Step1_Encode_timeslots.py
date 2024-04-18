import json

timeslots = {
    'Monday': [
        '09:00am - 10:00am',
        '10:00am - 11:00am',
        '11:00am - 12:00pm',
        '01:00pm - 02:00pm',
        '02:00pm - 03:00pm',
        '03:00pm - 04:00pm'
    ],
    'Tuesday': [
        '09:00am - 10:00am',
        '10:00am - 11:00am',
        '11:00am - 12:00pm',
        '01:00pm - 02:00pm',
        '02:00pm - 03:00pm',
        '03:00pm - 04:00pm'
    ],
    'Wednesday': [
        '09:00am - 10:00am',
        '10:00am - 11:00am',
        '11:00am - 12:00pm',
        '01:00pm - 02:00pm',
        '02:00pm - 03:00pm',
        '03:00pm - 04:00pm'
    ],
    'Thursday': [
        '09:00am - 10:00am',
        '10:00am - 11:00am',
        '11:00am - 12:00pm',
        '01:00pm - 02:00pm',
        '02:00pm - 03:00pm',
        '03:00pm - 04:00pm'
    ],
    'Friday': [
        '09:00am - 09:50am',
        '09:50am - 10:40am',
        '10:40am - 11:30am',
        '11:40am - 12:30pm',
        '02:00pm - 03:00pm',
        '03:00pm - 04:00pm'
    ]
}

# Encode timeslots into gene positions

time_slots = {}  #empty dictionary to store the timeslot with its code sample:'Monday 09:00am - 10:00am': 'G1'
gene_count = 1  #start the gene_count from 1
for day, slots in timeslots.items(): #day contains the day name, say Monday, slots contains the timeslots for the entire day i.e., 09:00 AM to 04:00 PM
    for slot in slots: #slots contains the hourly timing
        time_slots[f'G{gene_count}'] =  f'{day} {slot}'#stores into dictionary
        gene_count += 1 #increment the gene_count

# Stroing the output

file_path = "timeslots.json"     #output file to store the output
with open(file_path, "w") as json_file:  #open the file to write the output
        json.dump(time_slots, json_file, indent=4) #storing the timeslots into json file

