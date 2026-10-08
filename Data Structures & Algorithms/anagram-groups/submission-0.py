class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group = {}

        for i in range(len(strs)):
            sort = "".join(sorted(strs[i]))

            if sort in group:
                group[sort].append(strs[i])
            else:
                group[sort] = [(strs[i])]
        
        return list(group.values())
