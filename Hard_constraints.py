import json

# Define the hard constraints as Python functions

def hc_lecturer_conflict(schedule):
    violation_count = 0
    for p1 in schedule:
        for p2 in schedule:
            if p1 != p2:
                if p1[1][0] == p2[1][0] and p1[0][0] == p2[0][0]:
                    violation_count += 1
    return violation_count

def hc_class_conflict(schedule):
    violation_count = 0
    for p1 in schedule:
        for p2 in schedule:
            if p1 != p2:
                if p1[1][2] == p2[1][2] and p1[0][0] == p2[0][0]:
                    violation_count += 1
    return violation_count

def hc_room_capacity(schedule, room_capacity):
    violation_count = 0
    for p in schedule:
        if room_capacity.get(p[1][2]) and len(schedule) > room_capacity[p[1][2]]:
            violation_count += 1
    return violation_count

def hc_lecturer_time_constraints(schedule, lecturer_time_constraints):
    violation_count = 0
    for p in schedule:
        if lecturer_time_constraints.get(p[1][0]) and p[0][0] in lecturer_time_constraints[p[1][0]]:
            violation_count += 1
    return violation_count

def hc_lecturer_time_preferences(schedule, lecturer_time_preferences):
    violation_count = 0
    for p in schedule:
        if lecturer_time_preferences.get(p[1][0]) and p[0][0] < lecturer_time_preferences[p[1][0]]:
            violation_count += 1
    return violation_count

def calculate_fitness(schedule, weights, room_capacity, lecturer_time_constraints, lecturer_time_preferences):
    v1 = hc_lecturer_conflict(schedule)
    v2 = hc_class_conflict(schedule)
    v3 = hc_room_capacity(schedule, room_capacity)
    v4 = hc_lecturer_time_constraints(schedule, lecturer_time_constraints)
    v5 = hc_lecturer_time_preferences(schedule, lecturer_time_preferences)
    total_violation = weights[0] * v1 + weights[1] * v2 + weights[2] * v3 + weights[3] * v4 + weights[4] * v5
    return 1 / (1 + total_violation)

def read_chromosomes(input_file_path):
    chromosomes = []
    with open(input_file_path, 'r') as file:
        chromosome_data = file.read().split('Chromosome ')
        for i, chromosome_str in enumerate(chromosome_data[1:], start=1):
            chromosome_lines = chromosome_str.strip().split('\n')
            schedule = []
            for line in chromosome_lines[1:]:
                if line.strip():
                    schedule_data = line.strip()[3:-1].split("'], ['")
                    schedule.append([slot.split(", ") for slot in schedule_data])
            chromosomes.append(schedule)
    return chromosomes

def write_fitness_scores(chromosomes, fitness_scores, output_file_path):
    with open(output_file_path, 'w') as file:
        for chromosome, fitness in zip(chromosomes, fitness_scores):
            file.write(f"Chromosome: {chromosome}\n")
            file.write(f"Fitness Score: {fitness}\n")
            file.write("\n")

def main():
    input_file_path = "Final_week.txt"
    output_file_path = 'fitness_scores_final_week.txt'
    chromosomes = read_chromosomes(input_file_path)

    weights = [1, 1, 1, 1, 1]  # Adjust weights as needed
    room_capacity = {}  # Populate with room capacities
    lecturer_time_constraints = {}  # Populate with lecturer time constraints
    lecturer_time_preferences = {}  # Populate with lecturer time preferences

    fitness_scores = []
    for chromosome in chromosomes:
        fitness = calculate_fitness(chromosome, weights, room_capacity, lecturer_time_constraints, lecturer_time_preferences)
        fitness_scores.append(fitness)

    write_fitness_scores(chromosomes, fitness_scores, output_file_path)
    print("Fitness scores written to:", output_file_path)

if __name__ == "__main__":
    main()
