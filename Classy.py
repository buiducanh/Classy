IdxToDay = [
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        ]
from Queue import PriorityQueue
def resolveClassSchedule(courses, courseInfo):
    daySchedule = [None for i in IdxToDay]
    dayQueues = [PriorityQueue() for i in IdxToDay]
    for idx, course in enumerate(courses):
        for day, start, end in course:
            if daySchedule[day]:
                if start in daySchedule[day]:
                    print(courseInfo[daySchedule[day][start]])
                    print(courseInfo[idx])
                    return False
                if end in daySchedule[day]:
                    print(courseInfo[daySchedule[day][end]])
                    print(courseInfo[idx])
                    return False
                daySchedule[day][start] = idx
                daySchedule[day][end] = -idx
            else:
                daySchedule[day] = {}
                daySchedule[day][start] = idx
                daySchedule[day][end] = -idx
            dayQueues[day].put(start)
            dayQueues[day].put(end)

    for i in range(len(IdxToDay)):
        flip = [False for course in courses]
        count = 0
        while not dayQueues[i].empty():
            t = dayQueues[i].get()
            toggleIdx = daySchedule[i][t]
            if (toggleIdx > 0) != flip[abs(toggleIdx)]:
                flip[abs(toggleIdx)] = (toggleIdx > 0)
                count += (1 if toggleIdx > 0 else -1)
                if count >= 2:
                    for idx in range(len(flip)):
                        if flip[idx]:
                            print(courseInfo[idx])
                    return False

    return True
