"""
Given a string as input. Check and print how many times character 'z' is present in the given string?
Input-> "zackz"
Output-> Total=2
"""

st = "zackz"
ln = len(st)
total = 0
for i in range(0,ln):
  ch = st[i]
  if(ch=="z"):
    total = total + 1
print(f"Total={total}")

