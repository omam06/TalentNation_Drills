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
print()


#Implement grade_label(score). Return A for scores from 90 to 100, B for scores from 80 to 89, C for scores from 70 to 79, and F for scores below 70. If the score is less than 0 or greater than 100, return Invalid score. This fixes common comparison and branch-order bugs.
def grade_label(score):
    if score < 0 or score > 100:
        return "Invalid score" 
    elif score >= 90 and score <=100:
        return "A"
    elif score >= 80 and score <= 89:
        return "B"
    elif score >= 70 and score <= 79:
        return "C"
    elif score < 70:
        return "F"

print(grade_label(95))
print(grade_label(85))
print(grade_label(40))
print()

#Implement password_strength(password). Return Weak if the password has fewer than 8 characters. Return Medium if it has at least 8 characters but does not contain both letters and digits. Return Strong if it has at least 8 characters and contains at least one letter and at least one digit. Students may need to research isalpha and isdigit.
def password_strength(password):
    if len(password) < 8:
        return "Weak"

    has_letter = False
    has_digit = False

    for char in password:
        if char.isalpha():
            has_letter = True
        if char.isdigit():
            has_digit = True
    if has_letter is True and has_digit is True:
        return "Strong"
    
    else:
        return "Medium"
print(password_strength("abc12345"))
print(password_strength("abcdefgh"))
print(password_strength("abc12"))
print()

#Implement access_gate(age, has_id, is_banned). Use guard-clause style. Return Too young if age is less than 18. Return No ID if has_id is false. Return Banned if is_banned is true. Return Allowed only if all checks pass.
def access_gate(age, has_id, is_banned):
    if not isinstance(age, int):
        return "Age must be a number"
    if not isinstance(has_id, bool):
        return "has_id must have a boolean value"
    if not isinstance(is_banned, bool):
        return "is_banned must be a bool"
   
    
    if age < 18:
        return "Too young"
    if has_id is False:
        return "No ID"
    if is_banned is True:
        return "Banned"
    
    return "Allowed"
print(access_gate(25, True, False))
print(access_gate(17, True, False))
print(access_gate(25, False, False))