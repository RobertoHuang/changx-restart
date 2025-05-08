def bubble_sort(arr):
    """
    冒泡排序算法实现
    参数:
        arr: 需要排序的列表
    返回:
        排序后的列表
    """
    n = len(arr)
    # 外层循环控制需要进行多少轮比较
    for i in range(n):
        # 内层循环进行相邻元素比较和交换
        # 每轮结束后，最大的元素会"冒泡"到最后，所以可以减少比较次数
        for j in range(0, n - i - 1):
            # 如果前面的元素大于后面的元素，则交换它们
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 测试代码
if __name__ == "__main__":
    # 测试用例1：普通数组
    test_arr1 = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组1:", test_arr1)
    sorted_arr1 = bubble_sort(test_arr1)
    print("排序后数组1:", sorted_arr1)
    
    # 测试用例2：已排序数组
    test_arr2 = [1, 2, 3, 4, 5]
    print("\n原始数组2:", test_arr2)
    sorted_arr2 = bubble_sort(test_arr2)
    print("排序后数组2:", sorted_arr2)
    
    # 测试用例3：逆序数组
    test_arr3 = [5, 4, 3, 2, 1]
    print("\n原始数组3:", test_arr3)
    sorted_arr3 = bubble_sort(test_arr3)
    print("排序后数组3:", sorted_arr3) 