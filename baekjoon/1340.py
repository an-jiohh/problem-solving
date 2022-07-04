Month = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", 'December' ]
Month_name = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

N = input().split()

def check(year) :
    if year % 400 == 0 :
        return 1
    elif year % 4 == 0 and year % 100 != 0 :
        return 1
    return 0

Month_name[1] = 28 + check(int(N[2]))
day_sum = 0
for i in range(Month.index(N[0])) :
    day_sum += Month_name[i]

N[1] = int(N[1][:-1])
N[3] = list(map(int, N[3].split(":")))
day_sum += N[1] - 1
day_sum = day_sum * 24 * 60 + N[3][0] * 60 + N[3][1]
year_sum = (365 + check(int(N[2]))) * 24 * 60
print(day_sum / year_sum * 100)