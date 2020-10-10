#Problem: given list of start/end times of jobs, output the maximum length subset of mutually compatible jobs

#greedy solution: order by end time, only take job if start time > last end time


def optJobs(jobs):
    jobs = sorted(jobs, key = lambda x : x[1])
    lastEnd = 0
    opt = []
    print(jobs)
    for job in jobs:
        if job[0] >= lastEnd:
            opt.append(job)
            lastEnd = job[1]

    print(opt)

def test1():
    jobs = [(0, 6), (1, 4), (3, 5), (3, 8), (4, 7), (5, 9), (6, 10), (8, 11)]
    optJobs(jobs)

test1()
