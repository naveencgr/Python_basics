str = "aaabbbbakkdfksfslkfklkakfabcdefghijklmosdfklasfljkafklsafjkkasfkslkfjas"
target_str = ""
temp = ""
for s in str:
    #print(s)
    if s in temp:
        if len(temp) > len(target_str):
            #print(f"{temp} {target_str}")
            target_str = temp
            temp = ""
    else:
        temp += s        

print(target_str)        