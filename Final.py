import json

def read_timetable_from_file(file_path):
    timetable = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(':')
                time_slot = parts[0].strip()
                events = [event.strip().split(',') for event in parts[1:]]
                timetable[time_slot] = events
    return timetable

def check_teacher_conflicts(timetables):
    teacher_counts = {}
    teachers = []
    for timetable in timetables.values():
        t = []
        for slot in timetable:
            t.append(slot[1][0])
        teachers.append(t)

    print(teachers)

    conflict_counts = 0
    for i in (range(len(teachers[0]))):
        visited = []
        for slot in teachers:
            #print(slot)
            if slot[i] in visited:
                conflict_counts += 1
            else:
                visited.append((slot[i]))

    return conflict_counts

# Example usage
file_path = 'Final_week.json'

with open(file_path, 'r') as file:
    timetables = json.load(file)

conflict_counts = check_teacher_conflicts(timetables)

print(conflict_counts)
