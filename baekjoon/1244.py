n = int(input())
arr = list(map(int, input().split()))
np = int(input())

def change(num) :
    if num == 1 : return 0
    else : return 1
for i in range(np) :
    xy, num = map(int, input().split())
    if xy == 1 :
        for j in range(num - 1, len(arr), num) :
            arr[j] = change(arr[j])
    else :
        arr[num - 1] = change(arr[num - 1])
        left, right = num - 2, num
        while left >= 0 and right < len(arr) :
            if arr[left] != arr[right] :
                break
            else : 
                arr[left] = change(arr[left])
                arr[right] = change(arr[right])
                left, right = left - 1, right + 1
counter = 0
for i in arr :
    print("{} ".format(i), end="")
    counter += 1
    if counter % 20 == 0 : print("")
print("")