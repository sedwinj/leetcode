// https://leetcode.com/problems/median-of-two-sorted-arrays

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function (nums1, nums2) {
    /*
     * Approach: Create partitions nums1l, nums1r, nums2l, nums2r
     * such that no element in nums1l + nums2l exceeds any element
     * in nums1r + nums2r. O(log(m + n)) time.
     *
     * Determine median from resulting partitions.
     */

    // Ensure that nums1 is smaller than nums2
    if (nums1.length > nums2.length) {
        [nums1, nums2] = [nums2, nums1]
    }

    let left_size = Math.floor((nums1.length + nums2.length + 1) / 2)
    let [low, high] = [0, nums1.length]
    let [mid1, mid2] = [null, null]
    let [l1, l2, r1, r2] = [null, null, null, null]

    // Binary search for correct nums1 left partition size
    while (low <= high) {
        // Update midpoints
        mid1 = Math.floor((low + high) / 2)
        mid2 = left_size - mid1;

        [l1, l2, r1, r2] = [-Infinity, -Infinity, Infinity, Infinity]

        // Update values
        if (mid1 < nums1.length) {
            r1 = nums1[mid1]
        }
        if (mid2 < nums2.length) {
            r2 = nums2[mid2]
        }
        if (mid1 - 1 >= 0) {
            l1 = nums1[mid1 - 1]
        }
        if (mid2 - 1 >= 0) {
            l2 = nums2[mid2 - 1]
        }

        // Partitions are valid: exit loop
        if (l1 <= r2 && l2 <= r1) {
            break
        }

        // Partitions are not valid: adjust nums1 left partition
        if (l1 > r2) {
            high = mid1 - 1
        }
        else {
            low = mid1 + 1
        }
    }

    // Return median
    if ((nums1.length + nums2.length) % 2 == 1) {
        return Math.max(l1, l2)
    }
    return (Math.max(l1, l2) + Math.min(r1, r2)) / 2
};