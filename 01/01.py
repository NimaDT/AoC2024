''' Find total distance between left list and right list.

+ Pair up the smallest number in each list, proceeded by the second-smallest and so on.
+ Calculate how far appart the numbers in the pairs are. This i the distance of the pair.
+ Add upp the distances. This is the total distance of the list.
'''
import itertools

raw_list = []

with open('01_input.txt') as input_list:
    for pair in input_list:
        pair = pair.strip("\n")
        raw_list.append(pair)


def splittrad(input_array, output_1, output_2):
    for line in input_array:
        processed_line = line.split("   ")
        output_1.append(processed_line[0])
        output_2.append(processed_line[1])
    return output_1, output_2

left_list = []
right_list = []

left_list, right_list = splittrad(raw_list, left_list, right_list)

neo_left = [int(x) for x in left_list]
neo_right = [int(x) for x in right_list]

neo_left.sort()
neo_right.sort()

# Function for calculating the distances between elements of the left and right lists
def distances(left, right):
    new_list = []
    for (i, j) in zip(left, right):
        distance = max(i - j, j - i)
        new_list.append(distance)
    return new_list

distance_list = distances(neo_left, neo_right)

sum_of_distances = sum(distance_list)
print(sum_of_distances)
