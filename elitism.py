# Read fitness scores from the text file
def read_fitness_scores(file_path):
    chromosomes = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 3):
            chromosome_str = lines[i] + lines[i+1] + lines[i+2]
            chromosomes.append(chromosome_str)
    return chromosomes

# Apply elitism to the fitness scores
def apply_elitism(chromosomes, elite_count):
    chromosomes.sort(key=lambda x: float(x.split("Fitness Score: ")[1]), reverse=True)
    elite_chromosomes = chromosomes[:elite_count]
    return elite_chromosomes

# Write elite chromosomes to a text file
def write_elite_chromosomes(elite_chromosomes, output_file_path):
    with open(output_file_path, 'w') as file:
        for elite_chromosome in elite_chromosomes:
            file.write(elite_chromosome.strip() + '\n')

# Main function
def main():
    input_file_path = "fitness_scores_S8D.txt"
    output_file_path = "elite_chromosomes_S8D.txt"
    elite_count = 5  # Example: You can adjust the number of elite individuals as needed

    # Read fitness scores from the text file
    chromosomes = read_fitness_scores(input_file_path)

    # Apply elitism
    elite_chromosomes = apply_elitism(chromosomes, elite_count)

    # Write elite chromosomes to a new text file
    write_elite_chromosomes(elite_chromosomes, output_file_path)
    print("Elite chromosomes written to:", output_file_path)

if __name__ == "__main__":
    main()
