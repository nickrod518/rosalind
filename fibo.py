n = int(input())

prev_two = 0
prev_one = 1
curr = 1

for i in range(1, n):
    prev_one = prev_two
    prev_two = curr
    curr = prev_one + prev_two

print(curr)
