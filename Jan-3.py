class Solution:
    def subarrayXor(self, arr, k):
        xor_map = {}  # To store frequency of XOR values
        prefix_xor = 0  # Cumulative XOR
        count = 0  # Count of subarrays with XOR = k

        for num in arr:
            # Update cumulative XOR
            prefix_xor ^= num

            # If the XOR itself is equal to k, increment count
            if prefix_xor == k:
                count += 1

            # Check if prefix_xor ^ k exists in the hashmap
            target = prefix_xor ^ k
            if target in xor_map:
                count += xor_map[target]

            # Update the frequency of the current prefix_xor
            xor_map[prefix_xor] = xor_map.get(prefix_xor, 0) + 1

        return count
