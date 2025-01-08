class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # code here
        n = len(arr)
        arr.sort()  # Step 1: Sort the array
        count = 0

        # Step 2: Iterate for each third side (k)
        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1  # Two-pointer approach
            while i < j:
                if arr[i] + arr[j] > arr[k]:
                    count += (j - i)  # Count all valid pairs
                    j -= 1  # Move j backward
                else:
                    i += 1  # Move i forward
        
        return count

