import itertools

a_list = [1, 2, 3, 4]
l2 = itertools.permutations(a_list)

valid_time = []
max_val = 0.0
for item in l2:
    # print(item)
    a, b, c, d = item
    # time_flt = float('{str(a)}{str(b)}.{str(c)}{str(d)}'.format(a, b, c, d))
    time_flt = float('{}{}.{}{}'.format(a, b, c, d))
    if 0.0 <= time_flt <= 23.59:
        print(time_flt)
        valid_time.append(time_flt)

max_val = max(valid_time)
print(max_val)
