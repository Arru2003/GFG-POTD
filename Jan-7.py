#Pair with given sum in a sorted array

class Solution:
    def countPairs(self, arr, target):
        left = 0
        right = len(arr) - 1
        count = 0
    
        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == target:
                # Handle duplicates
                if arr[left] == arr[right]:
                    n = right - left + 1  # Count duplicates between left and right
                    count += (n * (n - 1)) // 2  # Add combinations
                    break
                else:
                    # Count frequency of duplicates
                    left_count = 1
                    right_count = 1
                    while left + 1 < right and arr[left] == arr[left + 1]:
                        left += 1
                        left_count += 1
                    while right - 1 > left and arr[right] == arr[right - 1]:
                        right -= 1
                        right_count += 1
                    count += left_count * right_count
                    left += 1
                    right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        return count