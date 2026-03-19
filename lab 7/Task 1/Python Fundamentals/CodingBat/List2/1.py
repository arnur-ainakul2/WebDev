def count_evens(nums):
  t=0
  for i in range(len(nums)):
    if nums[i]%2==0:
      t=t+1
  return t