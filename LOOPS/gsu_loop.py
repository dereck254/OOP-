data = {'color':'red', 'fruit':'apple', 'pet':'dog', 'car':'larmboghini'}

while data:
    print("data: ", data)

keys = list(data.keys())
i = 0
while i < len(keys):
    key = keys[i]
    value = data[key]
    print(key + ':' + value_)
    i+=1