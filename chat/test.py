import re
  
def longestSubstring(str):
    letter = max(re.findall(r'[a-z]+', str), key = len)
    return letter

print(longestSubstring("This is just an example123 of an ExtrEmely long string"))
