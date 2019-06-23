def binary_search(sorted_arr, x):
    lo = 0
    hi  = len(sorted_arr)
    while lo < hi:
        mid = (lo + hi) // 2        
        if sorted_arr[mid] < x: lo = mid + 1
        else: hi = mid
        #print( "lo = " + str(lo) + " hi = " + str(hi) + " mid = " + str(mid) )
    return lo

array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print( binary_search(array, 15) )
print( binary_search(array, 70) )
print( binary_search(array, -100) )
print( binary_search(array, 0) )
print( binary_search(array, 110) )
