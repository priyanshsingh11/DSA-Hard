from collections import deque
import sys

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj = [[] for _ in range(n)]
        for flight in flights:
            adj[flight[0]].append((flight[1], flight[2]))
        
        q = deque()
        q.append((0, src, 0))
        
        dist = [sys.maxsize] * n
        dist[src] = 0
        
        while q:
            stops, node, cost = q.popleft()
            
            if stops > k:
                continue
                
            for neighbor, weight in adj[node]:
                new_cost = cost + weight
                if new_cost < dist[neighbor] and stops <= k:
                    dist[neighbor] = new_cost
                    q.append((stops + 1, neighbor, new_cost))

        if (dist[dst] == sys.maxsize): return -1
        else:
            return dist[dst] 
