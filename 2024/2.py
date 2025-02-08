
# Report(list) only safe when continually decreasing or decreasing,
#   with jumps of no more than 3 between nums
def report_safe(report):
    if report[0] < report[1]:
        for i in range(len(report)-1):
            if report[i] >= report[i+1] or (report[i+1]-report[i]) > 3:
                return False
        return True
    if report[0] > report[1]:
        for i in range(len(report)-1):
            if report[i] <= report[i+1] or (report[i]-report[i+1]) > 3:
                return False
        return True
    return False

def dampened_report_safe(report):
    for i in range(len(report)):
        temp_report = report[:]
        temp_report.pop(i)
        if report_safe(temp_report):
            return True
    return False

safe_reports = 0
with open("2024/2.txt", "r") as file:
    for line in file:
        report = [int(x) for x in line.strip().split()]
        if dampened_report_safe(report):
            safe_reports += 1

print(safe_reports)
