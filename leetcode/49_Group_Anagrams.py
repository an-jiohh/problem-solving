import collections

strs = ["eat","tea","tan","ate","nat","bat"]
s = collections.defaultdict(list)
for i in strs :
    s[''.join(sorted(i))].append(i)
print(s)