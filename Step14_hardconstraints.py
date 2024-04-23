import json

def hc_lecturer_conflicts(timetable):
    violation_count = 0
    for p1 in timetable:
        for p2 in timetable:
            if p1 != p2 and len(p1) > 1 and len(p2) > 1:  # Added length check
                if p1[1][0] == p2[1][0] and p1[0][0] == p2[0][0]:
                    violation_count += 1
    return violation_count

def hc_class_conflicts(timetable):
    violation_count = 0
    for p1 in timetable:
        for p2 in timetable:
            if p1 != p2 and len(p1) > 0 and len(p2) > 0:  # Added length check
                if len(p1[0]) > 2 and len(p2[0]) > 2:  # Added length check for inner list
                    if p1[0][2] == p2[0][2] and p1[0][0] == p2[0][0]:
                        violation_count += 1
    return violation_count

def calculate_fitness(timetable, weights):
    v1 = hc_lecturer_conflicts(timetable)
    v2 = hc_class_conflicts(timetable)
    total_violation = weights[0] * v1 + weights[1] * v2
    return 1 / (1 + total_violation)

# Read the JSON data from the file
with open('child_data1.json', 'r') as file:
    data = json.load(file)

# Assuming data is a list of timetables
timetables = data

weights = [1, 1]
fitness_scores = []

for timetable in timetables:
    fitness_score = calculate_fitness(timetable, weights)
    fitness_scores.append(fitness_score)

print("Fitness scores:", fitness_scores)
