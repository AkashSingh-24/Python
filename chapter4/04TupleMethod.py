a = (1, 23, 24, False, False, "rohan", "shivam")
print(a)
print(type(a))

# index method tuple
print(a.index("rohan"))

#count method tuple
n = a.count(False)
print(n)

# cocatenation method
a1 = (1, 2, 3)
a2 = (4, 5, 6,)
print(a1 + a2)

# '*' method
mult = (1, 2, 3)
repeat = mult*3
print(repeat)

# method len
print(len(a1))

# Slice method
a2 = (1, 2, 3, 4, 5)
slice = a2[1:4]
print(slice)

# unpacking method
ak = (1, 2, 3,)
a, b, c = ak
print(a, b, c)



