from typing import List

def KadaneAlg(nums: List[int]) -> int:
        #This is also the max subarray leetcode problem
        dp = nums[0]
        max_sum = nums[0]
        for i in range(1,len(nums)):
                dp = max(nums[i], dp + nums[i])
                max_sum = max(max_sum, dp)
        return max_sum

def main():
        test_array = [[-2,1,-3,4,-1,2,1,-5,4]]

        for nums in test_array:
                print(f"Array: {nums}")
                print(f"Max Subarray Sum: {max_sub_array(nums)}\n")

if __name__ == "__main__":
        main()
