class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ptr_a = 0
        ptr_b = len(height) - 1
        max_cap = -1
        
        while ptr_a < ptr_b:
            curr_height = min(height[ptr_a], height[ptr_b])
            curr_cap = curr_height * (ptr_b - ptr_a)
            if curr_cap > max_cap:
                max_cap = curr_cap
            
            if height[ptr_a] < height[ptr_b]:
                while ptr_a < len(height) - 1 and height[ptr_a] <= curr_height:
                    ptr_a += 1
            else:
                while ptr_b >= 0 and height[ptr_b] <= curr_height:
                    ptr_b -= 1
        
        return max_cap
