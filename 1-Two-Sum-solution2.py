class Solution:
    """
    Runtime: 36 ms, faster than 92.52% of Python3 online submissions for Two Sum.
    Memory Usage: 14.3 MB, less than 46.54% of Python3 online submissions for Two Sum.
    """
    def twoSum(self, nums, target):
        # Dict is a hash map in python
        map_ = {nums[0]: 0}

        for i, num in enumerate(nums[1:]):
            another = target - num
            try:
                return [map_[another], i + 1]
            except KeyError:
                map_[num] = i + 1


if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    s = Solution()
    print(s.twoSum(nums, target))

    nums = [2, 5, 5, 11]
    target = 10
    print(s.twoSum(nums, target))
