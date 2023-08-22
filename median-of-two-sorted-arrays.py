class Solution:
    # Time Complexity O(n+n)
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        i = len(nums1) - 1
        j = len(nums2) - 1
        last = len(nums1) + len(nums2) - 1
        nums1.extend([0]*len(nums2))
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1
            last -= 1
        while j >= 0:
            nums1[last] = nums2[j]
            last -= 1
            j -= 1
        if len(nums1) < 1:
            return 0
        if len(nums1) % 2 == 1:
            return nums1[len(nums1) // 2]
        else:
            return (nums1[len(nums1) // 2 - 1] + nums1[len(nums1) // 2]) / 2
