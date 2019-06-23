class Solution:
    """
    Runtime: 24 ms, faster than 99.90% of Python3 online submissions for Jewels and Stones.
    Memory Usage: 13.2 MB, less than 33.46% of Python3 online submissions for Jewels and Stones.
    """
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(S.count(j) for j in J)
