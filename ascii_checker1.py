a1 = (input("Please enter your number or letter here:"))

ascii_val = ord(a1)
print(f"character: {a1}")
print(f"ASCII Value: {ascii_val}")

if ascii_val >= 65 and ascii_val <= 90:
    print("this is an uppercase letter.")

elif ascii_val >= 97 and ascii_val <= 122:
    print("this is a lowercase letter.")

elif ascii_val >= 48 and ascii_val <= 57:
    print("this is a digit.")
else:
    print("this is a symbol")


    