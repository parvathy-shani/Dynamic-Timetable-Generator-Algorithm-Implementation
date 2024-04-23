import json

with open('elite_population.json', 'r') as elite_file:
    batches_data = json.load(elite_file)

parent_timetable1 = {}
parent_timetable2 = {}

for key in batches_data.keys():
    initial_chromosomes = batches_data[key]
    parent_timetable1[key] = []
    parent_timetable2[key] = []
    for idx, chromosome in enumerate(initial_chromosomes[:2]):
        if idx == 0:
            parent_timetable1[key].append(chromosome)
        else:
            parent_timetable2[key].append(chromosome)

crossover={}
crossover["parent1"] = parent_timetable1
crossover["parent2"] = parent_timetable2
# Save chromosomes to a new file
file_path = "selection_population.json"
with open(file_path, "w") as json_file:
    json.dump(crossover, json_file, indent=4)

