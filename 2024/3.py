s = open("2024/3.txt").read()
res = 0
enabled = True

def check(st):
  global res
  nums = st.split(",")
  if len(nums) != 2 or not nums[0].isdigit() or not nums[1].isdigit():
    return
  res += int(nums[0]) * int(nums[1])

def toggle(st):
  global enabled
  while st:
    do_i = st.find("do()")
    dont_i = st.find("don't()")
    if do_i == -1 and dont_i == -1:
      return
    if do_i == -1:
      enabled = False
      print("DISABLING: ", st)
      return
    if dont_i == -1:
      print("ENABLING: ", st)
      enabled = True
      return
    i = min(do_i, dont_i)
    st = st[i+4:]


while i := s.find("mul("):
  toggle(s[:i])
  s = s[i+4:]
  i = s.find(")")
  if not i: break
  if enabled:
    check(s[:i])

print(res)
