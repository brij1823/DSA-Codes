#Dont Forget to comine the list. That's the crux

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        combined_list = nums1+nums2
        combined_list = sorted(combined_list)
        length = len(combined_list)
        if(length%2):
            return (combined_list[length//2])
        else:
            print(combined_list)
            temp = (combined_list[length//2] + combined_list[length//2 - 1])
            return (float(temp)/2)