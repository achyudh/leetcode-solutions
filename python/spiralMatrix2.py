class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return list()

        max_iter = n * n
        direction, i = 0, 1
        ptr1, ptr2 = 0, 0
        bounds = [n - 1, n - 1, 0, 1]
        output = [[0 for x in range(n)] for y in range(n)]
        
        while i <= max_iter:
            if direction == 0:
                while ptr2 <= bounds[0]:
                    output[ptr1][ptr2] = i
                    i += 1
                    ptr2 += 1
                bounds[0] -= 1
                ptr1 += 1
                ptr2 -= 1
            
            elif direction == 1:
                while ptr1 <= bounds[1]:
                    output[ptr1][ptr2] = i
                    i += 1
                    ptr1 += 1
                bounds[1] -= 1
                ptr1 -= 1
                ptr2 -= 1
            
            elif direction == 2:
                while ptr2 >= bounds[2]:
                    output[ptr1][ptr2] = i
                    i += 1
                    ptr2 -= 1
                bounds[2] += 1
                ptr1 -= 1
                ptr2 += 1
            
            else:
                while ptr1 >= bounds[3]:
                    output[ptr1][ptr2] = i
                    i += 1
                    ptr1 -= 1
                bounds[3] += 1
                ptr1 += 1
                ptr2 += 1
            
            direction = (direction + 1) % 4 
            
        return output
