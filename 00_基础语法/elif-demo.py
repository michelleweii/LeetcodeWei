a = 18


if a<0:
    print("a<0")
elif a<10:
    print("a < 10")
elif a<20:
    print("a < 20")
elif a<30:
    print("a < 30")
else:
    print("a aaaa")

# a < 20
# 只会走一个

if a < 0:
    print("a<0")
if a < 10:
    print("a < 10")
if a < 20:
    print("a < 20")
if a < 30:
    print("a < 30")
else:
    print("a aaaa")
# a < 20
# a < 30
# 满足条件的都会在走

hashmap={"a":1, "b":2}
hashmap.pop("a") # hashmap的删除操作pop
print(hashmap)