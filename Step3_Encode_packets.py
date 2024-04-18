import json
import itertools


# Read encoded timeslots data from file
with open('timeslots.json', 'r') as timeslots_file:
    timeslots_data = json.load(timeslots_file)


# Read encoded rooms data from file
with open('rooms.json', 'r') as rooms_file:
    rooms_data = json.load(rooms_file)

#taking only the keys
timeslots = timeslots_data.keys()
rooms = rooms_data.keys()

# Generate all possible combinations using itertools.product
all_combinations = list(itertools.product(timeslots, rooms))

#Save all combinations to a new file
file_path = "packets.json"     # Output file to store the output
with open(file_path, "w") as json_file:  # Open the file to write the output
    json.dump(all_combinations, json_file, indent=4)  # Storing the timeslots into json file
