import random
import json
import copy

def extract_pair_info(pair):
    timeslot = pair[0][0]
    room = pair[0][1]
    lecturer = pair[1][0]
    course = pair[1][1]
    room_batch = room.split('-')[1]
    purpose = room.split('-')[2]
    code = f'{timeslot} {room} {lecturer} {course}'

    return timeslot, room, lecturer, course, room_batch, purpose, code

def generate_chromosome(pairs, batch):
    chromosome = []
    gene_number = 1
    used_codes = set()

    random_pairs = random.sample(pairs, len(pairs)) #randomly generated pairs

    # Greedy Initialization
    for pair in random_pairs:  #consider one gene from the randomly generated pool
        timeslot, room, lecturer, course, room_batch, purpose, code = extract_pair_info(pair) #extract the relevant data

        if (batch == room_batch) and (code not in used_codes) and (timeslot == f'G{gene_number}'):  #check if the batch for which the chromosome generated is same and the gene hasn't been used yet and the timeslot matches the position
            if purpose == 'o' and (gene_number) % 3 == 1:  #checks whether the purpose if others(lab/project) or lecture
                chromosome.append(pair)
                used_codes.add(code)
                gene_number += 1
                for _ in range(2):
                    new_code = f'G{gene_number} {" ".join(code.split()[1:])}'  # Create new pair with incremented gene number
                    new_pair = copy.deepcopy(pair)  # Create a deep copy of the pair
                    new_pair[0][0] = f'G{gene_number}'
                    chromosome.append(new_pair)
                    used_codes.add(new_code)
                    gene_number += 1
                if gene_number > 30:
                    break
            else:
                # If purpose is not 'o', add random pairs with purpose 'l' for the next three consecutive positions
                if purpose!='o':
                    chromosome.append(pair)
                    used_codes.add(code)
                    gene_number += 1
                    if gene_number > 30:
                        break
            if gene_number > 30:
                break


    return chromosome

#inputting genes
with open('valid_pairs.json', 'r') as pair_file:
    pairs = json.load(pair_file)

batches = ['S2C', 'S2D', 'S4C', 'S4D', 'S6C', 'S6D', 'S8C', 'S8D']  # Names of the batches
num_chromosomes_per_batch = 50  # Number of chromosomes for each batch
batch_chromosomes = {}  # Dictionary to store chromosomes for each batch


for batch in batches:
    batch_chromosomes[batch] = []  # Initialize empty list for each batch
    for _ in range(num_chromosomes_per_batch):
        chromosome = generate_chromosome(pairs, batch)
        batch_chromosomes[batch].append(chromosome)  # Append generated chromosome to the batch list

# Save chromosomes to a new file
file_path = "initial_population.json"
with open(file_path, "w") as json_file:
    json.dump(batch_chromosomes, json_file, indent=4)