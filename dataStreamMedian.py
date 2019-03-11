import heapq

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # loHeap is a max heap that stores numbers <= median
        self.loHeap = list()
        # hiHeap is a min heap that stores numbers >= median
        self.hiHeap = list()

    def addNum(self, num: int) -> None:
        if not self.loHeap:
            heapq.heappush(self.loHeap, -num)
                
        elif num < self.findMedian():
            # Insert into loHeap
            heapq.heappush(self.loHeap, -num)
            if len(self.loHeap) == len(self.hiHeap) + 2:
                heapq.heappush(self.hiHeap, -heapq.heappop(self.loHeap))
            
        else:
            # Insert into hiheap
            heapq.heappush(self.hiHeap, num)
            if len(self.hiHeap) == len(self.loHeap) + 1:
                heapq.heappush(self.loHeap, -heapq.heappop(self.hiHeap))

    def findMedian(self) -> float:
        if (len(self.loHeap) + len(self.hiHeap)) % 2 == 1:
            return -self.loHeap[0]
        else:
            return (self.hiHeap[0] - self.loHeap[0]) / 2


# Usage:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
