"""
This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

- The levels are either all increasing or all decreasing.
- Any two adjacent levels differ by at least one and at most three.
"""

redNoseReports = open("advent_of_code_2024_day_02.txt", "r")

reports = redNoseReports.readlines()

safe = 0

for report in reports:
    # print(f'Report: {report}') # DEBUG
    r = [int(i) for i in report.split(' ')]

    if all(r[i] < r[i+1] and 3 >= abs(r[i] - r[i+1]) >= 1 for i in range(len(r) - 1)) or all(r[i] > r[i+1] and 3 >= abs(r[i] - r[i+1]) >= 1 for i in range(len(r) - 1)):
        safe += 1
# print(f'Safe:  {safe}') # DEBUG

