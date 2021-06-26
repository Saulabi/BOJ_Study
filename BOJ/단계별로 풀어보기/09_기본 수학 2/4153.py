while True:
  nums = list(map(int, input().split()))
  max_num = max(nums)
  if max_num == 0:
    break
  nums.remove(max_num)
  if nums[0]**2 + nums[1]**2 == max_num**2:
    print('right')
  else:
    print('wrong')