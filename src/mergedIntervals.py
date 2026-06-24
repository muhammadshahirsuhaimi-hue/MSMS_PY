class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. Always sort by the start time first!
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        
        for interval in intervals:
            # If the merged list is empty, or if the current interval 
            # does NOT overlap with the last merged one, add it directly.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # There is an overlap, so merge the current interval 
                # into the last merged interval by updating its end time.
                merged[-1][1] = max(merged[-1][1], interval[1])
                
        return merged