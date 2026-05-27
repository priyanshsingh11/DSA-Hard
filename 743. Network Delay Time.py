from collections import deque
import heapq
import sys

class Solution(object):
    def networkDelayTime(self, times, n, k):
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))

        dist = [sys.maxsize] * (n + 1)
        dist[k] = 0
        heap = [(0, k)]

        while heap:
            time, node = heapq.heappop(heap)
            if time > dist[node]:
                continue
            for neighbour, weights in graph[node]:
                newtime = time + weights
                if newtime < dist[neighbour]:
                    dist[neighbour] = newtime
                    heapq.heappush(heap, (newtime, neighbour))
        
        ans = max(dist[1:])
        
        if ans == sys.maxsize:
            return -1
        return ans
