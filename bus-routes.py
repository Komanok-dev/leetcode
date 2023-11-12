from collections import defaultdict, deque


class Solution(object):
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        to_route = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                to_route[stop].add(i)
        result = -1
        visited = set()
        lookup = deque([source])
        while lookup:
            result += 1
            for _ in range (len(lookup)):
                next_stop = lookup.popleft()
                if next_stop == target:
                    return result
                for bus in to_route[next_stop]:
                    if bus not in visited:
                        visited.add(bus)
                        lookup.extend(routes[bus])
        return -1
