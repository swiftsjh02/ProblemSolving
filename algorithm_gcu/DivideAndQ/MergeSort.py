#merge sort
def merge_sort(list):
    if len(list) <= 1:
        return list
    num = int(len(list)/2)
    left = merge_sort(list[:num])
    right = merge_sort(list[num:])
    return merge(left, right)

def merge(left, right):
    r, l = 0, 0
    result = []
    while l<len(left) and r<len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += right[r:]
    result += left[l:]
    return result

if __name__ == '__main__':
    list = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    print(merge_sort(list))