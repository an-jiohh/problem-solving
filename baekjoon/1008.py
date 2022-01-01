a = int(input())
b = int(input())

b1 = int(b / 100)
b = b - b1 * 100
b2 = int(b / 10)
b = b - b2 * 10

print(a * b)
print(a * b2)
print(a * b1)
print(a * (b + b2 * 10 + b1 *100))