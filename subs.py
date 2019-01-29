s = input()
s_len = len(s)

t = input()
t_len = len(t)

pos_found = []
curr_pos = 0

while curr_pos <= (s_len - t_len):
    sub_str_end = curr_pos + t_len
    sub_str = s[curr_pos:sub_str_end]

    if sub_str == t:
        pos_found.append(curr_pos + 1)

    curr_pos = curr_pos + 1

print(" ".join(map(str, pos_found)))
