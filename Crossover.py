import random

def single_point_crossover(parent1, parent2):
    # Choose a crossover point
    crossover_point = random.randint(1, min(len(parent1), len(parent2)) - 1)

    # Perform crossover
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]

    return child1, child2

# Example usage
parent1 = [[['G1', '412-S6D-o'], ['CSAA02n', 'CSL332-S-S6D']], [['G2', '412-S6D-o'], ['CSAA18n', 'CST308-F-S6D']], [['G3', '412-S6D-o'], ['CSAA23n', 'CSD334-T-S6D']], [['G4', '412-S6D-o'], ['CSAA09n', 'CST308-F-S6D']], [['G5', 'SDP-S6D-o'], ['CSAA04n', 'CST306-C-S6D']], [['G6', 'CL2-S6D-o'], ['CSAA04n', 'CST306-C-S6D']], [['G7', '412-S6D-o'], ['CSAA06n', 'CST362-D-S6D']], [['G8', 'CL1-S6D-o'], ['CSAA22n', 'CSD334-T-S6D']], [['G9', 'CL2-S6D-o'], ['CSAA07n', 'CST306-C-S6D']], [['G10', 'SDP-S6D-o'], ['CSAA21n', 'CSL332-S-S6D']], [['G11', 'CL2-S6D-o'], ['CSAA02n', 'CSL332-S-S6D']], [['G12', 'CL2-S6D-o'], ['CSAA16n', 'CST308-F-S6D']], [['G13', 'CL1-S6D-o'], ['CSAA18n', 'CST302-A-S6D']], [['G14', 'CL1-S6D-o'], ['CSAA06n', 'CST362-D-S6D']], [['G15', 'CL2-S6D-o'], ['CSAA04n', 'CST306-C-S6D']], [['G16', '104-S6D-l'], ['CSAA06n', 'CSD334-T-S6D']], [['G17', '412-S6D-o'], ['CSAA18n', 'CST308-F-S6D']], [['G18', 'CL2-S6D-o'], ['CSAA06n', 'CSD334-T-S6D']], [['G19', '104-S6D-l'], ['CSAA18n', 'CST302-A-S6D']], [['G20', '104-S6D-l'], ['CSAA23n', 'CSD334-T-S6D']], [['G21', '412-S6D-o'], ['CSAA12n', 'CSD334-T-S6D']], [['G22', 'SDP-S6D-o'], ['CSAA07n', 'CST306-C-S6D']], [['G23', 'CL2-S6D-o'], ['CSAA07n', 'CST306-C-S6D']], [['G24', 'CL1-S6D-o'], ['CSAA16n', 'CST308-F-S6D']], [['G25', 'CL2-S6D-o'], ['CSAA06n', 'CSD334-T-S6D']], [['G26', '104-S6D-l'], ['CSAA06n', 'CST362-D-S6D']], [['G27', '412-S6D-o'], ['CSAA18n', 'CST308-F-S6D']], [['G28', '104-S6D-l'], ['CSAA10n', 'CSD334-T-S6D']], [['G29', 'SDP-S6D-o'], ['CSAA12n', 'CSD334-T-S6D']], [['G30', 'SDP-S6D-o'], ['CSAA10n', 'CST308-F-S6D']]]

parent2 = [[['G1', 'CL1-S6D-o'], ['CSAA16n', 'CST308-F-S6D']], [['G2', '412-S6D-o'], ['CSAA20n', 'CSL332-S-S6D']], [['G3', '412-S6D-o'], ['CSAA12n', 'CSD334-T-S6D']], [['G4', 'CL1-S6D-o'], ['CSAA20n', 'CSL332-S-S6D']], [['G5', 'CL2-S6D-o'], ['CSAA10n', 'CSD334-T-S6D']], [['G6', 'SDP-S6D-o'], ['CSAA10n', 'CST308-F-S6D']], [['G7', 'SDP-S6D-o'], ['CSAA13f', 'CST304-B-S6D']], [['G8', 'CL2-S6D-o'], ['CSAA10n', 'CST308-F-S6D']], [['G9', 'SDP-S6D-o'], ['CSAA10n', 'CST308-F-S6D']], [['G10', 'CL2-S6D-o'], ['CSAA18n', 'CST302-A-S6D']], [['G11', '104-S6D-l'], ['CSAA10n', 'CST308-F-S6D']], [['G12', '412-S6D-o'], ['CSAA18n', 'CST302-A-S6D']], [['G13', 'SDP-S6D-o'], ['CSAA06n', 'CST362-D-S6D']], [['G14', 'CL1-S6D-o'], ['CSAA22n', 'CSD334-T-S6D']], [['G15', 'SDP-S6D-o'], ['CSAA02n', 'CSL332-S-S6D']], [['G16', '104-S6D-l'], ['CSAA18n', 'CST308-F-S6D']], [['G17', 'CL2-S6D-o'], ['CSAA09n', 'CST308-F-S6D']], [['G18', 'SDP-S6D-o'], ['CSAA22n', 'CSD334-T-S6D']], [['G19', 'SDP-S6D-o'], ['CSAA06n', 'CSD334-T-S6D']], [['G20', 'CL1-S6D-o'], ['CSAA18n', 'CST302-A-S6D']], [['G21', '104-S6D-l'], ['CSAA23n', 'CSD334-T-S6D']], [['G22', '104-S6D-l'], ['CSAA12n', 'CSD334-T-S6D']], [['G23', 'CL1-S6D-o'], ['CSAA18n', 'CSL332-S-S6D']], [['G24', 'CL2-S6D-o'], ['CSAA16n', 'CSL332-S-S6D']], [['G25', '104-S6D-l'], ['CSAA20n', 'CSL332-S-S6D']], [['G26', '412-S6D-o'], ['CSAA10n', 'CST308-F-S6D']], [['G27', 'CL2-S6D-o'], ['CSAA06n', 'CST362-D-S6D']], [['G28', '412-S6D-o'], ['CSAA10n', 'CST308-F-S6D']], [['G29', 'CL1-S6D-o'], ['CSAA06n', 'CSD334-T-S6D']], [['G30', 'CL1-S6D-o'], ['CSAA04n', 'CST308-F-S6D']]]



child1, child2 = single_point_crossover(parent1, parent2)

print("Parent 1:")
for item in parent1:
    print(item)

print("\nParent 2:")
for item in parent2:
    print(item)

print("\nChild 1:")
for item in child1:
    print(item)

print("\nChild 2:")
for item in child2:
    print(item)

import random

def mutate_child(child):
    # Select two random indices for gene swapping
    idx1, idx2 = random.sample(range(len(child)), 2)
    # Swap the genes at the selected indices
    child[idx1], child[idx2] = child[idx2], child[idx1]
    return child

# Mutate Child 1
mutated_child1 = mutate_child(child1)
print("Mutated Child 1:")
print(mutated_child1)

# Mutate Child 2
mutated_child2 = mutate_child(child2)
print("\nMutated Child 2:")
print(mutated_child2)