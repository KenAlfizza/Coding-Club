"""
Syntax of dictionaries
    dict = {"key" : "value", "anotherkey":2, "yetanotherkey[1,2,3]}
    get() method
    
    iterating through dictionary
"""

var = {"key":"value", "key2":3}
print(var["key"])
#print(var["key2"])

#print(var["key",0])
#print(var["key5",4])

print(var.get("key5",0))


for key in var:
    print(var[key])