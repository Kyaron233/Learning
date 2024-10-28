def Sort(m, n, nums1: list, nums2: list):
    idx1 = idx2 = 0
    new_list = [None] * (m + n)
    for i in range(0, m + n ):
        if idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] > nums2[idx2]:
                new_list[i] = nums2[idx2]
                idx2 += 1
            elif nums1[idx1] < nums2[idx2]:
                new_list[i] = nums1[idx1]
                idx1 += 1
            elif nums1[idx1] == nums2[idx2]:
                new_list[i] = nums1[idx1]
                idx2 += 1
        elif idx1 > len(nums1)-1:
            new_list[i] = nums2[idx2]
            idx2+=1
        elif idx2 > len(nums2)-1:
            new_list[i] = nums1[idx1]
            idx1+=1
    return new_list


test1 = [1, 2, 3, 4, 9, 100,200]
test2 = [5, 7, 9, 11, 13, 15,114514]
new_list = Sort(len(test1), len(test2), test1, test2)
print(new_list)
