''' Find total similarity score between left list and right list.
+ Similarity score is calulated by multiplying each number in the left list by the number of times it appears in the right list

+ Solution is the sum of all the similarity scores
'''
import itertools

raw_list = []

# Read input file
with open('01_input.txt') as input_list:
    for pair in input_list:
        pair = pair.strip("\n")
        raw_list.append(pair)

# Function for splitting each row of the input file
def splittrad(input_array, output_1, output_2):
    for line in input_array:
        processed_line = line.split("   ")
        output_1.append(processed_line[0])
        output_2.append(processed_line[1])
    return output_1, output_2

left_list = []
right_list = []

left_list, right_list = splittrad(raw_list, left_list, right_list)

# Convert items in lists from strings to integers
neo_left = [int(x) for x in left_list]
neo_right = [int(x) for x in right_list]

# Sort lists
neo_left.sort()
neo_right.sort()

# Make dicitionary of all the elements in the left list and their corresponding occurances in the right list
occurance_count = {x: neo_right.count(x) for x in neo_left}

# Function for calculating the similarity score for each element in the left list
def similarities(left, right):
    new_list = []
    for (i, j) in zip(left, right):
        similarity = i * j
        new_list.append(similarity)
    return new_list

# Make a list of the number of occurances in the right list of the elements of the left list
right_values = list(occurance_count.values())

similarity_list = similarities(neo_left, right_values)

# Calculate total similarity score
similarity_score = sum(similarity_list)
print(similarity_score)
