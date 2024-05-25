def parse_gene(gene_line):
    parts = gene_line.strip().split()
    timeslot_room = [parts[0], parts[1]]
    staff_subject_class = parts[2:]
    return [timeslot_room, staff_subject_class]

def parse_chromosome(chromosome_lines):
    parsed_chromosome = []
    gene_lines = []
    for line in chromosome_lines:
        if line.strip():  # Check if the line is not empty
            gene_lines.append(line)
        else:
            parsed_chromosome.append(parse_gene_lines(gene_lines))
            gene_lines = []
    # Add the last gene if it exists
    if gene_lines:
        parsed_chromosome.append(parse_gene_lines(gene_lines))
    return parsed_chromosome

def parse_gene_lines(gene_lines):
    parsed_genes = []
    for line in gene_lines:
        parsed_genes.append(parse_gene(line))
    return parsed_genes

def parse_input_file(file_path):
    with open(file_path, 'r') as file:
        chromosome_lines = []
        parsed_data = []
        for line in file:
            if line.strip():
                chromosome_lines.append(line)
            else:
                parsed_data.append(parse_chromosome(chromosome_lines))
                chromosome_lines = []
        # Add the last chromosome if it exists
        if chromosome_lines:
            parsed_data.append(parse_chromosome(chromosome_lines))
    return parsed_data

def write_formatted_initial_population(parsed_data, output_file):
    with open(output_file, 'w') as file:
        for i, chromosome in enumerate(parsed_data, 1):
            file.write(f"Chromosome {i}:\n")
            for j, gene in enumerate(chromosome, 1):
                file.write(f"{gene}\n")

file_path = "initial_population_S8D.txt"
output_file = "formatted_initial_population_S8D.txt"

parsed_data = parse_input_file(file_path)
write_formatted_initial_population(parsed_data, output_file)
