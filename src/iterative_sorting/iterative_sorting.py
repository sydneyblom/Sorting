# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i + 1, len(arr)):
            # Selecting the smallest value
            if arr[j] < arr[smallest_index]:
                smallest_index = j
         
        element1 = arr[i]
        element2 = arr[smallest_index]
        arr[i] = element2
        arr[smallest_index] = element1



    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    n = len(arr)
    for i in range(n): #traverse through all array elements
           # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr