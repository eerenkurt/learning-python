x = input("write your prompt ").strip().lower()

if x == "42":
    print("yes")
elif x == "forty-two":
    print("yes")
elif x == "forty two":
    print("yes")
else:
    print("no")