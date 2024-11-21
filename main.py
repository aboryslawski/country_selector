import random

ctries_dict = {}
sum_ppl = 0
file = open("ctries.csv", "r")
for x in file:
    split = x.split(",")
    if split[2] in ctries_dict:
        continue
    val = int(float(split[11]) * 1000)
    lower_bound = sum_ppl
    upper_bound = val + sum_ppl
    ctries_dict[split[2]] = [lower_bound, upper_bound]
    sum_ppl += val

random_val = random.randrange(sum_ppl) # poor fellow's fate is decided here
for x in ctries_dict:
    if random_val > ctries_dict[x][0] and random_val <= ctries_dict[x][1]:
        print(x)
