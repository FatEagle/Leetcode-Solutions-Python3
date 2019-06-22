class Solution:
    def twoSum(self, nums, target):
        # Dict is a hash map in python
        map_ = {num: i for i, num in enumerate(nums)}
        print(map_)

        result = None
        for i, num in enumerate(nums):
            another = target - num

            if another in map_:
                another_i = map_[another]
                if another_i != i:
                    result = [i, another_i]
                    break

        if result is None:
            result = [0, 0]

        return result


if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    s = Solution()
    print(s.twoSum(nums, target))

    nums = [2, 5, 5, 11]
    target = 10
    print(s.twoSum(nums, target))
