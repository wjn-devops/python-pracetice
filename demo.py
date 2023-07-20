def bubble_sort(arr):
    n = len(arr)
    print(f"n={n}")
    for i in range(n):
        print(f"i={i}")
        for j in range(0, n-i-1):
            print(f"j={j}")
            # 比较相邻的元素
            if arr[j] > arr[j+1]:
               arr[j],arr[j+1] =  arr[j+1], arr[j]




my_list = [4, -2, -5, 7, 1]
bubble_sort(my_list)
print(my_list)