import random

def generate_random_list(length):
    r = []

    for _ in range(0, length):
        n = random.randint(0, 10)
        r.append(n)
    
    return r

def unique_list(data):
    s = set(data)
    r = list(s)
    return r

def reverse_list(data):
    data.sort(reverse = True)
    return data

data = generate_random_list(15)
print("data: ", data)

unique_data = unique_list(data)
print("uniquedata:", unique_data)

reverse_data = reverse_list(unique_data)
print("reverse data:", reverse_data)
