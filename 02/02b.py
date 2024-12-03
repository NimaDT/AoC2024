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
    reports_for_audit = []
    for report in input:
        if report[0] < report[1]:
            assessment = increaser(report)
            if assessment == True:
                safe_reports.append(report)
            else:
                reports_for_audit.append(report)
        elif report[0] > report[1]:
            assessment = decreaser(report)
            if assessment == True:
                safe_reports.append(report)
            else:
                reports_for_audit.append(report)
        else:
            reports_for_audit.append(report)
    return safe_reports, reports_for_audit

safe_reports, reports_for_audit = safety_checker(int_list)

length_check = len(safe_reports)
print(f"100% safe lists: ", length_check)

# This function should track which reports passes the safety_checker-tests in the problem_dampener
def auditer(input):
    reports_passed = []
    for report in input:
        safe_revisions = problem_dampener(report)
        if safe_revisions:
            reports_passed.append(safe_revisions) 
    return reports_passed

# Checks if reports are safe in safety_checker after a list of reports with one level removed has been generated
def problem_dampener(input): 
    revised_reports_total = []
    revised_reports = revised_report_generator(input)
    safe_revisions, waste = safety_checker(revised_reports)
    if len(safe_revisions) >= 1:
        return safe_revisions

# This function generates a list of reports with one level removed.
def revised_report_generator(input): 
    report_list = []
    for level in range(len(input)):
        report_copy = [x for x in input]
        report_copy.pop(level)
        report_list.append(report_copy)
    return report_list


safe_after_audit = auditer(reports_for_audit)
new_length = length_check + len(safe_after_audit)
print(f"Number of safe reports including safety dampener revisions: ", new_length)
print(f"Number of reports revised", len(safe_after_audit))

