'''
Read corrupted file and find instructions. Match pattern like 'mul(1 ,4)'. 
Elements in each mul should be multiplied. Sum the results of the multiplications
'''
import re

# Open input file and asign
with open('03_in.txt') as input_text:
    corrupted_text = input_text.read()
    
# Search corrupted text with regex for instructions like mul(1, 5). Save in list.
patterns = re.findall("mul\(\d+,\d+\)", corrupted_text)

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

