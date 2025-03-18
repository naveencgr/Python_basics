
str = "([{[]}])"

open_brakets = ["(", "[", "{"]

bracket_array = []

isValid = True

for bracket in str:
    if bracket in open_brakets:
        bracket_array.append(bracket)
    else:
       if(len(bracket_array) == 0):
           isValid = False
       else:
        element = bracket_array.pop()
        if element == "[" and  bracket != "]":
            isValid = False
            break
        elif element == "{" and bracket != "}":
            isValid = False
            break
        elif element == "(" and bracket != ")":
            isValid = False
            break

print(isValid)


