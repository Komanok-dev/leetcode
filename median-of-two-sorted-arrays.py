class Solution:
    # Time Complexity O(log min(m,n))
    # Space Complexity O(1)
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        total_lengh = len(nums1) + len(nums2)
        half = total_lengh // 2
        mid1 = (len(nums1) - 1) // 2
        mid2 = half - mid1 - 2

        while True:
            print('half =', half, 'mid1 =', mid1, 'mid2 =', mid2)
            left1 = nums1[mid1] if mid1 >= 0 else float('-inf')
            right1 = nums1[mid1+1] if mid1 < len(nums1) - 1 else float('inf')
            left2 = nums2[mid2] if mid2 >= 0 else float('-inf')
            right2 = nums2[mid2+1] if mid2 < len(nums2) - 1 else float('inf')

            if left1 <= right2 and left2 <= right1:
                if total_lengh % 2:
                    return min(right1, right2)
                else:
                    return (min(right1, right2) + max(left1, left2)) / 2
            elif left1 > right2:
                mid1 -= 1
                mid2 += 1
            else:
                mid1 += 1
                mid2 -= 1

    # Time Complexity O(n+n)
    # Space Complexity O(1)
    def findMedianSortedArrays2(self, nums1: list[int], nums2: list[int]) -> float:
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
