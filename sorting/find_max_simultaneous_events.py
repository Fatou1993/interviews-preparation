from collections import namedtuple

Event = namedtuple("Event", ("start", "finish"))
Endpoint = namedtuple('Endpoint', ('time', 'is_start'))

def find_max_simultaneous_events(events):
    endpoints = []
    for event in events:
        endpoints += [Endpoint(event.start, True), Endpoint(event.finish, False)]
    endpoints.sort(key = lambda x : (x.time, not x.is_start))
    max_simultaneous_events = simultaneous_events = 0
    for endpoint in endpoints :
        if endpoint.is_start :
            simultaneous_events+=1
            max_simultaneous_events = max(max_simultaneous_events, simultaneous_events)
        else:
            simultaneous_events-=1
    return max_simultaneous_events

if __name__ == "__main__":
    events = [Event(1,5), Event(2,7), Event(4,5), Event(6,10), Event(8,9), Event(9,17),
              Event(11,13), Event(12,15), Event(14,15)]
    print find_max_simultaneous_events(events)
