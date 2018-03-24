hamming_distance = 0

s = input()
t = input()

for i in range(len(s)):
    if s[i] != t[i]:
        hamming_distance = hamming_distance + 1

print(hamming_distance)
