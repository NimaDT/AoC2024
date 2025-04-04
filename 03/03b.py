'''
Read corrupted file and find instructions. do() instructions enable 
Mul() patterns; don't() disable them. Mul pattern may thus only 
be multiplied if enabled by do(). Sum the results of the enabled 
multiplications
'''
import re

# Open input file and asign
with open('03_input.txt') as input_text:
    corrupted_text = input_text.read()

# Split corrupted text for every do() and construct list
do_split = [part for part in corrupted_text.split('do()')]

dont_filtered_out = []

# Split each element of if there's a don't() and discard that element
for part in do_split:
    neo_part = part.split("don't()")
    dont_filtered_out.append(neo_part[0])

print(dont_filtered_out[1])

# Join all remaining elements into new string
rejoined_mul_list = ' '.join(dont_filtered_out)

# Search rejoined string with regex for instructions like mul(1, 5). Save in list.
patterns = re.findall("mul\(\d+,\d+\)", rejoined_mul_list)

mul_list = []

# Search list of patterns with regex to filter the numbers. Put the pairs in separate lists, all in a new list
for ekvation in patterns:
    siffrorna = re.findall("\d+", ekvation)
    mul_list.append(siffrorna)

int_list = []

# Convert number strings to integers
for par in mul_list:
    int_par = [int(x) for x in par]
    int_list.append(int_par)

prod_list = []
# Perform multiplication on each pair. Put in new list
for par in int_list:
    prod = par[0] * par[1]
    prod_list.append(prod)

# Sum list
summan = sum(prod_list)

print(summan)

