d = {} # empty dictionary
marks = {
    "harry": 100,
    "shubham": 56,
    "rohan": 23,
    0: "harry"
}

#method items
# print(marks.items())

#method clear
# print(marks.clear())

#method key
# print(marks.keys())

#method values
# print(marks.values())

#method popitem
# print(marks.popitem())

#method pop
# print(marks.pop("harry"))

#method update
# marks.update({"harry": 99, "renuka": 100})
# print(marks)

# method get
print(marks.get("harry2")) # prints non
# print(marks["harry"]) # retrun an error

# print(marks.get("harry"))

print(marks.copy())



