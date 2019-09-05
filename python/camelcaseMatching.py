class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        results = list()
        
        for query in queries:
            ptr1, ptr2 = 0, 0
            isMatch = True
            
            while ptr1 < len(pattern) and ptr2 < len(query):
                if pattern[ptr1] == query[ptr2]:
                    ptr1 += 1
                    ptr2 += 1
                elif query[ptr2].islower():
                    ptr2 += 1
                else:
                    isMatch = False
                    break
            
            if ptr1 != len(pattern):
                isMatch = False
            else:
                while ptr2 < len(query):
                    if query[ptr2].islower():
                        ptr2 += 1
                    else:
                        isMatch = False
                        break
            
            results.append(isMatch)
            
        return results
