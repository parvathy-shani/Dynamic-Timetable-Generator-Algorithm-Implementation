import json
import itertools

# Read encoded packets data from file
with open('packets.json', 'r') as packets_file:
    packets_data = json.load(packets_file)


# Read encoded events data from file
with open('events.json', 'r') as events_file:
    events_data = json.load(events_file)



# Generate all possible combinations using itertools.product
all_combinations = list(itertools.product(packets_data, events_data))

#Save all combinations to a new file
file_path = "pairs.json"     # Output file to store the output
with open(file_path, "w") as json_file:  # Open the file to write the output
    json.dump(all_combinations, json_file, indent=4)  # Storing the timeslots into json file
