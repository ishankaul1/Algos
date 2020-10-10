#Problem: given start and end times of several events (say, meetings), output minimum number of conference rooms needed to schedule all meetings with no overlapping meetings in one conference room.

#approach: sort by start time. get room with the minimum current finish time (priority queue). if the start time of the current meeting is less than the end time of this room's meeting, it means this meeting cannot happen here (or in any of the other rooms). Create a new room with the finish time of current meeting. If the start time was > than the min finish time of a meeting, just put the meeting in that classroom
import heapq


def min_rooms(events):
    events = sorted(events)
    room_finishtimes = [] #keep track of last finish time for each room
    for event in events:
        if len(room_finishtimes) == 0:
            heapq.heappush(room_finishtimes, event[1])
        else:
            min_finishtime = room_finishtimes[0]
            if event[0] >= min_finishtime:
                #start time event > min finishtime; meeting "fits" in room
                heapq.heapreplace(room_finishtimes, event[1])
            else:
                #start time event < min finishtime; push a new room onto the priority queue
                heapq.heappush(room_finishtimes, event[1])

    return len(room_finishtimes)
#if we needed to return optimal scheduling as well as min number of rooms, would have to save 'ids' in order of when we create the rooms, and append start/end times to a defaultdict(list) that holds all the start/end times. priority queue would hold (finish_time, id) tuples

def test1():
    events = [(930, 1100), (930, 1300), (930, 1100), (1100, 1400), (1130, 1300), (1330, 1500), (1330, 1500), (1430, 1700), (1530, 1700), (1530, 1700)]
    print(min_rooms(events))


test1()
