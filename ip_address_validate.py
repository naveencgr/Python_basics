number = "192.168.0.12"

number_array = number.split(".")

print(number_array)

isValidIp = True

for num in number_array:
    if int(num) < 0 or int(num) > 255:
        isValidIp = False

print(f"Is Valid IP-->{isValidIp}")
