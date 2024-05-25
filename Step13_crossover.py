import json

# Load parent data from the selection_population.json file
with open('selection_population.json', 'r') as parent_file:
    parent_data = json.load(parent_file)

# Retrieve parent1 data from the loaded JSON
parent1_data = parent_data["parent1"]
parent2_data = parent_data["parent2"]

# Create a dictionary to store the child data
child_data1 = {}
child_data2= {}

# Store the first 15 genes of each chromosome in parent1 as the child data
for batch_key, chromosomes in parent1_data.items():
    child_data1[batch_key] = []
    child_data2[batch_key] = []
    for chromosome in chromosomes:
        child_data1[batch_key].append(chromosome[:15])
        child_data2[batch_key].append(chromosome[15:])

# Store the first 15 genes of each chromosome in parent1 as the child data
for batch_key, chromosomes in parent2_data.items():
    for chromosome in chromosomes:
        child_data2[batch_key].append(chromosome[:15])
        child_data1[batch_key].append(chromosome[15:])



child_file1_path = "child_data1.json"
with open(child_file1_path, "w") as child_file1:
    json.dump(child_data1, child_file1,)

print(f"Child data 1 saved to {child_file1_path}")

# Save child_data2 to a JSON file
child_file2_path = "child_data2.json"
with open(child_file2_path, "w") as child_file2:
    json.dump(child_data2, child_file2,)

print(f"Child data 2 saved to {child_file2_path}")
