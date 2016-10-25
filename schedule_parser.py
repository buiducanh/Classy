AbbToDayIdx = {
        'su': 0,
        'mo': 1,
        'tu': 2,
        'we': 3,
        'th': 4,
        'fr': 5,
        'sa': 6,
        }

def parse_time(time):
    time.strip()
    suffix = time[-2:]
    h, m = map(int, time[:-2].split(':'))
    if suffix.lower() == 'pm' and h < 12:
        h += 12
    return (h, m)

def parse_schedule(input):
    courses = []
    courseInfo = []
    credits = 0
    for line in input:
        course = line.strip().split()
        if not course: continue
        if course[0][0] == '#': continue
        if course[0].lower() == 'course':
            courses.append([])
            courseInfo.append(" ".join(course[1:]))
            if course[-1].isdigit():
                credits += int(course[-1])
        else:
            days = [i.strip()[:2].lower() for i in course[:-2]]
            start, end = map(parse_time, course[-2:])
            for day in days:
                schedule = (AbbToDayIdx[day], start, end)
                courses[-1].append(schedule)
    courseInfo.append(credits)
    return (courses, courseInfo)

from Classy import resolveClassSchedule
import argparse

# defines program's arguments.
parser = argparse.ArgumentParser(description='Resolves your class schedule.')
parser.add_argument('input', type=argparse.FileType('r'))

# parses command line arguments.
args = parser.parse_args()

input = args.input
courses, courseInfo = parse_schedule(input)
print("credits {}".format(courseInfo[-1]))
print(resolveClassSchedule(courses, courseInfo))
