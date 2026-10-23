#Implement safe_calculator(a, operator, b). Return the result of applying the operator to the two numbers. Supported operators are "+", "-", "*", "/", "%", and "**". If the operator is unknown, return "Invalid operator". If the operator is "/" or "%" and b is 0, return "Cannot divide by zero". Round division results to 2 decimal places.
def safe_calculator(a, operator, b):
    operators = ["+", "-", "*", "/", "%", "**"]
    if operator not in operators:
        return "Invalid operator"
    elif (operator == "/" or operator == "%") and (b == 0):
        return "Cannot divide by zero"
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b 
    elif operator == "/":
        return round(a/b, 2)
    elif operator == "%":
        return a % b 
    elif operator == "**":
        return a ** b 

print(safe_calculator(5, "+", 3))    
print()

#Implement deep_flatten(items). Return a flat list containing every non-list value from items, no matter how deeply nested the lists are. Students may need to research recursion. Preserve the left-to-right order.
def deep_flatten(items):
    result = []
    for each_thanq in items:
        if isinstance(each_thanq, list):
           dav = deep_flatten(each_thanq)
           result.extend(dav)
        else:
            result.append(each_thanq)
    return result

print(deep_flatten([[[1,[2]],3]]))
print()

#Implement dedupe_preserve_order(items). Return a new list with duplicate values removed while keeping the first time each value appeared. Do not use set for this challenge.
def dedupe_preserve_order(items):
    new_list = []
    for each_item in items:
        if each_item not in new_list:
            new_list.append(each_item)
    return new_list

print(dedupe_preserve_order([1,2,1,3,2]))
print()

#Implement chunk_list(items, size). Split items into smaller lists of length size. The final chunk may be shorter if there are not enough items left. If size is less than 1, return Invalid size.
def chunk_list(items, size):
    if size < 1:
        return "Invalid size"
    chunk = []
    start = 0
    while start < len(items):
        end = start + size
        slyz = items[start:end]
        chunk.append(slyz)
        start = start + size
    return chunk

print(chunk_list([1,2,3,4,5], 2))
print()

#Implement clean_words(words). Return a new list where each word is stripped of surrounding spaces and converted to lowercase. Ignore words that become empty after stripping. Use a list comprehension.
def clean_words(words):
    return [nulist.lower() for eachthing in words if (nulist := eachthing.strip()) != ""]
print(clean_words([" Apple ","BANANA"," mango "]))

