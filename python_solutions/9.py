with open("input_9.txt", "r") as f:
    lines = f.readlines()

nums = [int(line.strip()) for line in lines]
# for i, num in enumerate(nums[25:]):
#     preamble = set(nums[i:25 + i])
#     found_pair = False
#     for prenum in preamble:
#         diff = num - prenum
#         if diff in preamble:
#             found_pair = True
#             break
#     if not found_pair:
#         print(num)
#         break

invalid_num = 29221323

start_idx = 0
end_idx = -1
expand_upper = True # either expand the upper or the lower

cur_sum = 0
while True:
    if expand_upper:
        end_idx += 1
        cur_sum += nums[end_idx]
    else:
        cur_sum -= nums[start_idx]
        start_idx += 1

    if cur_sum > invalid_num:
        expand_upper = False
    elif cur_sum < invalid_num:
        expand_upper = True
    else:
        break

included_range = nums[start_idx : end_idx+1]
ans = min(included_range) + max(included_range)
print(ans)