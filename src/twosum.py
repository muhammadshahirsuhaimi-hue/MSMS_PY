#brute-force solution:
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        resultList = []
        maxLen = len(nums)
        for i in range(maxLen):
            iVal = nums[i]
            for j in range(i+1, maxLen):
                jVal = nums[j]
                if (iVal + jVal == target):
                    resultList.append(i)
                    resultList.append(j)
                    break

        return resultList
    

#optimized using a single loop and dict
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store the value as key and its index as value
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            # O(1) average time lookup
            if complement in seen:
                return [seen[complement], i]

            # O(1) average time insertion
            seen[num] = i

        return []
