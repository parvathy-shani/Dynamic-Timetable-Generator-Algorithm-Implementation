import random
import json
from collections import Counter


# Function to read data from the input file
def read_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


# Function to generate a single chromosome based on input data and batch
def generate_chromosome(input_data, batch):
    chromosome = []
    gene_number = 1
    available_genes = input_data.copy()  # Make a copy of input data for random sampling
    while gene_number <= 30 and available_genes:  # Ensure we generate up to G30 and have lines available
        gene = random.choice(available_genes)  # Randomly choose a line from available data

        while gene[0][0] != f'G{gene_number}' or batch != gene[1][1][-3:]:
            gene = random.choice(available_genes)

        # available_genes.remove(gene)  # Remove the chosen line from available data

        if gene[0][1][-1] == 'o' and (gene_number - 1) % 6 < 4:
            chromosome.append(gene)
            gene_number += 1

            teacher = gene[1][0]
            room = gene[1][1]

            while gene[0][0] != f'G{gene_number}' or batch != gene[1][1][-3:] or gene[0][1][-1] != 'o' or gene[1][0] != teacher or gene[1][1] != room:
                gene = random.choice(available_genes)
            gene[0][0] == f'G{gene_number}'
            chromosome.append(gene)
            gene_number += 1

            while gene[0][0] != f'G{gene_number}' or batch != gene[1][1][-3:] or gene[0][1][-1] != 'o' or gene[1][
                0] != teacher or gene[1][1] != room:
                gene = random.choice(available_genes)
            chromosome.append(gene)
            gene_number += 1

            continue

        elif gene[0][1][-1] == 'o' and (gene_number - 1) % 6 >= 4:
            continue

        chromosome.append(gene)
        gene_number += 1

        # Check batch and ensure uniqueness

    return chromosome


def check_count_constraint(chromosome):
    possible = True  #initially considers the constraint is satisfied

    event = [] #empty event to store teacher-course pair
    for gene in chromosome:
        event.append(gene[1])  #add the event part of each gene to the event page

    event_counts = Counter(tuple(item) for item in event)


    file_path = 'combined_data.json'
    with open(file_path, 'r') as file:
        courses = json.load(file)

    for event_data in event:
        course_code = event_data[1][:6]  # Extract the first 5 characters of the course code
        lecture_code = event_data[0]

        for course in courses:
            if course["Course code"] == course_code:
                for lecturer in course["lecturers"]:
                    if lecturer["teacher_code"] == lecture_code:
                        if event_counts[(event_data[0], event_data[1])] - course["lecture/week"]:
                            possible == False
                            break

                if not possible:
                    break
        if not possible:
            break

    return possible


# Main function to generate initial population and store it in text files
def main():
    input_data = read_data('valid_pairs.json')
    batches = ['S2C', 'S2D', 'S4C', 'S4D', 'S6C', 'S6D', 'S8C', 'S8D']  # Names of the batches

    for i in range(10):
        set = []
        for batch in batches:
            print(batch)
            chromosomes = []
            z = 0
            while z < 1:
                chromosome = generate_chromosome(input_data, batch)

                if check_count_constraint(chromosome):
                    chromosomes.append(chromosome)
                    z += 1

            set.append(chromosome)

            # Store chromosomes in a text file
        output_file = f'set_{i + 1}.json'
        with open(output_file, 'w') as file:
            json.dump(chromosomes, file, indent=4)


if __name__ == "_main_":
    main()