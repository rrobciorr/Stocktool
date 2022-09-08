import json

x = [1, 'simple', 'list']
f=""
z= json.dumps(x)
print(z)

print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
  
