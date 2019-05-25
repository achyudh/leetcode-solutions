class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = 0
        ptr1, ptr2 = 0, 0
        output = []
        
        if not matrix:
            return output

        max_iter = len(matrix) * len(matrix[0])
        bounds = [len(matrix[0]) - 1, len(matrix) - 1, 0, 1]
        
        while len(output) < max_iter:
            if direction == 0:
                while ptr2 <= bounds[0]:
                    output.append(matrix[ptr1][ptr2])
                    ptr2 += 1
                bounds[0] -= 1
                ptr1 += 1
                ptr2 -= 1
            
            elif direction == 1:
                while ptr1 <= bounds[1]:
                    output.append(matrix[ptr1][ptr2])
                    ptr1 += 1
                bounds[1] -= 1
                ptr1 -= 1
                ptr2 -= 1
            
            elif direction == 2:
                while ptr2 >= bounds[2]:
                    output.append(matrix[ptr1][ptr2])
                    ptr2 -= 1
                bounds[2] += 1
                ptr1 -= 1
                ptr2 += 1
            
            else:
                while ptr1 >= bounds[3]:
                    output.append(matrix[ptr1][ptr2])
                    ptr1 -= 1
                bounds[3] += 1
                ptr1 += 1
                ptr2 += 1
            
            direction = (direction + 1) % 4
        
        return output
