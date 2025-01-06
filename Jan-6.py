class Solution:
    def sumClosest(self, arr, target):
        # Edge case: if the array has fewer than 2 elements, return an empty list
        if len(arr) < 2:
            return []

        # Sort the array for the two-pointer technique
        arr.sort()
        n = len(arr)

        # Initialize variables
        closest_pair = []
        min_diff = float('inf')

        # Two-pointer approach
        left, right = 0, n - 1

        while left < right:
            current_sum = arr[left] + arr[right]
            current_diff = abs(target - current_sum)

            # If a smaller difference is found, update closest_pair and min_diff
            if current_diff < min_diff:
                min_diff = current_diff
                closest_pair = [arr[left], arr[right]]
            elif current_diff == min_diff:
                # If differences are the same, prioritize the pair with max absolute difference
                if abs(arr[right] - arr[left]) > abs(closest_pair[1] - closest_pair[0]):
                    closest_pair = [arr[left], arr[right]]

            # Move pointers
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                # Exact match found
                return closest_pair

        return closest_pair
