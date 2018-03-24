s = input()
r = ""

for i in range(len(s) - 1, -1, -1):
    if s[i] == "A":
        r = r + "T"
    elif s[i] == "T":
        r = r + "A"
    elif s[i] == "C":
        r = r + "G"
    else:
        r = r + "C"

print(r)
