try:
    weight = int(input("Enter Weight: "))
    age = int(input("Enter Age: "))
    print(weight / age)
except ZeroDivisionError:
    print(" 0 is not allowed")    
except ValueError:
    print(" String values not allowed")


