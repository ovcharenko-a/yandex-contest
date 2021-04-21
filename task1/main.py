

def get_step(data):
    max_v = max(data)
    min_v = min(data)
    delta = max_v - min_v
    flag_min = min_v
    for v in data:
        if v < flag_min:
                return -1
        flag_min = v
    return delta

with open("input.txt", "r") as f:
    n = f.readline()
    data = f.readline()
    data = [int(x) for x in data.split()]
    print(get_step(data))
