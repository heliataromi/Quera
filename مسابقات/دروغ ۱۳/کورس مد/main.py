def lis(arr):
    m = 0
    
    for i in range(len(arr)):
        temp_arr = []
        temp_arr.append(arr[i])
        
        if len(arr) - i > m:
            for j in range(i, len(arr)):
                if arr[j] > temp_arr[-1]:
                    temp_arr.append(arr[j])

        if len(temp_arr) > m:
            m = len(temp_arr)

    return(m)
      

n = int(input())
arr = list(map(int, input().split()))

print(lis(arr))
