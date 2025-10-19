#217. Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        # if you wanna add an element to the set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False
