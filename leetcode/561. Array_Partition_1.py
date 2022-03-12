nums = [1,4,3,2]

nums.sort()
count = 0
for n, i in enumerate(nums) :
    if n % 2 == 0 :
        count += i

print(count)