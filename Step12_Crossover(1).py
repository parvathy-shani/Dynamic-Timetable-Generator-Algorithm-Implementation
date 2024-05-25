import json
import random

indexes = range(10)

for z in range(10):

    i = random.choice(indexes)
    j = random.choice(indexes)
    while j == i:
        j = random.choice(indexes)

    file_path = f'set_{i+1}.json'
    with open(file_path, 'r') as file:
        data1 = json.load(file)

    file_path = f'set_{i+1}.json'
    with open(file_path, 'r') as file:
        data2 = json.load(file)

    child = []

    for b in range(len(data1)):
        batch = []
        for k in range(30):
            if k % 6 < 3:
                batch.append(data1[b][k])
            else:
                batch.append(data2[b][k])
        
        child.append(batch)

    output_file = f'child_{z+1}.json'
    with open(output_file, 'w') as file:
        json.dump(child, file, indent=4)
    

    