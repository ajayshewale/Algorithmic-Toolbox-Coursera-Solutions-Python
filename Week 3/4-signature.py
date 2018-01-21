# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    segments = sorted(segments, key=lambda segment: segment.end)
    current = segments[0].end
    points.append(current)
    for s in segments:
        if ((current < s.start) or (current > s.end)):
            current = s.end
            points.append(current)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
