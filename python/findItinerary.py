from collections import defaultdict


class Solution:
    def __init__(self):
        self.itinerary = ['JFK']
        self.graph = defaultdict(list)
        
    def nextDestination(self, ticketsLeft):
        if ticketsLeft == 0:
            return True
        
        elif not self.graph[self.itinerary[-1]]:
            return False
        
        for i0 in range(len(self.graph[self.itinerary[-1]])):
            nextCity = self.graph[self.itinerary[-1]].pop(i0)
            self.itinerary.append(nextCity)
            
            if self.nextDestination(ticketsLeft - 1):
                return True
            
            self.itinerary.pop()
            self.graph[self.itinerary[-1]].insert(i0, nextCity)
        
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        for ticket in tickets:
            self.graph[ticket[0]].append(ticket[1])
        
        for key in self.graph:
            if len(self.graph[key]) > 1:
                self.graph[key] = sorted(self.graph[key])
        
        self.nextDestination(len(tickets))
        
        return self.itinerary
