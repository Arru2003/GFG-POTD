class Solution:
    def countSubarrays(self, arr, k):
        # Dictionary to store the frequency of prefix sums
        prefix_sum_count = {0: 1}
        current_sum = 0
        count = 0

        for num in arr:
            # Update the current prefix sum
            current_sum += num
        
            # Check if (current_sum - k) exists in the dictionary
            if (current_sum - k) in prefix_sum_count:
                count += prefix_sum_count[current_sum - k]
        
            # Update the frequency of the current prefix sum in the dictionary
            prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1

        return count