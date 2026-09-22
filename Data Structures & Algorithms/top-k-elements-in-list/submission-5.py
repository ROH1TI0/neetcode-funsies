class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = Counter(nums)
        
        sort = sorted(map, key = lambda x: map[x])
        return sort[-k:][::-1]
