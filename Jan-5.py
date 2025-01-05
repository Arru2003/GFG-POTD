class Solution:
    # Complete the below function
    def countPairs(self, arr, target):
        # Sort the array
        arr.sort()
        
        count = 0
        n = len(arr)

        # Use two pointers
        left, right = 0, n - 1

        while left < right:
            # Calculate the sum of the current pair
            pair_sum = arr[left] + arr[right]

            if pair_sum < target:
                # All pairs from left to right-1 will also satisfy the condition
                count += (right - left)
                left += 1
            else:
                # Decrease the right pointer
                right -= 1

        return count