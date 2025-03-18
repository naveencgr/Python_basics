text = "ABCD"
current_index = 1
print(text[current_index-1:current_index])
print(text[current_index+1:current_index+2])

#for i in range(len(text)):
    #print(f"first-->{text[0:i]}")
    #print(f"second-->{text[i+1:]}")

def permutation(text, mutation=''):
    if len(text) == 0:
        print(mutation)
    else:
        for i in range(len(text)):
            newMutation = mutation + text[i]
            #print(newMutation) 
            newString = text[0:i] + text[i+1:]
            permutation(newString, newMutation)

permutation("ABCD")



