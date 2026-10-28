from getopt import gnu_getopt

nums = [1,2,3,4,5]
nums_sum = 0
for item in nums:
    nums_sum += item
    print(nums_sum)

nums_2 = [145,457,234,892,12]
sorted_nums = sorted(nums_2)
print(sorted_nums[0], sorted_nums[-1])
print(min(nums_2), max(nums_2))

str_nums = ["1", "2", "3", "4", "5"]
nums_3 = []
for i in str_nums:
    nums_3.append(int(i))
    print(nums_3)

print([int(i) for i in nums])

# user_nums = (input("Введите свою цифру через запятую: ").split(',')
# user_nums_sum = sum([int(i) for i in user_nums])
#     print(user_nums)

