# https://youtu.be/K8L6KVGG-7o
# https://stackoverflow.com/questions/5616822/python-regex-find-all-overlapping-matches

import re

s='1234567890'
p=re.compile(r'\d{3}')

ms=p.finditer(s)

for m in ms:
    print(m.group(0))
    

ms = re.finditer(r'(?=(\d{3}))',s)
results = [int(m.group(1)) for m in ms]
results
