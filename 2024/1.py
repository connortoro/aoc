arr_1 = []
arr_2 = []

with open("1.txt", "r") as file:
    for line in file:
        nums = line.strip().split()
        arr_1.append(int(nums[0]))
        arr_2.append(int(nums[1]))


# arr_1.sort()
# arr_2.sort()

# res = 0
# for i in range(len(arr_1)):
#     res += abs(arr_1[i] -arr_2[i])

# print(res)

# PART 2
right_map = {}
for num in arr_2:
    if num in right_map:
        right_map[num] += 1
    else:
        right_map[num] = 1

similarity_score = 0
for num in arr_1:
    if num in right_map:
        similarity_score += num*right_map[num]

print(similarity_score)
