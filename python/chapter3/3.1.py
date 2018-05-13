names = ['fengqian', 'zhangjiawei', 'caijie', 'dongyang']
print(names[0], names[1], names[2].title(), names[3].title())
names[0] = "feichanghao"
print(names)
names.append("good")
print(names)
names.insert(0, "the first ele")
print(names)
del names[1]
print(names)

good = names.pop()
print(names)
print(good)

first = names.pop(0)
print(names)
print(first)

names.remove("caijie")
print(names)