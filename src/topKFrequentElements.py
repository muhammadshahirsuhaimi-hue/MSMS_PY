class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        for num in nums:
            if num in countMap:
                countMap[num] += 1
            else:
                countMap[num] = 1

        # Sort by value in descending order
        highest_first_map = dict(sorted(countMap.items(), key=lambda item: item[1], reverse=True))
        
        # 1. Convert the keys into a list
        sorted_keys = list(highest_first_map.keys())

        # 2. Extract the highest key
        highest_key = sorted_keys[:k]

        return highest_key