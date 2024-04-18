import json
from collections import Counter

def check_count_constraint(chromosome):
    event = []  # empty event to store teacher-course pair
    processed_courses = set()  # to keep track of processed course codes

    for gene in chromosome:
        event.append(gene[1][1][:6])

    courses_counts = Counter(event)  # counts the number of occurrences of a single subject

    file_path = 'combined_data.json'
    with open(file_path, 'r') as file:
        courses = json.load(file)
    total_deviation = 0
    for course_code in event:
        for course in courses:
            if course["Course code"] == course_code and course_code not in processed_courses:
                processed_courses.add(course_code)
                deviation = courses_counts[course_code] - (course["lecture/week"] + course["tutorial/week"] + course["practical/week"])
                total_deviation += deviation


    return total_deviation

# Load JSON data from the file
with open('initial_population.json', 'r') as batches_file:
    batches_data = json.load(batches_file)

elite_group={}
# Iterate through the keys and access the nested lists
for key in batches_data.keys():
    initial_chromosomes = batches_data[key]

    # Iterate through the nested lists and print their elements
    chromosome_collection = []
    for chromosome in initial_chromosomes:
        deviation = check_count_constraint(chromosome)
        if deviation >0 and deviation < 15 :
            chromosome_collection.append(chromosome)
    elite_group[key] = chromosome_collection
    print(key, len(elite_group[key]))
# Save chromosomes to a new file
file_path = "elite_population.json"
with open(file_path, "w") as json_file:
    json.dump(elite_group, json_file, indent=4)