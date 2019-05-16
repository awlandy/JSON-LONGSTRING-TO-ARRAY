import json
import re
s = "Some loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong string"
stack = []
data = {}
length = int(len(s)/64 + 1)
index = 0
start = 0
end   = 64
for index in range(length):
    stack.append(s[start:end])
    start += 64
    end   += 64
data["paragraph"] = stack
with open('test.json', 'w') as f:  # writing JSON object
    json.dump(data, f, indent=4)
