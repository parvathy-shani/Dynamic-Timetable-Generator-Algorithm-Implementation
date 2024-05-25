from collections import Counter
import json

data = {
    'chromosome':
        [[['G1', 'CC2-S4C-o'], ['CSAA10n', 'CST204-C-S4C']],
         [['G2', '105-S4C-l'], ['CSAA17n', 'CST284-m-S4C']],
         [['G3', '105-S4C-l'], ['CSAA15n', 'CST284-h-S4C']],
         [['G4', 'CC1-S4C-o'], ['CSAA17n', 'CST284-h-S4C']],
         [['G5', '105-S4C-l'], ['CSAP01n', 'CST202-B-S4C']],
         [['G6', '105-S4C-l'], ['CSAA11f', 'CSL204-T-S4C']],
         [['G7', 'CC2-S4C-o'], ['CSAP01n', 'CST202-B-S4C']],
         [['G8', '105-S4C-l'], ['CSAA12n', 'EST200-E-S4C']],
         [['G9', 'CC1-S4C-o'], ['CSAA10n', 'CST204-C-S4C']],
         [['G10', 'CC1-S4C-o'], ['CSAA11f', 'CST206-D-S4C']],
         [['G11', 'CC2-S4C-o'], ['CSAA11f', 'CSL204-T-S4C']],
         [['G12', 'CC2-S4C-o'], ['CSAA11f', 'CSL204-T-S4C']],
         [['G13', 'CC2-S4C-o'], ['CSAA16n', 'CST292-m-S4C']],
         [['G14', 'CC1-S4C-o'], ['CSAA13f', 'CSL204-T-S4C']],
         [['G15', '105-S4C-l'], ['CSAA15n', 'CST284-m-S4C']],
         [['G16', '105-S4C-l'], ['CSAA12n', 'EST200-E-S4C']],
         [['G17', '105-S4C-l'], ['CSAA17n', 'CST284-m-S4C']],
         [['G18', 'CC2-S4C-o'], ['CSAA10n', 'CST204-C-S4C']],
         [['G19', '105-S4C-l'], ['CSAP01n', 'CST202-B-S4C']],
         [['G20', 'CC1-S4C-o'], ['CSAA09n', 'CST202-B-S4C']],
         [['G21', 'CC1-S4C-o'], ['CSAA15n', 'CST284-m-S4C']],
         [['G22', 'CC1-S4C-o'], ['CSAA11f', 'CSL204-T-S4C']],
         [['G23', '105-S4C-l'], ['CSAA09n', 'CST202-B-S4C']],
         [['G24', '105-S4C-l'], ['CSAA12n', 'EST200-E-S4C']],
         [['G25', 'CC1-S4C-o'], ['CSAA13f', 'CSL204-T-S4C']],
         [['G26', '105-S4C-l'], ['CSAA17n', 'CST284-h-S4C']],
         [['G27', 'CC2-S4C-o'], ['CSAA09n', 'CST202-B-S4C']],
         [['G28', 'CC1-S4C-o'], ['CSAA13f', 'CSL204-T-S4C']],
         [['G29', 'CC2-S4C-o'], ['CSAA15n', 'CST284-h-S4C']],
         [['G30', '105-S4C-l'], ['CSAP01n', 'CST202-B-S4C']]]
}

event = []
for gene in data['chromosome']:
    event.append(gene[1])
print(f"{event}\n")

# Count occurrences using Counter
event_counts = Counter(tuple(item) for item in event)
print(f"{event_counts}\n")

# Specify the file path
file_path = 'combined_data.json'

# Read the JSON file
with open(file_path, 'r') as file:
    course_data = json.load(file)

# Compare course codes and print matching courses
for event_data in event:
    print(event_data)
    course_code = event_data[1][0]  # Extract the first 5 characters of the course code
    lecture_code = event_data[1]
    for course in course_data:
        if course_code[:5] == course['Course code'][:5]:  # Compare first 5 characters of course codes
            print()

