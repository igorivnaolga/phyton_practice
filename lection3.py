import random

# l = [1,2,3,4,5]
# random.shuffle(l)
# print(l)
# coin = {1: "Orel", 2: "reshka"}
# count_o = 0
# count_r = 0
# sequence = []

# while count_o < 3 and count_r < 3:
#     choice = random.randint(1,2)

#     if choice == 1:
#         count_o +=1
#         count_r = 0
#     else:
#         count_r += 1
#         count_o = 0

#         side = coin[choice]
#         sequence.append(side)

#     print (sequence)
#     print(len(sequence))

# letters = ["A", "B", "C", "D", "E", "H"]
# nums = ["0","1","2","3","4","5","6","7","8","9"]

# l1 = random.choices(letters,k=2)
# l2 = random.choices(nums, k=4)
# l3 = random.choices(letters,k=2)

# print(l1 + l2 + l3)

# res = "".join(l1 + [" "] + l2 + [" "] + l3)
# print(res)

array = [4, 52, -3, 43]

array_sorted = sorted(array)

i = 0

while array_sorted != array:
    i += 1
    random.shuffle(array)
    print(f"# {i}, data: {array}")