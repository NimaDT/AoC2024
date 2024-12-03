'''
Analyze the reports from the fusion/fission plant.

+ Safe reports are all increasing or decreasing in level
+ No two adjacent levels in the reports may differ more than three but have to differ by at least one
+ Count the number of safe reports
'''
import itertools

raw_list = []

with open("02_input.txt") as input_text:
    for report in input_text:
        report = report.strip('\n')
        raw_list.append(report)

stripped_list = [x.split(' ') for x in raw_list]

def intmaker(input):
    output = []
    for x in input:
        korn = [int(x) for x in x]
        output.append(korn)
    return output

int_list  = intmaker(stripped_list)

def increaser(input):
    statement = all(earlier < later for earlier, later in zip(input, input[1:]))
    if statement == True:
        for level in range(len(input) - 1):
            if input[level + 1] - input[level] > 3:
                return False
            else:
                continue
        return True
   else:
        return False


def decreaser(input):
    statement = all(earlier > later for earlier, later in zip(input, input[1:]))
    if statement == True:
        for level in range(len(input) - 1):
            if input[level] - input[level + 1] > 3:
                return False
            else:
                continue
        return True
   else:
        return False



def safety_checker(input):
    safe_reports = []
    for report in input:
        if report[0] < report[1]:
            assessment = increaser(report)
            if assessment == True:
                safe_reports.append(report)
        elif report[0] > report[1]:
            assessment = decreaser(report)
            if assessment == True:
                safe_reports.append(report)
        else:
            continue
    return safe_reports

safe_reports = safety_checker(int_list)

length_check = len(safe_reports)
print(length_check)
